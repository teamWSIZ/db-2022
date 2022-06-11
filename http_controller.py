import aiohttp_cors
from aiohttp import web, ClientSession
from aiohttp.abc import BaseRequest

from config import APP_PORT
from db_service.airbnb_db_service import User, AirbnbDbService
from db_service.db import DbService
from util import log, answer

routes = web.RouteTableDef()


# query = req.match_info.get('query', '')  # for route-resolving, /{query}
# query = req.rel_url.query['query']  # params; required; else .get('query','default')

@routes.get('/status')
async def hello(req: BaseRequest):
    log('status check')
    return answer(f'OK')


@routes.get('/')
async def rootpath(req: BaseRequest):
    return answer('db app is working fine')


@routes.get('/add')
async def add_numbers(req: BaseRequest):
    a = float(req.rel_url.query['a'])
    b = float(req.rel_url.query['b'])
    res = a + b

    return web.json_response({"result": res})


# ### Working with data

@routes.get('/users')
async def get_all_persons(req):
    return web.json_response([i.__dict__ for i in await db().get_all_users()])


@routes.post('/post')
async def create_user(req):
    data = await req.json()
    p = User(**data)
    log(f'attempt to create user {p}')
    success = await db().create_person(p)
    if success:
        log(f'saved: {p}')
        return answer('OK')
    else:
        log(f'failed to save: {p}')
        return answer(f'failed to save user for {p}', status=400)


# INITIATION
app = web.Application()
app.router.add_routes(routes)


def session() -> ClientSession:
    return app['http']


def db() -> DbService:
    return app['db']


#  setup generous CORS:
cors = aiohttp_cors.setup(app, defaults={
    "*": aiohttp_cors.ResourceOptions(
        allow_credentials=True,
        expose_headers="*",
        allow_headers="*",
    )
})

for route in list(app.router.routes()):
    cors.add(route)


##############
# App creation

async def pre_init():
    print('App initialization..')
    app['db'] = AirbnbDbService()
    await db().initalize()
    app['http'] = ClientSession()
    log('App initalization complete')


async def app_factory():
    await pre_init()
    return app


def run_it():
    web.run_app(app_factory(), port=APP_PORT)


run_it()

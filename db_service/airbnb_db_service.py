import asyncio
from dataclasses import dataclass
from datetime import datetime

import asyncpg
from asyncache import cached
from cachetools import TTLCache

from aio_basics.profile import log

DB_HOST = '10.10.0.33'
DB_DB = 'student'
DB_USER = 'student'
DB_PASS = 'wsiz#1234'


def dicts(rows):
    """
    Convert DB-rows to dictionaries.
    Note: use only for DB-rows, not for collections of objects.
    :param rows:
    :return:
    """
    return [dict(r) for r in rows]


@dataclass
class User:
    id: int
    name: str


@dataclass
class Villa:
    id: int
    rate: int
    city: str


class DataError(RuntimeError):
    """Raised when problems with save/update of dato to db occur (constraints etc)"""


async def create_pool():
    log(f'creating pool for db:{DB_HOST}:5432, db={DB_DB}')
    pool = await asyncpg.create_pool(host=DB_HOST, port=5432, database=DB_DB, user=DB_USER, password=DB_PASS)
    log(f'pool created')
    return pool


class AirbnbDbService:
    """ Prototype of DAO, data access object"""
    pool: asyncpg.pool.Pool

    async def initalize(self):
        self.pool = await create_pool()

    @cached(TTLCache(maxsize=10, ttl=2))
    async def get_all_users(self) -> list[User]:
        # fixme: list of selected id's?  await c.fetch('select * from airbnb.users where id = ANY ($1)', ids)
        log('getting users from db')
        async with self.pool.acquire() as c:
            rows = await c.fetch('select * from airbnb.users')  # -> list[Record] -- wynik zapytania
        return [User(**d) for d in dicts(rows)]

    async def create_user(self, u: User) -> User:
        async with self.pool.acquire() as c:
            res = await c.fetch('''
                        INSERT INTO airbnb.users(name)
                        VALUES ($1) RETURNING *''',
                                u.name)
            d = dict(res[0])
            return User(**d)

    async def update_user(self, u: User):
        async with self.pool.acquire() as c:
            try:
                res = await c.fetch('''
                                UPDATE airbnb.users
                                SET name=$2
                                WHERE id = $1
                                RETURNING *''', u.id, u.name)
                d = dict(res[0])
                return User(**d)
            except IndexError as e:
                raise DataError(f'User with id {u.id} does not exist; cannot update')

    async def delete_user(self, id: int):
        async with self.pool.acquire() as c:
            await c.execute('''
                            DELETE FROM airbnb.users
                            WHERE id = $1
                            ''', id)
            log(f'Removed user {id}')

    # fixme: CRUD for villas, catch all errors

    async def book_villa(self, uid: int, villaid: int):
        async with self.pool.acquire() as c:
            # ~~ sposoby reakcji na błędy związane z ograniczeniami na tabelach
            res = await c.fetch('''
                        INSERT INTO airbnb.uservillas(userid,villaid)
                        VALUES ($1,$2) ON CONFLICT(userid) DO UPDATE set userid=$1''',
                                uid, villaid)
        pass    # fixme: catch all errors


async def run_it():
    db = AirbnbDbService()
    await db.initalize()

    # u = await db.create_user(User(0, 'Wu'))
    # print(f'created user: {u}')
    try:
        await db.update_user(User(1, 'Xiao'))
    except DataError as e:
        print('ERROR:', e)

    persons = await db.get_all_users()
    # persons = await db.get_all_users()    # caching
    # persons = await db.get_all_users()
    for p in persons:
        print(p)
    await db.book_villa(3, 2)
    # await db.delete_user(1)


if __name__ == '__main__':
    asyncio.run(run_it())

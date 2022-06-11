from datetime import datetime
from dataclasses import dataclass, asdict
from aiohttp import web


def now_ts():
    return datetime.now().timestamp()


def clock():
    return datetime.now().strftime('%H:%M:%S.%f')


def log(what):
    print(f'[{clock()[:-3]}]: {what}')
from dataclasses import dataclass, asdict

from aiohttp import web


@dataclass
class RestResult:
    result: str


def simple_response(comment: str):
    return asdict(RestResult(comment))


def answer(comment: str, status=200):
    return web.json_response(simple_response(comment), status=status)

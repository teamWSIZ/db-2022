import asyncio
from dataclasses import dataclass

import asyncpg
from asyncache import cached
from cachetools import TTLCache

from aio_basics.profile import log
from config import *
from nfj_db_service.model import Company


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
    log(f'creating pool for db:{DB_HOST}:{DB_PORT}, db={DB_DB}')
    pool = await asyncpg.create_pool(host=DB_HOST, port=DB_PORT, database=DB_DB, user=DB_USER, password=DB_PASS)
    log(f'pool created')
    return pool


class NfjDbService:
    """ Prototype of DAO, data access object"""
    pool: asyncpg.pool.Pool

    async def initalize(self):
        self.pool = await create_pool()

    @cached(TTLCache(maxsize=10, ttl=2))
    async def get_all_companies(self) -> list[Company]:
        async with self.pool.acquire() as c:
            rows = await c.fetch('select * from companies order by name')  # -> list[Record] -- wynik zapytania
        return [Company(**d) for d in dicts(rows)]

    async def create_company(self, co: Company) -> Company:
        async with self.pool.acquire() as c:
            res = await c.fetch('''
                        INSERT INTO companies(name, url)
                        VALUES ($1, $2) RETURNING *''', co.name, co.url)
            d = dict(res[0])
            co1 = Company(**d)
            log(f'company {co1} updated')
            return co1

    async def update_company(self, co: Company):
        async with self.pool.acquire() as c:
            try:
                res = await c.fetch('''
                                UPDATE companies
                                SET name=$2, url=$3
                                WHERE company_id = $1
                                RETURNING *''', co.name, co.url)
                d = dict(res[0])
                co1 = Company(**d)
                log(f'company {co1} updated')
                return co1
            except IndexError as e:
                raise DataError(f'Company with id {co.company_id} does not exist; cannot update')

    async def delete_company(self, company_id: int):
        async with self.pool.acquire() as c:
            await c.execute('''
                            DELETE FROM companies
                            WHERE company_id = $1
                            ''', id)
            log(f'Removed company {id}')


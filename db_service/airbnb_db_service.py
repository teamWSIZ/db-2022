import asyncio
from dataclasses import dataclass
from datetime import datetime

import asyncpg
from asyncache import cached
from cachetools import TTLCache

from aio_basics.profile import log
from config import *
from db_service.utils import get_random_lastname


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
            rows = await c.fetch('select * from users order by name')  # -> list[Record] -- wynik zapytania
        return [User(**d) for d in dicts(rows)]

    async def create_user(self, u: User) -> User:
        async with self.pool.acquire() as c:
            res = await c.fetch('''
                        INSERT INTO users(name)
                        VALUES ($1) RETURNING *''',
                                u.name)
            d = dict(res[0])
            return User(**d)

    async def update_user(self, u: User):
        async with self.pool.acquire() as c:
            try:
                res = await c.fetch('''
                                UPDATE users
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
                            DELETE FROM users
                            WHERE id = $1
                            ''', id)
            log(f'Removed user {id}')

    # fixme: CRUD for villas, catch all errors
    # CRUD -- Create Read Update Delete  (dla każdego typu danych)
    # set / unset dla każdej relacji *:* (many-to-many)

    async def add_book_villa(self, uid: int, villaid: int) -> bool:
        async with self.pool.acquire() as c:
            # ~~ sposoby reakcji na błędy związane z ograniczeniami na tabelach
            try:
                res = await c.fetch('''
                            INSERT INTO uservillas(userid, villaid)
                            VALUES ($1,$2)''',
                                    uid, villaid)
                # ON CONFLICT(userid) DO UPDATE set userid=$1
                return True
            except RuntimeError:
                log(f'Error assigning userid {uid} to villaid {villaid}')
                return False

    async def del_book_villa(self, uid: int, villaid: int) -> bool:
        async with self.pool.acquire() as c:
            # ~~ sposoby reakcji na błędy związane z ograniczeniami na tabelach
            try:
                res = await c.fetch('''
                            DELETE FROM uservillas
                            WHERE userid=$1 AND villaid=$2''', uid, villaid)
                # ON CONFLICT(userid) DO UPDATE set userid=$1
                return True
            except RuntimeError:
                log(f'Error unassigning userid {uid} to villaid {villaid}')
                return False


async def run_it():
    db = AirbnbDbService()
    await db.initalize()

    # u = await db.create_user(User(0, get_random_lastname()))

    try:
        await db.update_user(User(13, 'Xiao!!'))
    except DataError as e:
        print('ERROR:', e)

    users = await db.get_all_users()
    for u in users:
        print(u)

    # await db.add_book_villa(3, 2)
    # await db.delete_user(1)


if __name__ == '__main__':
    asyncio.run(run_it())

import asyncio
import json

import aioredis

from redis_client.model import User


class UsersDao:
    redis = None
    key: str

    def __init__(self) -> None:
        self.redis = aioredis.from_url('redis://10.10.28.44:6381')
        self.key = 'users'

    async def save_user(self, u: User):
        # kod który zapamięta dane usera w bazie....
        field = 'u' + str(u.uid)
        value = json.dumps(u.__dict__)
        await self.redis.hset(self.key, field, value)

    async def get_user_by_id(self, uid: int):
        field = 'u' + str(uid)
        res = (await self.redis.hget(self.key, field)).decode()
        dic = json.loads(res)
        user = User(**dic)
        print(user)

async def main():
    db = UsersDao()
    u = User(1, 'Wacław Konieczny', 'XXX1')
    await db.save_user(u)
    await db.get_user_by_id(1)

if __name__ == '__main__':
    asyncio.run(main())

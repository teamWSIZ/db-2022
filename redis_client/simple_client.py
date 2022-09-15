import asyncio
from random import randint

import aioredis

from aio_basics import profile
from aio_basics.profile import ts

"""
Installation (of redis): 
docker run --name some-redis1 -p 6380:6379 -d redis redis-server --save 60 1 --loglevel warning
[https://hub.docker.com/_/redis/]

Client:
https://aioredis.readthedocs.io/en/latest/getting-started/
"""


async def go_fast(redis, count):
    st = ts()
    for i in range(count):
        user_id = randint(0,10**9)
        await redis.sadd('lol12', f'user:{user_id}')
    end = ts()
    print(f'Saving {count} users took {end-st:.3f}s, i.e. {int(count/(end-st))} RPS')



async def main():
    redis = aioredis.from_url('redis://10.10.28.44:6381')
    # await redis.set('my-key', 3.14)
    # value = await redis.get('my-key')
    # print(type(value))  # bytes
    # print(value.decode())
    gamers = await redis.smembers('lol1155')
    print(gamers)
    for g in gamers:
        print(g.decode())
    await go_fast(redis, 1000)


if __name__ == "__main__":
    asyncio.run(main())

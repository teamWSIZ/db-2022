import asyncio

from db_service.airbnb_db_service import AirbnbDbService


async def run_it():
    db = AirbnbDbService()
    await db.initalize()

    await db.tx_test()


if __name__ == '__main__':
    asyncio.run(run_it())

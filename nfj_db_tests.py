# will make it proper soon
import asyncio

from nfj_db_service.model import Company
from nfj_db_service.nfj_db_service import NfjDbService


async def tests():
    db = NfjDbService()
    await db.initalize()
    await db.create_company(Company(0, 'ACME2', 'http://acme.wtf'))

if __name__ == '__main__':
    asyncio.run(tests())

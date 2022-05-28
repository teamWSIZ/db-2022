import unittest

from db_service.airbnb_db_service import AirbnbDbService, User


class SomeTests(unittest.IsolatedAsyncioTestCase):

    # @unittest.skip('--')
    async def test_list_users(self):
        db = AirbnbDbService()
        await db.initalize()
        u = await db.create_user(User(0, 'Wu'))
        assert u.id > 0


if __name__ == '__main__':
    unittest.main()

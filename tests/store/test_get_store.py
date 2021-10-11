from fixtures.store.model import StoreResponse


class TestUpdateUserInfo:
    def test_add_store(self, app, user_info):
        """
        Steps.

            1. Try to login user with valid data
            2. Change user data
            3. Check that status code is 200
            4. Check response
        """
        name_store = 1
        res = app.store.get_store_store(
            name_store=name_store, header=user_info.header, type_response=StoreResponse
        )
        assert res.status_code == 201

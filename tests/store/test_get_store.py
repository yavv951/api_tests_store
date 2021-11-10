from fixtures.store.model import StoreResponse


class TestStore:
    def test_get_store_info(self, app, store):
        """
        Steps.
            1. Register new user
            2. Access to store with valid data
            3. Add user info
            4. Add store
            5. Try to get info about created store
            6. Check that status code is 200
            7. Check response
        """
        res = app.store.get_store(
            name_store=store.store,
            header=store.header,
            type_response=StoreResponse,
        )
        assert res.status_code == 200, "Check status code"

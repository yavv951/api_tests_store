# import pytest
from fixtures.userinfo.model import UserInfo, UserInfoResponse


class TestUserInfo:
    def test_add_user_info(self, app, auth_user):
        """
        Steps.

            1. Try to login user with valid data
            2. Add user info
            3. Check that status code is 200
            4. Check response
        """
        data = UserInfo.random()
        res = app.userinfo.add_user_info(
            user_id=auth_user.user_uuid,
            data=data,
            type_response=UserInfoResponse,
            header=auth_user.header,
        )
        assert res.status_code == 200

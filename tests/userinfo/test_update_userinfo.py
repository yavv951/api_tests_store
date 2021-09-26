# import pytest
from fixtures.userinfo.model import (
    UserInfo,
    UpdateUserInfo,
    UpdateUserInfoResponse,
    UserInfoResponse,
)


class TestUpdateUserInfo:
    def test_update_userinfo(self, app, auth_user):
        """
        Steps.

            1. Try to login user with valid data
            2. Add user info
            3. Change user data
            4. Check that status code is 200
            5. Check response
        """
        data = UserInfo.random()
        app.userinfo.add_user_info(
            user_id=auth_user.uuid,
            data=data,
            type_response=UserInfoResponse,
            header=auth_user.header,
        )
        data = UpdateUserInfo.random()
        res = app.userinfo.change_user_data(
            user_id=auth_user.uuid,
            data=data,
            type_response=UpdateUserInfoResponse,
            header=auth_user.header,
        )
        assert res.status_code == 200

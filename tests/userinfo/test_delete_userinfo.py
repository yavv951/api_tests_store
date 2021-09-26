import pytest

from fixtures.constants import ResponseText
from fixtures.register.model import RegisterUser, RegisterUserResponse
from fixtures.auth.model import AuthUser
from fixtures.userinfo.model import UserInfo, UpdateUserInfo, DeleteUserInfoResponse, UserInfoResponse


class TestUpdateUserInfo:
    def test_update_userinfo(self, app, auth_user):
        """
        Steps.

            1. Try to login user with valid data
            2. Check that status code is 200
            3. Check response
        """
        data = UserInfo.random()
        app.userinfo.add_user_info(user_id=auth_user.uuid, data=data, type_response=UserInfoResponse,
                                   header=auth_user.header)
        res = app.userinfo.delete_user_info(user_id=auth_user.uuid, type_response=DeleteUserInfoResponse,
                                            header=auth_user.header)
        assert res.status_code == 200




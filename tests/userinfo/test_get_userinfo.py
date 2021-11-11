# import pytest
from fixtures.userinfo.model import (
    UserInfo,
    DeleteUserInfoResponse,
    UserInfoResponse,
    GetUserInfoResponse,
)


class TestGetUserInfo:
    def test_get_userinfo(self, app, auth_user):
        """
        Steps.

            1. Try to login user with valid data
            2. Add user info
            3. Change user data
            4. Get update user info
            5. Check that status code is 200
            6. Check response
        """
        data = UserInfo.random()
        app.userinfo.add_user_info(
            user_id=auth_user.user_uuid,
            data=data,
            type_response=UserInfoResponse,
            header=auth_user.header,
        )
        res = app.userinfo.get_user_info(
            user_id=auth_user.user_uuid,
            type_response=GetUserInfoResponse,
            header=auth_user.header,
        )
        assert res.status_code == 200

    def test_get_deleted_userinfo(self, app, auth_user):
        """
        Steps.

            1. Try to login user with valid data
            2. Add user info
            3. Delete user data
            4. Get delete user info
            5. Check that status code is 404(data is not found)
            6. Check response
        """
        data = UserInfo.random()
        app.userinfo.add_user_info(
            user_id=auth_user.user_uuid,
            data=data,
            type_response=UserInfoResponse,
            header=auth_user.header,
        )
        app.userinfo.delete_user_info(
            user_id=auth_user.user_uuid,
            type_response=DeleteUserInfoResponse,
            header=auth_user.header,
        )
        res = app.userinfo.get_user_info(
            user_id=auth_user.user_uuid,
            type_response=GetUserInfoResponse,
            header=auth_user.header,
        )
        assert res.status_code == 404

# import pytest
from common_models import MessageResponse
from fixtures.constants import ResponseText
from fixtures.userinfo.model import (
    UserInfo,
    DeleteUserInfoResponse,
    UserInfoResponse,
    GetUserInfoResponse,
)


class TestGetUserInfo:
    def test_get_userinfo(self, app, user_info):
        """
        Steps.
        1. Register new user
        2. Access to store
        3. Add user info
        4. Try to get user info
        5. Check that status code is 200
        6. Check response
        """
        res = app.userinfo.get_user_info(
            user_id=user_info.user_uuid,
            header=user_info.header,
            type_response=GetUserInfoResponse,
        )
        assert res.status_code == 200, "Check status code"
        assert res.data.city == user_info.user_info.address.city, "Check city"
        assert res.data.street == user_info.user_info.address.street, "Check street"
        assert res.data.email == user_info.user_info.email, "Check email"

    def test_get_deleted_userinfo(self, app, user_info):
        """
        Steps.
        1. Register new user
        2. Access to store
        3. Add user info
        4. Try to get info of non-existent user
        5. Check that status code is 404
        6. Check response
        """
        res = app.userinfo.get_user_info(
            user_id=1000,
            header=user_info.header,
            type_response=MessageResponse,
        )
        assert res.status_code == 404, "Check status code"
        assert res.data.message == ResponseText.MESSAGE_INFO_NOT_FOUND

import pytest
from fixtures.userinfo.model import UpdateUserInfo, UpdateUserInfoResponse


class TestUpdateUserInfo:
    def test_update_userinfo(self, app, user_info):
        """
        Steps.

            1. Try to login user with valid data
            2. Change user data
            3. Check that status code is 200
            4. Check response
        """
        data = UpdateUserInfo.random()
        res = app.userinfo.change_user_data(
            user_id=user_info.uuid,
            data=data,
            type_response=UpdateUserInfoResponse,
            header=user_info.header,
        )
        assert res.status_code == 200

    @pytest.mark.parametrize("uuid", ["ffddass", "@/&", -55, True])
    def test_update_invalid_id_userinfo(self, app, user_info, uuid):
        """
        Steps.

            1. Try to login user with valid data
            2. Change user info with invalid uuid
            3. Check that status code is 404
            4. Check response
        """
        data = UpdateUserInfo.random()
        res = app.userinfo.change_user_data(
            user_id=uuid,
            data=data,
            type_response=None,
            header=user_info.header,
        )
        assert res.status_code == 404

    def test_none_exist_id_userinfo(self, app, user_info, uuid=1000):
        """
        Steps.

            1. Try to login user with valid data
            2. Change user data with invalid uuid
            3. Check that status code is 404
            4. Check response
        """
        data = UpdateUserInfo.random()

        res = app.userinfo.change_user_data(
            user_id=uuid,
            data=data,
            type_response=None,
            header=user_info.header,
        )
        assert res.status_code == 404

    @pytest.mark.xfail(reason="Ожидается 400 ошибка")
    def test_invalid_phone_userinfo(self, app, user_info, phone="1" * 10000):
        """
        Steps.

            1. Try to login user with valid data
            2. Change user data invalid phone
            3. Check that status code is 400
            4. Check response
        """
        data = UpdateUserInfo.random()
        setattr(data, "phone", phone)
        res = app.userinfo.change_user_data(
            user_id=user_info.uuid,
            data=data,
            type_response=None,
            header=user_info.header,
        )
        assert res.status_code == 400

    def test_update_userinfo_wo_header(self, app, user_info):
        """
        Steps.

            1. Try to login user with valid data
            2. Change user data with None token
            3. Check that status code is 200
            4. Check response
        """
        data = UpdateUserInfo.random()
        res = app.userinfo.change_user_data(
            user_id=user_info.uuid,
            data=data,
            type_response=None,
            header=None,
        )
        assert res.status_code == 401

    def test_update_userinfo_invalid_header(self, app, user_info):
        """
        Steps.

            1. Try to login user with valid data
            2. Change user data with invalid token
            3. Check that status code is 200
            4. Check response
        """
        data = UpdateUserInfo.random()
        header = {"Authorization": "JWT 895241"}
        res = app.userinfo.change_user_data(
            user_id=user_info.uuid, data=data, type_response=None, header=header
        )
        assert res.status_code == 401

from fixtures.userinfo.model import UserInfo, DeleteUserInfoResponse, UserInfoResponse


class TestDeleteUserInfo:
    def test_delete_userinfo(self, app, auth_user):
        """
        Steps.

            1. Try to login user with valid data
            2. Add user info
            3. Delete user data
            4. Check that status code is 200
            5. Check response
        """
        data = UserInfo.random()
        app.userinfo.add_user_info(
            user_id=auth_user.user_uuid,
            data=data,
            type_response=UserInfoResponse,
            header=auth_user.header,
        )
        res = app.userinfo.delete_user_info(
            user_id=auth_user.user_uuid,
            type_response=DeleteUserInfoResponse,
            header=auth_user.header,
        )
        assert res.status_code == 200

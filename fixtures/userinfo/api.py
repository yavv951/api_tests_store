from requests import Response

from fixtures.userinfo.model import UserInfo
from fixtures.validator import Validator
from common.deco import logging as log


class Userinfo(Validator):
    def __init__(self, app):
        self.app = app

    POST_USERINFO = "/user_info/{}"

    @log("Add user info")
    def add_user_info(self, user_id: int, data: UserInfo, header=None, type_response=None) -> Response:
        """
        https://app.swaggerhub.com/apis-docs/berpress/flask-rest-api/1.0.0#/userInfo/userInfoAdd # noqa
        """
        response = self.app.client.request(
            method="POST",
            url=f"{self.app.url}{self.POST_USERINFO.format(user_id)}",
            json=data.to_dict(),
            headers=header
        )
        return self.structure(response, type_response=type_response)

    PUT_USERINFO = "/user_info/{}"

    @log("Update user info")
    def change_user_data(self,user_id: int, data: UserInfo, header=None, type_response=None):
        """
        https://app.swaggerhub.com/apis-docs/berpress/flask-rest-api/1.0.0#/userInfo/userInfoUpdate # noqa
        """
        response = self.app.client.request(
            method="PUT",
            url=f"{self.app.url}{self.PUT_USERINFO.format(user_id)}",
            json=data.to_dict(),
            headers=header
        )
        return self.structure(response, type_response=type_response)

    DELETE_USERINFO = "/user_info/{}"

    @log("Update user info")
    def delete_user_info(self, user_id: int, header=None, type_response=None):
        """
        https://app.swaggerhub.com/apis-docs/berpress/flask-rest-api/1.0.0#/userInfo/userInfoDelete # noqa
        """
        response = self.app.client.request(
            method="DELETE",
            url=f"{self.app.url}{self.DELETE_USERINFO.format(user_id)}",
            headers=header
        )
        return self.structure(response, type_response=type_response)

    GET_USERINFO = "/user_info/{}"

    @log("Update user info")
    def get_user_info(self, user_id: int, header=None, type_response=None):
        """
        https://app.swaggerhub.com/apis-docs/berpress/flask-rest-api/1.0.0#/userInfo/userInfoDelete # noqa
        """
        response = self.app.client.request(
            method="GET",
            url=f"{self.app.url}{self.GET_USERINFO.format(user_id)}",
            headers=header
        )
        return self.structure(response, type_response=type_response)
from requests import Response

from fixtures.auth.model import AuthUser
from fixtures.validator import Validator
from common.deco import logging as log


class LogIn(Validator):
    def __init__(self, app):
        self.app = app

    POST_AUTH = "/auth"

    @log("Auth user")
    def login(self, data: AuthUser, type_response=None) -> Response:
        """
        https://app.swaggerhub.com/apis-docs/berpress/flask-rest-api/1.0.0#/auth/authUser # noqa
        """
        response = self.app.client.request(
            method="POST",
            url=f"{self.app.url}{self.POST_AUTH}",
            json=data.to_dict(),
        )
        return self.structure(response, type_response=type_response)

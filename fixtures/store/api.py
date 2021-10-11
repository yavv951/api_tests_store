from requests import Response

# from fixtures.userinfo.model import UserInfo
from fixtures.validator import Validator
from common.deco import logging as log


class AddStore(Validator):
    def __init__(self, app):
        self.app = app

    POST_STORE = "/store/{}"

    @log("Add store")
    def add_store(self, name_store: str, header=None, type_response=None) -> Response:
        """
        https://app.swaggerhub.com/apis-docs/berpress/flask-rest-api/1.0.0#/storeMagazine/storeAdd # noqa
        """
        response = self.app.client.request(
            method="POST",
            url=f"{self.app.url}{self.POST_STORE.format(name_store)}",
            headers=header,
        )
        return self.structure(response, type_response=type_response)

    GET_STORE = "/store/{}"

    @log("GEt store")
    def get_store(self, name_store: str, header=None, type_response=None):
        """
        https://app.swaggerhub.com/apis-docs/berpress/flask-rest-api/1.0.0#/storeMagazine/storeGet # noqa
        """
        response = self.app.client.request(
            method="GET",
            url=f"{self.app.url}{self.GET_STORE.format(name_store)}",
            headers=header,
        )
        return self.structure(response, type_response=type_response)

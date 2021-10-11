import logging
import pytest

# from common_models import UserStore
from fixtures.app import StoreApp
from fixtures.auth.model import AuthUserResponse, UserType
from fixtures.register.model import RegisterUser, RegisterUserResponse

# from fixtures.store.model import Store, StoreResponse
from fixtures.userinfo.model import UserInfo, UserInfoResponse

logger = logging.getLogger("api")


@pytest.fixture(scope="session")
def app(request):
    url = request.config.getoption("--api-url")
    logger.info(f"Start api tests, url is {url}")
    return StoreApp(url)


def pytest_addoption(parser):
    parser.addoption(
        "--api-url",
        action="store",
        help="enter api url",
        default="https://stores-tests-api.herokuapp.com",
    ),


@pytest.fixture
def auth_user(app):
    data = RegisterUser.random()
    res_register = app.register.register(data=data, type_response=RegisterUserResponse)
    res_auth = app.auth.login(data=data, type_response=AuthUserResponse)
    token = res_auth.data.access_token
    header = {"Authorization": f"JWT {token}"}
    user_uuid = res_register.data.uuid
    return UserType(header, user_uuid)


@pytest.fixture
def user_info(app, auth_user):
    data = UserInfo.random()
    app.userinfo.add_user_info(
        user_id=auth_user.uuid,
        data=data,
        type_response=UserInfoResponse,
        header=auth_user.header,
    )
    return UserType(header=auth_user.header, uuid=auth_user.uuid, user_data=data)


"""@pytest.fixture
def store(app, auth_user):
    name_store = Store.random()
    res = app.store.add_store(
        name_store=name_store, header=user_info.header, type_response=StoreResponse
    )
    data_store = UserStore(**user_info.to_dict())
    data_store.store = name_store
    data_store.store_uuid = res.data.uuid
    return data_store"""

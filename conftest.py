import logging
import pytest
from common_models import UserStore
from fixtures.app import StoreApp
from fixtures.auth.model import AuthUserResponse, UserType
from fixtures.register.model import RegisterUser, RegisterUserResponse
from fixtures.store.model import Store, StoreResponse
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
def register_user(app) -> UserStore:
    """
    Register new user
    """
    data = RegisterUser.random()
    res = app.register.register(data=data, type_response=RegisterUserResponse)
    data = UserStore(user=data, user_uuid=res.data.uuid)
    return data

@pytest.fixture
def auth_user(app, register_user):
    res = app.auth.login(data=register_user.user, type_response=AuthUserResponse)
    token = res.data.access_token
    header = {"Authorization": f"JWT {token}"}
    data = UserStore(**register_user.to_dict())
    data.header = header
    return data

@pytest.fixture
def user_info(app, auth_user):
    data = UserInfo.random()
    app.userinfo.add_user_info(
        user_id=auth_user.user_uuid,
        data=data,
        type_response=UserInfoResponse,
        header=auth_user.header,
    )
    data_user = UserStore(**auth_user.to_dict())
    data_user.user_info = data
    return data_user


@pytest.fixture
def store(app, user_info) -> UserStore:
    """
    Add store
    """
    name_store = Store.random()
    res = app.store.add_store(
        name_store=name_store,
        header=user_info.header,
        type_response=StoreResponse,
    )
    data_store = UserStore(**user_info.to_dict())
    data_store.store = name_store
    data_store.store_uuid = res.data.uuid
    return data_store



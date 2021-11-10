from faker import Faker
import attr

from fixtures.base import BaseClass

fake = Faker()


@attr.s
class Address:
    city: str = attr.ib(default=None)
    street: str = attr.ib(default=None)
    home_number: str = attr.ib(default=None)


@attr.s
class UserInfo(BaseClass):
    phone: str = attr.ib(default=None)
    email: str = attr.ib(default=None)
    address: Address = attr.ib(default=None)

    @staticmethod
    def random():
        address = Address(city=fake.city(), street=fake.street_name(), home_number=fake.building_number())
        return UserInfo(phone=fake.phone_number(), email=fake.email(), address=address)

@attr.s
class UserInfoResponse:
    message: str = attr.ib()

@attr.s
class UpdateUserInfo(BaseClass):
    phone: str = attr.ib(default=None)
    email: str = attr.ib(default=None)
    address: Address = attr.ib(default=None)

    @staticmethod
    def random():
        address = Address(city=fake.city(), street=fake.street_name(), home_number=fake.building_number())
        return UpdateUserInfo(phone=fake.phone_number(), email=fake.email(), address=address)

@attr.s
class UpdateUserInfoResponse:
    message: str = attr.ib(validator=attr.validators.instance_of(str))

@attr.s
class DeleteUserInfo(BaseClass):
    uuid: int = attr.ib(validator=attr.validators.instance_of(str))


@attr.s
class DeleteUserInfoResponse:
    message: str = attr.ib(validator=attr.validators.instance_of(str))


@attr.s
class GetUserInfo(BaseClass):
    uuid: int = attr.ib(validator=attr.validators.instance_of(int))


@attr.s
class GetUserInfoResponse:
    phone: str = attr.ib(default=None, validator=attr.validators.instance_of(str))
    email: str = attr.ib(default=None, validator=attr.validators.instance_of(str))
    city: str = attr.ib(default=None, validator=attr.validators.instance_of(str))
    street: str = attr.ib(default=None, validator=attr.validators.instance_of(str))
    home_number: str = attr.ib(default=None, validator=attr.validators.instance_of(str))
    address: Address = attr.ib(default=None)
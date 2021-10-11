from typing import List

from faker import Faker
import attr

fake = Faker()


@attr.s
class Store:
    name: str = attr.ib(default=None)

    @staticmethod
    def random():
        name = fake.company()
        return name


@attr.s
class StoreResponse:
    name: str = attr.ib(default=None, validator=attr.validators.instance_of(str))
    uuid: int = attr.ib(default=None, validator=attr.validators.instance_of(int))
    items: List[str] = attr.ib(
        default=None,
        validator=attr.validators.deep_iterable(
            member_validator=attr.validators.instance_of(str),
            iterable_validator=attr.validators.instance_of(list),
        ),
    )

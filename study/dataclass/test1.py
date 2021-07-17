from dataclasses import dataclass


# ref> https://docs.python.org/ko/3.7/library/dataclasses.html
# 아래 세가지가 동일하다.
@dataclass
class C:
    ...


@dataclass()
class D:
    ...


@dataclass(
    init=True, repr=True, eq=True, order=False, unsafe_hash=False, frozen=False
)  # noqa : E501
class E:
    ...

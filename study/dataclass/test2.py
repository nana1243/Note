from dataclasses import asdict, dataclass, field
from typing import List


@dataclass
class C:
    x: int
    y: int = field(repr=False)
    z: int = field(repr=False, default=10)
    t: int = 20


c = C(x=1, y=2)
print(c)


@dataclass
class Point:
    x: int
    y: int


@dataclass
class C:
    mylist: List[Point]


p1 = Point(1, 2)
p2 = Point(1, 3)
p3 = Point(1, 4)

c = C(mylist=[p1, p2, p3])

print(asdict(p1))
print(asdict(c))

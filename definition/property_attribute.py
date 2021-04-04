# https://stackoverflow.com/questions/52162720/why-are-properties-class-attributes-in-python

"""
variables:
    - 값을 저장할 수 있는 메모리 공간에 붙은 이름
attribute:
    - In computing, an attribute is a specification
    that defines a property of an object, element
properties:
    - Properties are always class attributes,
     but they actually manage attribute access in the instances of the class.

"""


class LineItem:
    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight  # <1>
        self.price = price

    def subtotal(self):
        return self.weight * self.price

    @property  # <2>
    def weight(self):  # <3>
        return self.__weight  # <4>

    @weight.setter  # <5>
    def weight(self, value):
        if value > 0:
            self.__weight = value  # <6>
        else:
            raise ValueError("value must be > 0")  # <7>


item = LineItem(description="test", weight=30, price=1000)
print(dir(LineItem))
print(dir(item))

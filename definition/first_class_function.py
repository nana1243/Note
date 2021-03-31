"""
# https://en.wikipedia.org/wiki/First-class_function
** 파이썬의 모든것은 객체이며 파이썬은 일급 객체 언어이다. **
First-class function :
    This means the language supports
    1) passing functions as arguments to other functions,
    2) returning them as the values from other functions,
    3) and assigning them to variables or storing them in data structures.

    즉, 일급객체란 3가지를 충족하는 함수이다.
    1. 인자로 함수를 건네받거나
    2. 리턴값으로 사용될 수 있거나
    3. 변수나 데이터 구조 안에 담을 수 있다
"""


# 객체 할당(assigning them to variables)


def hello(a: int):
    for _ in range(a):
        print("hello word!")


greet = hello
greet(3)


# passing functions as arguments to other functions
def add_two(a, b):
    return a + b


def calculate(func, arg1, arg2):
    print("result : ", func(arg1, arg2))


calculate(add_two, 1, 2)


# returning them as the values from other functions


def document_it(func):
    def new_function(*args, **kwargs):
        print("Running function:", func.__name__)
        print("Positional arguments:", args)
        print("Keyword arguments:", kwargs)
        result = func(*args, **kwargs)
        print("Result:", result)
        return result

    return new_function


def add_ints(a, b):
    return a + b


closure_add_ints = document_it(add_ints)

"""
https://ko.wikipedia.org/wiki/%EC%BD%9C%EB%B0%B1

** callback (or call-after function) 정의**
- 다른 코드의 인수로서 넘겨주는 실행 가능한 코드를 의미
-- In computer programming, a callback,
    also known as a “call-after[1]” function,
    is any executable code that is passed as an argument to other code,
     which is expected to call back (execute) the argument at a given time.
(쉽게 말하자면, 함수인데 다른 함수에서 input으로 받게 되면 그게 콜백 함수)

check) first-class function vs 콜백함수 뭔차이지?
"""


def get_square(val):
    """ the callback """
    return val ** 2


def caller(func, val):
    return func(val)


caller(get_square, 5)

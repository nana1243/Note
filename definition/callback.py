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
- first_class function 의 조건중 콜백 조건도 있어야 한다가 답이 아닐까함
-- first_class는 3가지 조건을 만족하는 객체(생략)이고 그중 하나의 조건이 콜백의 의미와 동일하기 떄문에
-- 그리고 콜백은 위 조건을 만족시키는 실행가능한 `code` 이며, first-class function  객체 라는 차이

"""


def get_square(val):
    """ the callback """
    return val ** 2


def caller(func, val):
    return func(val)


caller(get_square, 5)

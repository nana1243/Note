"""
#PR_501(SongForm 조회 오류 수정: MongoDB에서 유효한 Configuration만 조회)
cf. 조건문 대신 None 콜백 사용
https://stackoverflow.com/questions/3914667/false-or-none-vs-none-or-false

False or None vs. None or False
- the expression x or y evaluates
    to x if x is true
    or y if x is false
cf. `false` values include False, None, 0 and []

"""

test1 = None or "test"
print(test1)
test2 = None or False
test3 = False or None
print(test2)
print(test3)

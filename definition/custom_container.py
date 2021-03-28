"""
1. container?
- 컨테이너란, __contain__ 메서드가 구현된 객체를 의미
    - 무언가를 담고 있는 객체를 의미한다.
    - 파이썬 내장 컨테이너 타입으로는 리스트, 튜플, 세트 딕셔너리 등이 있다.
"""

# customer_container_ex_1


class CustomList(list):
    def __init__(self, initialize):
        super().__init__(initialize)

    def summary(self):
        rtn = {}
        for item in self:
            rtn.setdefault(item, 0)
            rtn[item] += 1
        return rtn


# list의 표준기능을 전부 구현하면서, 중첩되는 아이템의 갯수를 카운팅하는 커스텀 기능을 가진 커스텀 컨테이너 예시이다.
clist = CustomList(["a", "b", "c", "d", "a", "b"])
summary = clist.summary()

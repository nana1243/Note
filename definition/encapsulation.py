"""
1. 캡슐화
- 메소드와 내부의 속성을 하나의 단위로 묶어서 클래스를 만드는 것을 `캡술화` 라고 한다
    - 클래스를 정의할때 내부의 속성과 메서들를 묶어서 하나의 단위로 처리할 수 있다.


이 클래스 내부의 네임스페이스를 조회하면 name 속성이 property 인스턴스라는 것과,
클래스 내부에 정의된 메서드들이 name이라는 property 인스턴스 내부에 들어가 있는 것을 알 수 있다.
"""


class PropertyClass:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

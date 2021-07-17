class C:
    x = []

    def add(self, element):
        self.x.append(element)


o1 = C()
o2 = C()
o1.add(1)
o2.add(2)
assert o1.x == [1, 2]
assert o1.x is o2.x

# class 변수이기 때문에 서로다른
# 인스턴스(o1,o2)가 해당 x값을 공유한다


class C:
    x = [3]

    def add(self, element):
        self.x.append(element)


o1 = C()
o2 = C()
o1.add(1)
o2.add(2)
assert o1.x == [3, 1, 2]
assert o1.x is o2.x

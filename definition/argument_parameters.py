# ref) https://stackoverflow.com/questions/1788923/parameter-vs-argument


# argument vs params
# Parameter 는 함수 혹은 메서드 정의에서 나열되는 변수 명.
# 반면 Argument는 함수 혹은 메서드를 호출할 때, 전달 혹은 입력되는 실제 값.


def check(str1: str, str2: str):
    print(str1)
    print(str2)


check("test1", "test2")

# params : str1, str2
# arguments : test1, test2

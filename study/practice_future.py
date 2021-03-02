import concurrent.futures

"""
submit : 
 fn 이 fn(*args **kwargs) 처럼 실행되도록 예약하고, 
 콜러블 객체의 실행을 나타내는 Future 객체를 반환합니다.

Future:
Future 클래스는 콜러블 객체의 비동기 실행을 캡슐화합니다. Future 인스턴스는 Executor.submit() 에 의해 생성됩니다.
"""

with concurrent.futures.ThreadPoolExecutor() as executor:
    # https://docs.python.org/ko/3/library/concurrent.futures.html
    future_dict = dict()

    for i in range(10):
        future = executor.submit(lambda x: x * 2, i)
        future_dict[future] = i

    print(future_dict.values())

    for future in concurrent.futures.as_completed(future_dict):
        print(future.result(), future_dict[future])


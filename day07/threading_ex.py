# threading 모듈 - 프로세스의 작동, 작업 단위를 말함.
import threading


def repeat():
    print("3초 간격으로 실행")
    timer = threading.Timer(3, repeat) # 주의! repeat 괄호 생략
    timer.start()


repeat()

# repeat() 콜백함수 - 함수의 매개변수로 함수를 사용
# 재귀함수 - 자신을 호출하는 함수와 비슷함
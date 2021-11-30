# SuperSonicAirplane 클래스 정의

from day09.class_lib.airplane import Airplane


class SuperSonicAirplane(Airplane):
    NORMAL = 1  # 클래스 상수
    SUPERSONIC = 2

    def __init__(self):
        self.fly_mode = SuperSonicAirplane.NORMAL  # 멤버 - 비행 모드

    def fly(self):
        if self.fly_mode == SuperSonicAirplane.SUPERSONIC:
            print("비행기가 초음속으로 비행합니다.")
        else:
            super().fly()




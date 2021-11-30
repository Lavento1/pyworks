# Customer 클래스

class Customer:
    def __init__(self, cid, name):
        self.cid = cid          # 고객 아이디
        self.name = name        # 고객 이름
        self.cgrade = "SILVER"  # 고객 등급
        self.bonus_point = 0    # 보너스 포인트
        self.bonus_ratio = 0.01 # 보너스 적립율 1%

    def get_name(self):
        return self.name

    def calc_price(self, price):
        self.bonus_point += int(price) * self.bonus_ratio   # 포인트 점수로 계산
        return price

    def __str__(self):
        return "%s님의 등급은 %s이고, 보너스 포인트는 %d점입니다." % (self.name, self.cgrade, self.bonus_point)


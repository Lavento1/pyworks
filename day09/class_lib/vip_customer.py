# VIPCustomer 클래스 정의
from day09.class_lib.customer import Customer


class VIPCustomer(Customer):
    def __init__(self, cid, name, agent):
        super().__init__(cid, name)     # 부모 멤버 상속
        self.agent = agent              # 전문 상담원 멤버
        self.cgrade = "VIP"
        self.sale_ratio = 0.2
        self.bonus_ratio = 0.05

    def calc_price(self, price):
        price -= int(price * self.sale_ratio)
        self.bonus_point += int(price) * self.bonus_ratio
        return price

    def __str__(self):
        return super().__str__() + "\n전문 상담원 ID는 %s입니다." % self.agent

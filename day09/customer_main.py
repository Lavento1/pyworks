from day09.class_lib.customer import Customer
from day09.class_lib.gold_customer import GoldCustomer
from day09.class_lib.vip_customer import VIPCustomer

c = Customer(101, "놀부")
g = GoldCustomer(201, "흥부")
v = VIPCustomer(301, "심청", 1004)

cost_c = c.calc_price(10000)
cost_g = g.calc_price(10000)
cost_v = v.calc_price(10000)

print(c.get_name() + "님의 지불 비용은 " + str(cost_c) + "원 입니다.")
print(g.get_name() + "님의 지불 비용은 " + str(cost_g) + "원 입니다.")
print(v.get_name() + "님의 지불 비용은 " + str(cost_v) + "원 입니다.")

print(c)
print(g)
print(v)

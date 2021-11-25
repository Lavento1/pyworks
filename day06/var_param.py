# 가변 매개변수
# 매개변수 앞에 *를 붙임
def calc_avg(*number):
    sum_v = 0
    for i in number:
        sum_v += i
    avg = sum_v / len(number)
    return avg


avg1 = calc_avg(1, 2)
avg2 = calc_avg(1, 2, 3)
print(avg1)
print(avg2)
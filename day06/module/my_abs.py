# 절대값 함수 구현하기
import math


def myabs(x):
    if x < 0:
        return -x
    else:
        return x


def myabs2(x):
    y = x * x
    return int(math.sqrt(y))


print(myabs(-3))
print(myabs2(-3))
print(abs(-3))

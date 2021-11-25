# 지역변수와 전역변수


def one_up():
    global x
    x += 1
    return x


x = 1  # 전역변수
print(one_up())
print(one_up())

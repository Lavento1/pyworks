# 1 ~ 100 까지의 수 중에서 배수 출력

def times(x):
    # 3의 배수
    global count
    count = 0
    for i in range(1, 101):
        if i % x == 0:
            count += 1
            print(i, end=' ')


times(3)
print("\n3의 배수의 개수 : %d개" % count)

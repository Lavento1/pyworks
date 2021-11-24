# 구구단 함수 정의

def print_gugu(dan):
    for i in range(1, 10):
        print("%d x %d = %d" % (dan, i, (dan * i)))


print_gugu(6)

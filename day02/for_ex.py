# 반복문 - for
# 1부터 5까지 출력

for i in (1, 2, 3, 4, 5):
    print(i, end = ' ')
print()

for i in range(1, 6, 1): #range(초기값, 종료값 - 1, 증감값 - 1씩 증가할경우 생략 가능)
    print(i, end = ' ')
print()


# 1부터 10까지의 홀수 출력
for i in range(1, 11):
    if i % 2 == 1 :
        print(i, end = ' ')

# 1부터 10까지의 합계 출력 :
sum_v = 0

for i in range(1, 11) :
    sum_v += i
    print(i, end = ' ')
    
print()
print("sum =", sum_v)

# 2차원 리스트

a = [
    [10, 20],
    [30, 40],
    [50, 60],
    [70, 80]
]

print("리스트의 크기(행) : " + str(len(a)))
print("리스트의 크기(열) : " + str(len(a[0])))
print("리스트의 크기(열) : " + str(len(a[1])))
print("리스트의 크기(열) : " + str(len(a[2])))

#출력
for x, y in a:
    print(x, y)

print("*" * 30)

#중첩 for문
for i in range(0, len(a)):
    for j in range(0, len(a[i])):
        print(a[i][j], end=' ')
    print()

# 합계와 평균 계산하기
sum_v = 0
avg = 0.0
count = 0

for i in range(0, len(a)):
    for j in range(0, len(a[i])):
        sum_v += a[i][j]
        count += 1

# avg = sum_v / count
avg = sum_v / (len(a) * len(a[0]))

print("합계 : {}점". format(sum_v))
print("평균 : {}점". format(avg))
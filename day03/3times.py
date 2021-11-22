# 3의 배수 (1 ~ 20)

count = 0
sum = 0
avg = 0

for i in range(1, 21):
    if i % 3 == 0:
        print(i, end=' ')
        count += 1
        sum += i

avg = sum / count

print()
print("3의 배수의 개수 :", count)
print("3의 배수의 합 :", sum)
print("3의 배수의 평균 :", avg)
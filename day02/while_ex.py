# while 반복문

i = 0
sum_v = 0
while i < 10:
    i += 1
    sum_v += i
    print(i)

print("i의 값 ", i)
print("sum의 값 ", sum_v)

i = 0
while(i < 10):
    i+= 1
    if i % 2 == 0:
        print(i, end = ' ')

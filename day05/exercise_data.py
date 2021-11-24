# 연습문제 112p

# 1

kor = 80
eng = 75
math = 55
total = kor + eng + math
avg = total / 3

print(avg)

# 2

num = 13

if num % 2 == 1:
    print(str(num) + "는 홀수입니다.")
else:
    print(str(num) + "는 짝수입니다.")

# 3

pin = "881120-1068234"
yyyymmdd = pin[:6]
num = pin[7:]
print(yyyymmdd)
print(num)

# 4

pin2 = "881120-1068234"
print(pin2[7])

# 5

a = "a:b:c:d"
b = a.replace(':', '#')
print(b)

# 6
a = [1, 3, 5, 4, 2]
a.sort()
print(a)
a.sort(reverse=True)
print(a)

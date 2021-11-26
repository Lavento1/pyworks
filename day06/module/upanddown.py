# 숫자 추측 게임
import random

com = random.randint(1, 100)
min_v = 1
max_v = 100

for i in range(10):
    try:
        guess = int(input("%d ~ %d 사이의 수를 맞춰보세요!(주어진 기회 - %d회) : " % (min_v, max_v, (10-i))))
        if guess == com:
            print("정답입니다!")
            break
        elif guess > com:
            max_v = guess
            print("너무 큼!")
        else:
            min_v = guess
            print("너무 작음!")
    except:
        print("숫자가 아닙니다. 다시 입력해 주세요.")

print("정답은 %d였습니다!" % com)
print("점수 : %d점" % ((10 - i) * 10))

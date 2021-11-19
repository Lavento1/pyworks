# while ~ break문

'''
i = 0
while True:
    i += 1
    if i > 10:
        break
    print(i)
'''


# 키가 'y' -> 반복, 'n' -> 반복 중단, 그 이외 키는 '정상 입력이 아님'

while True:
    key = input("반복을 계속하시겠습니까?(y/n) : ")

    #조건 처리
    if key == 'y':
        print("반복")
    elif key == 'n':
        print("중단")
        break
    else:
        print("정상 입력이 아닙니다")

# 로또 복권 생성기
# 1 ~ 45 중에 6개의 번호 추첨
import random

lotto = []  # 빈 리스트 준비
# 로또 복권 번호 1개 추첨

'''
for i in range(0, 6):  # 0부터 5까지 6개의 숫자 추첨
    num = random.randint(1, 45)
    # print(num)
    if num not in lotto:  # 기존 로또 리스트에 없는 번호를 리스트에 추가(중복 방지)
        lotto.append(num)
    
print(lotto)
'''

while len(lotto) < 6:   # 0 ~ 5 => 6개
    num = random.randint(1, 45)
    if num not in lotto:
        lotto.append(num)

print(lotto)

# random() - 무작위수(난수) 추출
import random
import math

# 0.0 <= x < 1.0
print(random.random())

# 주사위
dice = math.floor(random.random() * 6 + 1)
print(dice)

# randint(처음, 끝) : 처음과 끝 사이의 난수
dice2 = random.randint(1, 6)
print(dice2)

# 리스트에서 난수 추출하기
lis = ["강아지", "고양이", "햄스터", "소"]
print(random.choice(lis))

# 리스트의 항목을 무작위로 섞기
random.shuffle(lis)
print(lis)


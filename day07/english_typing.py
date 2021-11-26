# 영어 타자 게임
import random
import time

word = ['sky', 'earth', 'moon', 'flower', 'tree',
        'strawberry', 'grape', 'garlic', 'onion', 'potato']

# rw = random.choice(word)
# print(rw)

n = 1  # 문제 번호

input("[타자게임] 준비되면 엔터!")

start = time.time()

while n < 11:
    print('-문제', n)
    question = random.choice(word)  # 문제 단어 선정
    print(question)
    answer = input()  # 답을 입력
    if answer == question:
        n += 1
        word.remove(question)
        print("통과!")
    else:
        print("오타!")

end = time.time()

print("게임 소요 시간 : %.2f" % (end - start))
# 점수의 합계와 평균, 최고 점수, 최저 점수

score = [70, 80, 90, 20, 40]
count = len(score)
sum_v = 0
avg = 0
maxScore = score[0]
minScore = score[0]

print(sum(score))
print(0)
for i in score:
    sum_v += i
    if maxScore < i:
        maxScore = i
    if minScore > i:
        minScore = i

avg = sum_v/count

print("개수 :", count)
print("합계 :", sum_v)
print("평균 :", avg)
print("최고 점수 :", maxScore)
print("최고 점수 :", max(score))
print("최저 점수 :", minScore)
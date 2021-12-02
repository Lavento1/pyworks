# 파일을 읽어서 성적의 총점과 평균 계산하기
with open('score_list.txt', 'r') as f:
    score = []
    for i in range(3):
        score.append(f.readline().split())
    # print(score)

# 총점 및 평균 계산
for i in range(3):
    score[i][1] = int(score[i][1])
    score[i][2] = int(score[i][2])
    score[i].append(score[i][1] + score[i][2])
    score[i].append(score[i][3] / 2)


# 성적표 출력
print("*" * 8 + " 성적표 " + "*" * 8)
print("=" * 23)
print("이름  국어  수학  총점  평균")
print("=" * 23)
for i in range(3):
    print("{}  {}   {}  {}  {}".format(score[i][0], score[i][1], score[i][2], score[i][3], score[i][4]))
print()

print("*" * 6 + " 과목별 평균 " + "*" * 6)
sum_subj = [0, 0]
for i in range(3):
    sum_subj[0] += score[i][1]
    sum_subj[1] += score[i][2]

print("국어 : %.2f, 수학 : %.2f" % (sum_subj[0]/3, sum_subj[1]/3))

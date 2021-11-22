# 리스트의 생성 및 관리

number = [10, 20, 30, 40]

# 요소 추가
number.append(50)
print(number)

#요소 수정
number[1] = 60
print(number)

# 요소 삭제
# del number[2] #명령어 삭제
number.pop(2) #함수 삭제
print(number)

# 요소의 개수
print(len(number))

# for ~ in 문
for i in number:
    print(i)

print()

n = len(number)

for i in range(0, n):
    print(number[i], end=' ')
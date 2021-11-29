# Student 클래스를 외부에서 사용하기
from classlib.student import Student

'''
s = Student("김하나", 3)
print(s)
'''

s = [
    Student("김하나", 3),
    Student("이두울", 1),
    Student("박세엣", 2)
]

print(s[1])
print(s[2])

print("*" * 15 + " 학생 명단 " + "*" * 15)
for i in s:
    print(i)
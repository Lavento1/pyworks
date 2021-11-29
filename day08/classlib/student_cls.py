# student 클래스 만들기
# 클래스는 self 키워드를 사용
# def init() - 생성자 함수 사용

class Student:
    def __init__(self): # initial - 생성자
        self.name = "콩쥐"
        self.grade = 1
        print("생성자 함수입니다.")

    def learn(self):
        print("수업을 듣는다.")


s = Student()   # 매개변수가 없는 Student 클래스 객체 s 생성
print("이름 : " + s.name)
print("학년 : " + str(s.grade))
s.learn()

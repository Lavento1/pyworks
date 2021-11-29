# 생성자 - 매개변수가 있는 생성자

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __str__(self):
        return "이름 : %s, 학년 : %s" % (self.name, self.grade)


if __name__ == "__main__":  # name 변수의 이름이 main이라면 실행
    s1 = Student("콩쥐", 1)
    print(s1)
    s2 = Student("팥쥐", 2)
    print(s2)

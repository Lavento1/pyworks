# Person 클래스 만들기
# 접근 제한 방법 - 변수이름 앞에 _ 를 1개, 2개를 붙임
# 속성이 private으로 바뀜
# 접근 방법 - get + 변수이름(), set + 변수이름()으로 만들어 속성을 public으로 바꿈

class Person:
    def __init__(self):
        self.__name = ""  # 멤버 변수 초기화 및 접근 제한
        self.__age = 0

    def setname(self, name):
        self.__name = name

    def setage(self, age):
        self.__age = age

    def getname(self):
        return self.__name

    def getage(self):
        return self.__age


p1 = Person()
p1.setname("김하늘")
print(p1.getname())
p1.setage(25)
print(p1.getage())

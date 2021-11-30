# Employee 클래스 정의
from day09.class_lib.person import Person


class Employee(Person):  # Person 클래스 상속
    # pass                          # 부모 클래스를 그대로 상속 받을 때
    def __init__(self, name, age, employeeID):
        super().__init__(name, age)            # 부모 멤버를 super() 함수로 명시
        self.employeeID = employeeID

    def __str__(self):                         # 부모 __str__() 함수 상속 - 재정의(override)
        return super().__str__() + ", 사번 : " + str(self.employeeID)


e = Employee("이강", 25, 101)
print(e)
print("이름 : " + e.name)
print("나이 : " + str(e.age))
print("사번 : " + str(e.employeeID))

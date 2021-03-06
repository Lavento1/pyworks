# employee.py 모듈 만들기
# Employee 클래스 생성

class Employee:
    serial_num = 1000   # 기준값(클래스 변수), 데이터 영역 메모리

    def __init__(self):
        Employee.serial_num += 1
        self._id = Employee.serial_num   # 사원 id에 번호 저장

    def getid(self):
        return self._id

    def setname(self, name):
        self.name = name

    def getname(self):
        return self.name


e1 = Employee()         # 스택 메모리
e1.setname("김하늘")     # 힙 메모리
print("사번 : " + str(e1.getid()) + ", 이름 : " + e1.getname())

e2 = Employee()
e2.setname("이상혁")
print("사번 : " + str(e2.getid()) + ", 이름 : " + e2.getname())

e3 = Employee()
e3.setname("이아주")
print("사번 : " + str(e3.getid()) + ", 이름 : " + e3.getname())


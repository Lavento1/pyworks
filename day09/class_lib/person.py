# person 클래스

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "이름 : {}, 나이 : {}".format(self.name, self.age)


if __name__=="__main__":
    p = Person("김하늘", 21)
    print(p)

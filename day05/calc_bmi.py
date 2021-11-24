name = input("이름을 입력하세요 : ")
height = int(input("키(cm)를 입력하세요 : "))
height /= 100
weight = int(input("몸무게(kg)을 입력하세요 : "))

bmi = weight / (height * height)

# print(name + "님의 bmi는 " + str(bmi) + " 입니다.")
print("{}님의 bmi는 {:.2f} 입니다.".format(name, bmi))
print("%s님의 bmi는 %.2f 입니다." % (name, bmi))

if bmi < 20:
    print("저체중입니다.")
elif bmi < 25:
    print("정상입니다.")
elif bmi < 30:
    print("과체중입니다.")
else:
    print("비만입니다.")


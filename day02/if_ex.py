# if 조건문
age = 6

if age < 9:
    print("학교에 갈 나이가 아닙니다.") # 들여쓰기 - 인덴트(4칸)을 하는게 코드블록 대체

print("나이는 " + str(age) + "세입니다.")

# if ~ else 구문

speed = int(input("속도 입력 : "))

if speed > 50:
    print("속도 위반")
else:
    print("안전 속도 준수!!")

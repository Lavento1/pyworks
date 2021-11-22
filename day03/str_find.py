# find() 함수
s = "Hello, welcome to my website!"
print(s.find('H'))
print(s.find('l'))
print(s.find('k'))

s = s.find("welcome") # 단어로 검색 : 첫 문자 위치
print(s)

# strip() 함수 - 공백 제거
str1 = "   hi, soo!  "
str2 = "yes"

print(str1.lstrip() + str2)
print(str1.strip() + str2)

txt = "    banana    "
x = txt.strip()
print("Of all fruits", x, "is my favorite")

# isnumeric() - 숫자인지 검사하는 함수
text = "123".isnumeric()
print(text)

text2 = "123abc".isnumeric()
print(text2)
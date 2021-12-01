# 파일 읽기

f = open("c:/web_dev/pyfile/number.txt", 'r')     # 파일 읽기 모드 - 'r' 사용

text = f.read()     # 파일 내용 전체 읽어옴
print(text)         # 콘솔에 출력

f.close()

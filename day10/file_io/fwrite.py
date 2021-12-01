# 파일 쓰기

f = open("c:/web_dev/pyfile/file.txt", 'w')      # 파일 열기, 쓰기 모드

f.write("하늘이 파랗다.\n")
f.write("Thank You!!\n")
f.write("社員\n")
# f.write(45)
f.write('45\n')

f.close()       # 파일 닫기


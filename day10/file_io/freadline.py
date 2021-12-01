# 파일 읽기

f = open("c:/web_dev/pyfile/season.txt", 'r')     # 파일 읽기 모드 - 'r' 사용

# season = f.readline()
# print(season)
seasons = f.readlines()
print(seasons)
print(seasons[0])

# 전체 읽기
for season in seasons:
    print(season.strip())

f.close()

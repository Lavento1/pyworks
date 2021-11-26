# 날짜로 요일 알아내기
import datetime


def get_weekday(yyyy, mm, dd):
    days = ["월", "화", "수", "목", "금", "토", "일"]
    x = datetime.date(yyyy, mm, dd).weekday() # 요일결과는 숫자로 출력(월-0부터 시작)
    return days[x]


yyyy = 2021
mm = 11
dd = 26

weekday = get_weekday(yyyy, mm, dd)

print("%s년 %s월 %s일 %s요일" % (yyyy, mm, dd, weekday))

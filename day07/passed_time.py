# 시작일 ~ 종료일 기간 계산
import datetime

print("◎ 지금까지 몇 일? ◎")
start_day = datetime.date(2021, 10, 26)
# print(start_day)

today = datetime.date.today()
# print(today)

passed_time = today - start_day

print("개강이후 %s일이 지났습니다." % passed_time.days)

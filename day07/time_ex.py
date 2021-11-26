import math
import time

print(time.time()) # 1970. 1.1 자정이후 초로 환산
days = round(time.time() / (24*60*60)) # 초를 일로 환산
year = round(time.time() / (365*24*60*60)) # 초를 년으로 환산

print("%s일" % days)
print("{}년".format(year))

# time.sleep(x) x만큼 시간 간격을 둠
# for 문 수행 시간 측정
start = time.time()

for i in range(10):
    print(1)
    time.sleep(1) # 파이썬 1 - 1초, 다른 언어 1000 - 1초
    
end = time.time()
et = math.floor(end-start)
print("for문 수행 시간 : {}초".format(et))

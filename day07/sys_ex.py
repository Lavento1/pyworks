# sys 모듈
# 명령 행(cmd-명령프롬프트)에서 인수 전달하기
import sys

args = sys.argv[1:] # 리스트 1번부터 끝까지 슬라이싱
print(args)

for i in args:
    print(i)
# 주요 내장 함수

# all - 반복 자료안에 모두 0일때만 True, 나머지는 False
print(all([1, 2, 3]))
print(all([1, 2, 0]))

# any - 반복 자료안에 모두 0일때만 False, 나머지는 True
print(any([1, 0, 3]))

# eval - 문자열 표현 - > 숫자로 변환
print(eval("1+2"))

# list - 자료를 리스트로 변환
print(list('python'))

# 반올림
print(round(4.7))
print(round(4.52))
print(round(4.5))
print(round(4.32))

# 합계
print(sum([1, 2, 3, 4]))

# 최소 값
print(min([1, 2, 3, 4]))

# 거듭제곱
print(pow(2, 4))

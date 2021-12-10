import requests     # url에 접속 및 정보를 가져오는 모듈(pip install requests - cmd)

# 로봇 배제 표준 내역 가져오기

url = "https://www.naver.com/robots.txt"

response = requests.get(url)    # 응답 객체 생성
print(response)
print(response.text)

response2 = requests.get("http://www.python.org/robots.txt")
print(response2)
print(response2.text)

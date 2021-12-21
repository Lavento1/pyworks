import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/marketindex/"
response = requests.get(url)  # url 응답객체 생성
soup = BeautifulSoup(response.text, 'html.parser')  # html 객체 생성
ul = soup.find('ul', attrs={'class': 'data_lst'})

# 환율 하나만 찾기

li = ul.find('li')
print(li)
exchange = li.select_one('span.blind')
value = li.select_one('span.value')

print(exchange.string.split(' ')[-1], ':', value.string)

# 전체 환율 찾기

# lis = ul.find_all('li')
#
# for li in lis:
#     exchange = li.find('span', attrs={'class': 'blind'})
#     value = li.find('span', attrs={'class': 'value'})
#     print(exchange.string.split(' ')[-1], ':', value.text)  # 공백문자를 구분해서 맨 뒤의 문자열 추출

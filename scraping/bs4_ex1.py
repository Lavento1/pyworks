from bs4 import BeautifulSoup

html_str = """
<html>
    <body>
        <ul class='item'>
            <li>인공지능</li>
            <li>빅데이터</li>
            <li>로봇공학</li>
        </ui>
        <ul class='lang'>
            <li>Python</li>
            <li>Java</li>
            <li>C#</li>
        </ui>
    </body>
</html>
"""

soup = BeautifulSoup(html_str, "html.parser")  # BeautifulSoup의 객체 생성
first_ul = soup.find('ul')     # 처음 나오는 'ul' 태그를 찾음

print(first_ul)
print(first_ul.text)    # 태그를 제외한 문자열 출력

first_li = first_ul.find('li')  # firsst_ul 객체로 li 태그 접근함
print(first_li)

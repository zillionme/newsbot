import requests
from bs4 import BeautifulSoup, BeautifulStoneSoup

url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()
#우리가 가져온 res.text 문서를 lxml (parser= xml(트리구조 갖고있는 마크업 언어)를 해석하는 프로그램)
#lxml parser을 통해서, beautifulsoup 객체로 만든 것.  = 살아있는 html문서 만들기

soup = BeautifulSoup(res.text, "lxml")
# print(soup.title)   #soup 객체 밑에 있는 element에 접근할 수 있음.  title정보 가져오기
# print(soup.title.get_text())  # get_text()로 title에서 글자만 딸 수 있음
# print(soup.a)   #가지고 있는 정보 중  첫번제 element를 가져옴.
# soup객체에서 처음 발견되는 a element를 출력
print(soup.a.attrs) #attribute 속성정보 보는 방법 = attrs
#딕셔너리 형태로 태그의 속성 정보를 얻을 수 있음
#원하는 속성값 (속성명 빼고)을 얻고싶으면
print(soup.a["href"])  #a element의 href 속성값 정보를 출력할 수 있다


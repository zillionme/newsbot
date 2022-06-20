# 제목정보 가지고 오기
import requests
from bs4 import BeautifulSoup, BeautifulStoneSoup

url = "https://comic.naver.com/webtoon/list?titleId=748105"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
# cartoons = soup.find_all("td", attrs={"class":"title"})

# #타이틀과 링크 가지고오기.
# for cartoon in cartoons :
#   title = cartoon.a.get_text()
#   link = "https://comic.naver.com" + cartoon.a["href"]
#   print("제목 : "+  title, "\n바로가기 : " + link)

#평점구하기 (내가만든 버전)
# ratings = soup.find_all("div", attrs={"class":"rating_type"})
# for rating in ratings :
#   rating = rating.strong.get_text()
#   print(rating)

#평점구하기
# cartoons = soup.find_all("div", attrs={"class":"rating_type"})
# for cartoon in cartoons :
#   rate = cartoon.find("strong").get_text()
#   print(rate)

#평균 평점 구하기(내가 만든 버전)
cartoons = soup.find_all("div", attrs={"class":"rating_type"})

result = 0
for cartoon in cartoons :
  rate = cartoon.find("strong").get_text()
  result += float(rate)
  
print("평균점수 :", result/len(cartoons))

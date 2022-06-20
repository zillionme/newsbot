import requests
from bs4 import BeautifulSoup

url = "https://news.naver.com/main/list.naver?mode=LPOD&mid=sec&oid=008&listType=paper"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit"}

res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text, "lxml")

paper1 = soup.find_all("span",attrs={"title":"신문에 게재되었으며 1면의 기사입니다."})
paper2 = soup.find_all("span",attrs={"title":"신문에 게재되었으며 2면의 기사입니다."})
paper3 = soup.find_all("span",attrs={"title":"신문에 게재되었으며 3면의 기사입니다."})
paper4 = soup.find_all("span",attrs={"title":"신문에 게재되었으며 4면의 기사입니다."})

def news(papern) :
  for article in papern :
      article = article.find_previous_sibling("a")
      print(article.get_text())
      print(article["href"])

print("<1면>")
news(paper1)
print("<2면>")
news(paper2)
print("<3면>")
news(paper3)
print("<4면>")
news(paper4)


# for article in paper1 :
#   article = article.find_previous_sibling("a")
#   print(article.get_text())
#   print(article["href"])

from turtle import title
import requests
from bs4 import BeautifulSoup
import telegram

token=""
bot = telegram.Bot(token = token)
chat_id = 5

#스크래핑
url = "https://news.naver.com/main/list.naver?mode=LPOD&mid=sec&oid=008&listType=paper"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"}

res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text, "lxml")

#1면
paper1 = soup.find_all("span",attrs={"title":"신문에 게재되었으며 1면의 기사입니다."})
def news(papern) :
  papers = []
  for article in papern :
      article = article.find_previous_sibling("a")   #1면 span의 형제인 a 요소 가져오기
      paper = (article.get_text() ,article["href"])
      papers.append(paper)   
  return "\n".join(papers)
print(news(paper1))

# for n in paper1:
  # bot.sendMessage(chat_id=chat_id, text=n)                  # 튜플형식은 텍스트로 보내지지 않음. 




from turtle import title
import requests
from bs4 import BeautifulSoup
import telegram

token=""
bot = telegram.Bot(token = token)
chat_id = 5

#스크래핑
url = "https://news.naver.com/main/list.naver?mode=LPOD&mid=sec&oid=008&listType=paper"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit"}

res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text, "lxml")

paper1 = soup.find_all("span",attrs={"title":"신문에 게재되었으며 1면의 기사입니다."})
# paper2 = soup.find_all("span",attrs={"title":"신문에 게재되었으며 2면의 기사입니다."})
# paper3 = soup.find_all("span",attrs={"title":"신문에 게재되었으며 3면의 기사입니다."})
# paper4 = soup.find_all("span",attrs={"title":"신문에 게재되었으며 4면의 기사입니다."})

#제목과 링크 추출함수
def news(papern) :
  papers = []
  for article in papern :
      article = article.find_previous_sibling("a")   #1면 span의 형제인 a 요소 가져오기
      # title = article.get_text()
      # link = article["href"]
      paper = (article.get_text() ,article["href"])
      papers.append(paper)   
  return papers


#함수 값 여러개 반환 시 ,(콤마) 사용.  
#반환값들을 튜플로 반환하는 경우 : new(paper1) >>>(title,link)
#반환값들은 여러개의 변수에 저장하는 경우 : title,link = news(papern)  

#1,2,3,4면 추출
print( news(paper1))
# news(paper2)
# news(paper3)
# news(paper4)

#텔레그램 메시지 전송 함수

# bot.sendMessage(chat_id=chat_id, text=news(paper1))
for n in paper1:
  bot.sendMessage(chat_id=chat_id, text=n)





# for article in paper1 :
#   article = article.find_previous_sibling("a")
#   print(article.get_text())
#   print(article["href"])

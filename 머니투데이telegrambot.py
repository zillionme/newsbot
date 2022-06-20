import requests
from bs4 import BeautifulSoup
import telegram

token=""
bot = telegram.Bot(token = token)
chat_id = 1234

#스크래핑
url = "https://news.naver.com/main/list.naver?mode=LPOD&mid=sec&oid=008&listType=paper"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"}

res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text, "lxml")

#1면
paper1 = soup.find_all("span",attrs={"title":"신문에 게재되었으며 1면의 기사입니다."})
def url_title_extract(papern) :
  titles = []
  for idx, article in enumerate(papern) :
      article = article.find_previous_sibling("a")   #1면 span의 형제인 a 요소 가져오기
      title = article.get_text()
      titles.append('{}.'.format(idx +1) + title)
  
  links =[]
  for article in papern:
    article = article.find_previous_sibling("a")
    link = article["href"]
    links.append(link)
  
  result = []
  for i,j in zip(titles, links):
    result.append(i+j)
  return "\n".join(result)


news1 = url_title_extract(paper1)



paper2 = soup.find_all("span",attrs={"title":"신문에 게재되었으며 2면의 기사입니다."})
paper3 = soup.find_all("span",attrs={"title":"신문에 게재되었으며 3면의 기사입니다."})
paper4 = soup.find_all("span",attrs={"title":"신문에 게재되었으며 4면의 기사입니다."})

news2 = url_title_extract(paper2)
news3 = url_title_extract(paper3)
news4 = url_title_extract(paper4)


# print(news1)
bot.sendMessage(chat_id=chat_id, text="<<<<<<<<머니투데이>>>>>>>>>>\n1면\n"+ news1 +"\n\n2면\n"+news2+"\n\n3면\n"+news3+"\n\n4면\n"+news4)
# for n in news1 :
#   bot.sendMessage(chat_id=chat_id,text=n)



  


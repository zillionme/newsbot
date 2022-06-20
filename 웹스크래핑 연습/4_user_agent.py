# 웹사이트에서는 접속자의 정보를 알 수 있음. 헤더정보
# 예) 내가 pc에서 네이버 접속과 스마트폰에서 네이버 접속할 때 다른 페이지

# 브라우저가 웹사이트에 접속할 때 주는 헤더 정보에 따라서, 사이트가 각기 다른 페이지를 제공

# 근데 웹 스크래핑 크롤링 하기 위해 컴퓨터가 접속하는 경우, 사이트 입장에서 부하/정보 뺏길수 있기 때문에 차단함.


import requests
url = "https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=105"
#딕셔너리 형태.
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36"}
res = requests.get(url, headers = headers)
res.raise_for_status()

with open("news.html", "w", encoding= "utf-8") as f :
  f.write(res.text)

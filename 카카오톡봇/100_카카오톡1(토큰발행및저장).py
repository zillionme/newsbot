# https://kauth.kakao.com/oauth/authorize?client_id=cba9bcb29c316d12f80e1d8427f0d161&redirect_uri=REDIRECT로 설정했던값&response_type=code
#rest api값과 redirect url 값 넣을 때마다 code값 바뀜

#카카오톡에 메시지 보낼 수 있는 토큰 받고, 토큰 이용해 메시지 보내기
import requests
import json

url = 'https://kauth.kakao.com/oauth/token'
client_id = "156" #rest api값
redirect_url = 'https://example.com/oauth'
code = "XxA"

data = {
  "grant_type" : "authorization_code",
  "client_id": client_id,
  "redirect_url": redirect_url,
  "code": code,
}

res = requests.post(url, data=data)  #토큰 불러오기
tokens = res.json()   #토큰 json형태로 저장

#발행된 토큰 저장
with open("token.json","w") as kakao: #kakao는 현재 파일에서 쓰는 변수명 
  json.dump(tokens, kakao)  #파이썬의 token 객체를 kakao라는 json파일에 저장하기

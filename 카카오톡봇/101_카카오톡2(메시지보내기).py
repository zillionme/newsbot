import requests
import json

#발행된 토큰 불러오기
with open("token.json", "r") as kakao :
  tokens = json.load(kakao)  
  #load함수 : kakao변수 = json파일에 저장된 데이터를 읽어서 파이썬 객체로 불러오고 싶은 경우.


url =  "https://kapi.kakao.com/v2/api/talk/memo/default/send"

headers={
    "Authorization" : "Bearer " + tokens["access_token"]
}

data = {
  'object_type': 'text', 
  'text': '테스트입니다',
  'link': {
    'web_url': 'https://developers.kakao.com',
    'mobile_web_url': 'https://developers.kakao.com',
    },
  'button_title': '키워드'
  }

data = {'template_object': json.dumps(data)}
res = requests.post(url, headers=headers, data=data)
res.status_code

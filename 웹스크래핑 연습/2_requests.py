# response라는 res에 링크에서 가져온 내용을 담는 것
import requests
res = requests.get("https://news.naver.com")
# 정보 잘 받아왔는지, 페이지 접속 권한은 없는지 서버문제 등 확인하기 위해, 응답코드
# 응답코드가 200이면 정상 동작한 것  / 403이면 접근 권한이 없음 = 이 페이지에서 html문서를 올바로 가져올 수 없음 = 웹스크래핑 할 수 없음


print("응답코드 : ", res.status_code)  
if res.status_code == requests.codes.ok :
  print("정상 작동하였습니다")
else :
  print("문제가 생겼습니다. [에러코드 : ", res.status_code, " ]")


#같음. 올바르게 가져옴 문제가 없고, 오류가 생긴경우 에러를 내뱉고, 그자리에서 프로그램이 끝남
res.raise_for_status()
print("웹스크래핑을 진행합니다")
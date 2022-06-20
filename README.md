# newsbot
paper news scrapping bot (telegram) 

 ## 실행 모습
매일 오전 9시 자동으로 뉴스 지면 1~4면 스크래핑해서 보내준 모습

![Screen_Recording_20220621-030543_Telegram_1](https://user-images.githubusercontent.com/100172683/174672106-f62ecd0d-463d-4c06-8d14-1fbefcb62776.gif)


##  프로젝트 목표
* 매일 오전 9시에 지면 뉴스 스크래핑하여, 자동으로 채팅방에 전송됨  


 ##  데이터 파이프 라인
* 9AM : Trriger(Amazon EventBridge) -> LAMBDA FUNCTION 호출 -> 뉴스 스크래핑 및 text 파일에 저장->  telegrambot API -> USER


![뉴스봇 lambda](https://user-images.githubusercontent.com/100172683/174672876-229ddd7b-1277-4186-8f05-5f7e4cdd9f30.jpg)

*Amazon EventBridge는 다양한 소스의 데이터와 애플리케이션을 연결하는 데 사용할 수 있는 서버리스 이벤트 버스 서비스

 
## 사용 라이브러리
bs4 라이브러리/ beautifulsoup 모듈 사용해서 웹 스크래핑
reqeusts 라이브러리 사용해서 데이터 txt파일로 저장

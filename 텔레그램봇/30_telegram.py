import telegram

#토큰 이용해서 봇 가져오기
token=""
bot = telegram.Bot(token = token)

#id 가져오기
for i in bot.getUpdates():
  print(i.message)

# chat_id = 

# bot.sendMessage(chat_id=chat_id, text="안녕, 한글도 전송되니?")
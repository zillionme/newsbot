import requests
res = requests.get("https://www.google.com/")
res.raise_for_status()

# res.text하면 html문서 내용을 가지고옴. len()은 글자개수
print(len(res.text))

with open("mygoogle.html", "w", encoding= "utf-8") as f :
  f.write(res.text)
  
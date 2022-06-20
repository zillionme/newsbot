import requests
from bs4 import BeautifulSoup, BeautifulStoneSoup

url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

# soup.find("a", attrs={"class" : "Nbtn_upload"}) #어떤 a태그 가져올 수 있는지 정할 수 있음.

rank1 = soup.find("li", attrs={ "class": "rank01"})
# # # print(rank1.a.get_text())
# # print(rank1.next_sibling)
# rank2 = rank1.next_sibling.next_sibling
# rank3 = rank2.next_sibling.next_sibling
# print(rank3.a.get_text())

# print(rank1.parent)

# rank2 = rank1.find_next_sibling("li")
# print(rank2.a.get_text())

# rank3 = rank2.find_next_sibling("li")
# print(rank3.a.get_text())

# rank2 = rank3.find_previous_sibling("li")
# print(rank2.get_text())

# rank1.find_next_siblings("li")

webtoon = soup.find("a", text = "한림체육관-시즌1 에필로그")
print(webtoon)
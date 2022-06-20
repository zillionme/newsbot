import re
p = re.compile("ca.e")


# findall : 일치하는 모든 것들을 리스트 형태로
lst = p.findall("good care cafe careless")
print(lst)



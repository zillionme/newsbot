#match는 주어진 문자열의 처음부터 일치하는지
#search는 주어진 문자열 중에 일치하는 게 있는지 확인

import re
p = re.compile("ca.e")

s = p.search("good care")
print(s)


#함수로 만들기
def print_match(m):
  if m: 
    print(m.group())  #일치하는 문자열을 반환 careless면 care만
    print(m.string)   #입력받은 문자열을 그대로 출력 careless면 careless
    #string은 함수가 아니고 변수이기 때문에, 괄호 없이 사용
    print(m.start())  #일치하는 문자열의 시작 index
    print(m.end())  #일치하는 문자열의 끝 index
    print(m.span())  #일치하는 문자열의 시작과 끝 index를 함께 표현
  else : print("매칭되지 않음")

m = p.search("good care") 
print_match(m) 
#regular expression 정규표현식 = 정해진 형태를 의미하는 식
import re
#p = 패턴을 의미
p = re.compile("ca.e")
# .  : 하나의 문자를 의미
# ^ : 문자열의 시작

m = p.match("case")
print(m.group())    
#문자열이 p 변수(ca.e 단어들이 컴파일)와 매치되지 않으면, 에러가 발생함

m = p.match("caffe")
if m : print(m.group())   #m이 참이면
else : print("매칭되지 않음")  

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

m = p.match("care godd")  
print_match(m)
# match 매서드는. 주어진 문자열의 처음부터 일치하는지 확인/ 
#즉, 뒷부분은 달라도 상관없음.
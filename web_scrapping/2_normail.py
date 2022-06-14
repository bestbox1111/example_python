



import re   #정규 표현식 사용.

# cafe 가 키워드라면...
# ca?e 까지만 기억에 난다라면..

p= re.compile("ca.e")   #하나의 문자를 의미
# (ca.e) : 하나의 문자를 의미   ex) care, cafe
# (^de) : 문자열의 시작.    ex)desk,detination
# (se$) : 문자열의 끝   ex)case, base

# m = p.match("case")
# if m:
#     print(m.group())    #a매치되면 출력되며, 매칭 안되면오류
# else:
#     print("매칭되지 않음")
    
    
    
#위 m변수 부분의 구믄을 함수로 적용
def print_match(m): 
    if m:
        print("m.group():", m.group())    #매칭되는 문자열 반환
        print("m.string():", m.string)    #입력 모든 받은 문자열 반환
        print("m.start():", m.start())      # 입력 받은 문자중 첫번째 시작 인덱스
        print("m.end(): ",m.end())   #일치하는 문자열의 끝 인덱스
        print("m.span()", m.span()) #일치 하는 문자열의 시작/ 끝 인덱스
    else:
        print("매칭되지 않음")
    
# m = p.match("case")    #해당 문자열이면 
# print_match(m)


m=p.search("careless") #다음 문자열중에 포함만 되어있으면 됨
print_match(m)



lst=p.findall("good care cafe")   # 일치 하는 문자를 리스트로형태로 출력(care , cafe)
print(lst)


#정규식 사용법

#1. re.compile("문자열")
#2 p=re.compile("문자열")  을 원하는 변수에 저장.
#3. m= p.match("비교할 문자열") p.match("")를 원하는 변수에저장.  #위의26~30라인의 사용법.
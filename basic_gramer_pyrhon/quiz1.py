
#비밀번호를 만들어주는 프로그램을 작성하시오

#규칙1 http://naver.com  사이트는 네이버로 한다.
#규칙2 http:// 부분은 제외 =>naver.com
#규칙3 처음만나는점 . 이후 부분은 제외 ==>naver
#규칙4 남은 글자중 처음 세자리 + 글자객수 + 글자내 'e"갯수 +"!"로 구성
#생성된 비밀번호 nav51!


name ="http://naver.com"    #규칙1 변수 정하고

name_cut=name[7:]       #규칙2 앞부분은 제외 시키고
# name_cut= name.replace["http://"," "]     http://를 빈칸으로 바꾸겠다 ==== 이렇게 해도됌


index=name_cut.index(".")
# name_cut=name_cut[:name_cut.index["."]]      네임컷으로 남은 부분중 네임컷.인덱스"."로 . 부분까지 날려버린 문자를 저장

print(index)    #해당 변수에 해당하는 문자가 몇번째 있는지 출력해줌.

name_cut2=name_cut[:5]          #규칙3   . 이후 부분은 제외 한 문자를 name_cut2에 저장

name_cut3=name_cut2[0:3]        #규칙4중 첫번째 처음 3자리 저장
num =len(name_cut2)             #규칙 4중 두번째 글자 갯수를 변수에 저장
name_cut4=name_cut2.count("e")  #규칙 4중 글자내 e갯수를 저장
last="!"                        #규칙 4중 ! 추가해줌
print(name_cut4)


print(name_cut3+str(num)+str(name_cut4)+last)   #프린트로 모두 더해주며 인트로 계산된 부분을 스트링으로 변환.



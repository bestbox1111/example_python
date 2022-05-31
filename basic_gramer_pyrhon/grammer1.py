

#전체 컨셉 = 슬라이싱


jumin ="810414-1400000"

print("주민번호",jumin)

print("생년월일:", jumin[:6])   #:는 앞에서부터 해서 뒷숫자까지.
print("뒷7자리:", jumin[7:])   #7자리부터 : 끝자리까지
print()
print("뒷7자리 뒤에서부터",jumin[-7:])

print("성별",jumin[7])  #인덱스는 0부터시작해서 8번째자리인 1
print("년정보:",jumin[0:2]) #[x,y]  x부터 y직전까지 가져옴
print("월정보:",jumin[2:4]) #[x,y]  x부터 y직전까지 가져옴
print("일정보:",jumin[4:6]) #[x,y]  x부터 y직전까지 가져옴


#전체 컨셉  문자열 처리 함수




python="Python is Amazing"
print(python)
print(python.upper())   #모든 문자 대문자로
print(python.lower())   #모든 문자 소문자로
print(python[0].isupper())   #해당 변수의0 번째가 대문자냐? 블리언으로 출력됨
print(python[0].islower())   #해당 변수의0 번째가 소문자냐? 블리언으로 출력됨
print(len(python))      # 해당 변수의 총 길이출력해줌.
print(python.replace("Python", "JAVA")) # 해당 함수를 변경해줌 (1번째인자에 월래값, 2째인자엔는 바꿀값)


index=python.index("o")
print(index)    #해당 변수에 해당하는 문자가 몇번째 있는지 출력해줌.

index=python.index("i",index+1)
print(index)   #해당 변수에 해당하는 문자가 몇번째 있는지 출력해주지만, 뒷에 인자로 해당문자 다음 몇번째 뒤부터인지 정해줌..



#파인드와 인덱스의 가장 큰차이는 
#파인드는 해당 문자가 없어도 -1로 리턴해주지만
#인덱스는 해당 문자가 없으면 오류남

find=python.find("Android")
print(find)     #해당 변수에 해당하는 문자가 있으면 블리언을 리턴해줌 있으면 0 없으면 -1

# index=python.index("Android")
# print(index)    #해당 변수에 해당하는  문자가 없으면 오류

print(python.count("n"))



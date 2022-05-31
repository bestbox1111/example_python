

#전체 컨셉은 리스트

subway=["유재석,","조세호","박명수"]
print(subway)

# 조세호가 몇번째에 있는지
print(subway.index("조세호"))        
#인덱스 번호로 0부터 계산해서 출력됨.


#하하나 다음 정류장에서 다음칸에 탐
subway.append("하하")
print(subway)			#기존멤버에 다음차레로 추가되어 나타남.



#정형돈을 유재석/조세호 사이에 넣을때
subway.insert(1,"정형돈")	#인덱스 번호를 먼저 넣고, 그다음 데이터
print(subway)	


subway.pop()	#지하철에 있는 사람 뒤에서 부터꺼냄
print(subway)	

#같은 사람이 몇명 있는지 확인
subway.append("유재석")
print(subway)	

print(subway.count("유재석"))		#서브웨이에 유재석이 몇개있는지 확인해서 숫자로 출력

#정렬도 가능
num_list=[5,7,3,9,2]
num_list.sort()
print(num_list)

#순서 뒤집기
num_list.reverse()
print(num_list)

#리스트 지우기
num_list.clear()
print(num_list)


# 다양한 자료형 함께 사용
num_list =[5,4,3,2,1]
mix =["park",20,True]

#리스트확장
num_list.extend(mix)
print(num_list)
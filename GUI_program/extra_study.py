
#### list 및 mixed 보충 설명 ####
kor=["사과","바나나","오렌지"]
eng=["apple","banaba","orange"]

print(zip(kor, eng))        #이상태면 뭔가 주소를 전달 하는 상태
print(list(zip(kor, eng)))  # 리스트로 묶어줘야함


#반대로 같은 인덱스번호들끼리 묶어주는 함수도잇음.
mixed=[("사과","apple"),("바나나","banaba"),("오렌지","orange")]
print(zip(mixed))   #이상태면 뭔가 주소를 전달 하는 상태
print(list(zip(*mixed)))  # 리스트로 묶어줘야함

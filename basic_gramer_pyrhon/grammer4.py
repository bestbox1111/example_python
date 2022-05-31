


#전체 컨셉은 사전 == dictionaty
# 사전은 키와 밸류 값으로 되어있음 {}로 만듬.

cabinet ={
    3:"유재석",
    100:"김태호",
    999:"노홍철"
}

print(cabinet[3])
print(cabinet[100]) 
#위와 같이 키값으로 인덱스처럼 가져오는 방법이 있으며

print(cabinet.get(100)) #get으로 가져오는 방법도있음'



# 아래 두가지 방식의 차이
# 두 가지 인자인 99는 위에 없지만
# print(cabinet[99]) 
# print("55")
#위의 방식은 오류로 인해 프로그램 멈추지만

print(cabinet.get(99)) #
print("55")
#get 방식은 NONE 으로 프로그램 진행시킴


# 해당 사전에 값이 있는지 없는 지 확인 하는법 블리언으로 확인
print(33 in cabinet)


#새로운 값 추가 및 삭제
bag ={"A-3":"재석","B-100":"김태호"}

print(bag["A-3"])
print(bag["B-100"])


# 그냥 키 값에 데이터 넣으면됨.
bag["A-3"]="짱아치"
bag["G-13"]="김아라치"
print(bag)

# 삭제 할꺼면
del bag["G-13"]     #del 명령어 넣은후 뒤에 키값으로 원하는 데이터 삭제.
print(bag)


print(bag.keys())       #키들만 출력
print(bag.values())     #값들만 출력
print(bag.items())      #키와 값들 모두 출력.
print(bag.clear())      #모든 값들 다 지우기.

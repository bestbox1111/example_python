

# 전체 컨셉은 set
# 중복 적용 안됨, 순서 안됨.

my={1,2,3,3,3}
print(my)       #{1,2,3} 이 출력


java={"유재석","김태호","양세형"}
# python = set(["유재석","박명수"])
python = {"유재석","박명수"}


print(java & python)    #교집합
print(java.intersection(python))    #교집합의 다른 방법


print(java | python)    #합집합
print(java.union(python))   #합집합의 다른 방법

print(java - python)    #차집합 (자바만 하고 파이썬 못할경우)
print(java.difference(python))   #차집합의 다른 방법 (자바만 하고 파이썬 못할경우)


python.add("김태호")    #값을 추가할때
print(python)

java.remove("김태호")   #값을 삭제할때
print(java)


#전체 컨셉은 자료 구조의 변경

order={"커피","우유","쥬스"}
print(order, type(order))

order= list(order)
print(order, type(order))

order= tuple(order)
print(order, type(order))

order= set(order)
print(order, type(order))
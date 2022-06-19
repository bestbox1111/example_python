


## 컨테이너...같은 타입이나 다른 타입의 정보를 담기위해...
# list , tuple, set , frozenset , dictionary



# my_list1=[10, 10.1,"park",True]
# my_list1([10, 10.1,"park",True])    변수 선언없이 그냥 떄려 받아도됨...튜플도 동일.
# print(type(my_list1))
# print(my_list1[0])      #리스트안에 있는 값을 확인 할때 인덱스로.

# vip_names=["newton", "oiler","gauss"]
# vip_names[0]="keple"
# print(vip_names)        #리스트는 안의 내용 업데이트 가능.  터플으 업데이트 가능 불가능.


# my_num=[12,20,30,40,50]
# print(my_num)
# print(my_num[:])    #위와 동일한 의미임.
# print(my_num[0:4:1])    # 시작점 : 끝나는점(마지막포함안됨) : 인덱스의 갭


# my_num2=[[10,20,30,40,50],[20,30]]
# print(my_num2[0])   #10,20,30,40,50
# print(my_num2[0][0])    #10
# print(my_num2[0][1])    #20  이런 순으로 나오게됨.


# old_list=[10,20,30,40,50]
# new_list=old_list       #메모리상 동일한 공간을 서로 공유하는 의미이므로, 어느 한쪽을 업데이트하더라도 같은 주소를 공유하고있으므로 서로 업데이트가 적용됨.
# print(new_list)
# print(old_list)
# new_list[4]=500
# print(new_list)
# print(old_list)


# old_list2=[10,20,30,40,50]
# new_list2=old_list2.copy()      #copy를 사용하면 공유오피스 사용안되고, 독립적으로 사용가능함.
# print(old_list2)
# print(new_list2)
# old_list2[4]=500
# print(old_list2)
# print(new_list2)



# old_list2=[10,20,30,40,50]
# new_list2=[60,70,80,90]  

# old_list2.extend(new_list2)     #리스트를 더하거 old_list2+new_list2와 같은의미임.
# print(old_list2)




# vip_names2=["newton", "oiler","gauss"]
# # vip_names2[3]="parkl"       #인덱스 처음 범위가 2번째 까지인대 3까지 넣으려니까 방이 터짐..할당안됨..이럴떄..
# vip_names2.append("park1")
# print(vip_names2)    
# vip_names2.remove("park1")      #지우고 싶을떄 remove는 인덱스는 못받고 값만 받을수있음
# # vip_names2.remove[0]    #오류가 남.
# vip_names2.pop(0)       # 인덱스로 지우려면 pop과 (인덱스) 로사용
# print(vip_names2)    
# vip_names2.clear()      # 리스트 타입만 남기고 모든 내용 지울때 사용.
# print(vip_names2)
# vip_names2.insert(0,"park")     #리스트에 인덱스 번호와 값을 넣어주면 내용 삽입됨.
# print(vip_names2)
# vip_names2.insert(1,"park2")
# print(vip_names2)
# find =vip_names2.index("park")      # 그냥 print 로 묶어서 처버리면 적용안됨... 변수로 저장해서 프린트사용
# count= vip_names2.count("park2")     #park2 가 몇번 들어갔는지 횟수 .
# print(find)
# print(count)



# mix=[-1,True,False,"gagra",100]
# park=mix.sort()
# print(park) #오류가 나는 이유는 여러가지 타입이 섞여있어서 소트를 할수가 없음.


# mix2=[-1,5,3,8]
# park=sorted(mix2)       #sort와 sorted의 차이가 존재함...
# print(park)



# vip_names3=["newton", "oiler","gauss"]
# print(vip_names3)
# vip_names3=vip_names3[-1::-1]     #reverse라는 함수도 역시 none으로 나오는대...헷갈립니다요...
# print(vip_names3) 





# my_tuple1=(10,10.1,"park",True)
# print(type(my_tuple1))




#set부분

# my_set1={10,"park",True}
# print(my_set1)
# # my_set1[0]      #set는 이런식으로 인덱스로 확인 불가능함.
# # print(my_set1)

# my_set2={10,20,30,40,10,20}     #중복된 값들은 알아서 제거해서 출력..순서는 상관없이 출력됨
# print(my_set2)

# my_set2.add(50)     # set에서 추가는 가능. add를 사용..
# print(my_set2)

# my_set2.discard(50)     # set에서 삭제도 가능 discard 와 remove의 차이는   remove는 작업하려는 값이 없으면 애러 뛰움. discard는 그냥 진행.
# print(my_set2)

# a={10,20,30,40,50}
# b={20,30,40,50,60}

# print(a | b)    #set 기능중 합집합
# print(a.union(b))   #위와 동일한 의미


# print(a & b)    #set 기능중 교집합
# print(a.intersection(b))   #위와 동일한 의미


# print(a - b)    #set 기능중 차집합
# print(a.difference(b))   #위와 동일한 의미


# print(a ^ b)    #set 기능중 교집합을 제외한모든것
# print(a.symmetric_difference(b))   #위와 동일한 의미


# a={10,20,30,40,50}
# b={40}
# print(b.issubset(a))    #subset이란... b가 a에 포함되어있냐고 묻는 블린형
# print(a.issuperset(b))  #superset이란 b에 있는 모든게 a 에 있냐고 묻는거


#frozenset는 그냥 읽기 전용으로만 사용... 추가되거나 조정되기 어려움.


#딕션어리

# diction = {"a":"park","b":"jun","c":"hyung"}
# print(diction["a"])     #인덱스가 아닌 키값으로 밸류를 확인 하는식
# # print(diction.get("a"))   #위와 동일 함

# diction["a"]="ppark"    #안의 값을 변경하는법
# print(diction["a"])  
# diction.update({"a":"ppark2"})  #안의 값을 업데이트라는 함수를 통해 변경가능.
# print(diction["a"])  
# print(diction)  

# diction.pop("c")    # c의 키에 해당하는 값을 지우기
# print(diction)  
# diction.clear()     # 모든 해당 내용 지우기. 형태만 남기기.
# print(diction)  


# member_list={"park",24,"java"}      # 리스트 언패킹...이라고 사용..
# name, age, lang = member_list       #  하나씩 저장 하고 싶을떄 한줄로 가능
# #원래예상은
# #name = member_list[0] 이런식이지만 한줄로 다됨..
# #조금더 딥하게 들어간다면 name, *p_data= member_list 라고 작성하면 name="park"이 들어가고 나머지 p_data에 나머지 정보가 다 저장된다는 의미
# print(name, age, lang)



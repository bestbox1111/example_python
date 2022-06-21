


## 함수에 관해서2 position부분 ###

# def add(a,b):   
#     print("add 의 합은" ,a+b)
#     return a+b
# add(10,20)  # a= 10이고 b= 20으로 들어가지만.

# #꼭 함수의 인자에 순서대로 넣고싶지않을때

# def m_print(name, age=0,lang="english"):
#     print(name+' '+str(age)+' '+lang)

# m_print("park")     #매개변수를 하나만 넣었지만 오류없음 위에서 2,3번째 기본값으로 세팅.
# m_print("park", 90)  #매개변수를 두개 넣었지만 오류없음 위에서3 번째 기본값으로 세팅. 2반째는 입력값으로 업데이트됨.
# m_print("park", 90,"korean")     #위와 동일하게 매개변수 값으로 변환됨.
# print()
# # m_print("park","pythion", 54)   #이런식으로 매게변수의 순서가 뒤석이면 함수에선("네임(스트링)","에이지(인트)","랭(스트링)")

# #위와 같았지만 매개변수 위치에 관계없이 사용하려면 아래와 같이 변수명과 값을 같이 세팅해줌.
# m_print("park", lang="pythoanksisk", age=777)



## 임의로 들어오는 매개변수 처리.###

# def multi(*args):       #몇개를 받아야 할지 모를때 *args로 받기.
#     for muls in args:
#         print(muls)
#     print()
# multi("akak")
# multi("akak","Garmlgm")
# multi("akak",3,4,5)
# multi("akak",4,5,5,3,"gmkalmgk")

## 임의의 수를 더해야 하는 계산기를 만든다고 가정...ex

# def cal_sum(*args): #인자를 몇개 받을지 모르니...*args
#     total =0            #모든 인자의 합을 넣을 변수
#     for cal in args:    #매개 변수가 순번대로 cal에 들어가고.
#         total+=cal      # total에 차독차독 cal이 더해짐.
#     print(total)        # print로 총합 출력하고
#     return total        #리턴값으로도 총합 출력.

# cal_sum(1,2,3,4,5,6,7,8,9,10)   #1~10 까지 인자 받거나 그 이상, 이하도 동일


### unpacking

# a=[10,15]
# # for b in range(a[0],a[1]+1):
# #     print(b,end=" ")

# a[1]+=1         #위의 방법을 *a라는 방식으러 변한풀이
# for b in range(*a):
#     print(b,end=" ")
    
    
#위의 예제를 함수로 만들시에.

# def my_lst():
#     start = int(input("처음 숫자를 입력 하시요??? "))
#     last = int(input("마지막 숫자를 입력 하시요??? "))
#     increase = int(input("증가 숫자를 입력 하시요??? "))
#     for outlst in range(start, last+1, increase):
#         print(outlst)
#     return outlst
# my_lst()
# 사용자가 입력을 처음, 끝, 증가숫자 이렇게 3번을 넣으니 불편하여 업그레이드..


# def my_lst2():        #위의 방식보다 조금더 반복문을 사용하여 리스트로 넣어서 코드가 간결해짐.
#     print("처음숫자, 끝자리, 증가숫자    ex: 1,30,2" )
#     ui = input("세자리를 ,로 구분하여 입력하요 주새요~?")
#     ui_list=[int(i) for i in ui.split(",")]
#     ui_list[1]+=1
#     out_list =list(range(*ui_list))
#     print(out_list)
# my_lst2()



# 흐름 제어. for if while break continue pass 등등.

import numpy as np

# x_list=[1,2,3]
# x_tuple=(1,2,3)
# x_set={1,2,3}
# x_dic={'a':1, 'b':2,'c':3}

# x_array= np.array([1,2,3])
# x_range= range(1,4,1)

#스트링
# for i in "python":
#     print("i "+str(i))



#딕션어리
# i={"a":20, "b":30, "c":40}
# for ii in i:            #i면 기본 딕션어리 에서 키값을 출력.i.values() 및 i.items()로 분할
#     print("ii " ,ii)
    
    
# for f in range(2,10):       #구구단 이중 for문의 예시임.
#     for l in range(1,10):
#         print("{} * {} ={}".format(f,l,f*l))
#     print()



#enumerate  값과 인덱스를 같이 불러오고싶을때

# m =np.array([10,20,30])
# vip=["park","jun","hyung"]
# pd={"a":11,"b":21,"c":31}


# for idx, value in enumerate(m):
#     print(idx, value)




#zip        같은 인덱스 번호끼리 있는걸 묶어주는 역활
# m =np.array([10,20,30])
# vip=["park","jun","hyung"]
# pd={"a":11,"b":21,"c":31}

# for i in zip(m,vip):
#     print(i)



###활용 예제

# s="best company.    tel: 1234-5678"
# for i in range(1,6):
#     print(s)
#     print()


# vip=['kepler',"newton","euluer"]
# for name in vip:
#     print("name :", name)
#     print("2022 party show")
#     print()


# x=np.array([10,20,30,40,50])
# for i in x:
#     print("{}의 제곱은 : {}".format(i,i**2))    #제곱의 값만 출력할때사용for문
    
# for idx,i in enumerate(x):
#     print("인덱스{}번째 {}의 제곱은 : {}".format(idx,i,i**2)) 
    
# y=np.zeros(x.shape)         #0으로 채워줘라..
# for idx,i in enumerate(x):
#     y[idx]=i**2
#     print(y)        #인덱스 0부터 반복문을 돌면서 제곱을 채워주며 마무리함.
#결과값은
"""
[100.   0.   0.   0.   0.]
[100. 400.   0.   0.   0.]
[100. 400. 900.   0.   0.]        
[ 100.  400.  900. 1600.    0.]   
[ 100.  400.  900. 1600. 2500.]  이렇게됨.
"""



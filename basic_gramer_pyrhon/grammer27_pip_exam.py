

#### pip 관련 사용법 및 인스톨

#pip list   인스톨된 패키지들 확인함
#pip show 해당패키지  == 정보볼수있음
#pip install --updrade  해당패키지
#pip uninstall 해당패키지



#### 내장 함수 ####

# input :사용자 입력 받는 함수
# lang = input("언어를 입력해주세요??")
# print(f"나는 {lang} 의 언어를 좋아합니다.")


#dir: 어떤 객체를 넘겨줬을때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
import random   #d외장함수
print(dir())    #현제 어떤 외장 함수들을 쓸수 있는지 확인됨. random 임포트 후에 dir로 확인하면 random추가됨
print(dir(random))  #dir에 random을 넣어 확인하면 random안에 들어가있는 함수들을 확인 할수잇음

print()
print()
print()

lst=[1,2,3]
print(dir(lst))
#리스트를 dir에 넣으면  ['__add__', '__class__', '__class_getitem__', '__contains__',
# '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', 
# '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '
# __init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', 
# '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__',
# '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 
# 'insert', 'pop', 'remove', 'reverse', 'sort'] 과 같은 함수들을 사용할수 있음


## 검색창에 list of python builtins 라고 치면 사용할수있는 내장 함수들 확인됨
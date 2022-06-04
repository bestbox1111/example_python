

#### 전체 컨셉은 기본 값

def profile(name, age, main_lang):
    print("이름: {} ,나이 : {}, 주사용언어 : {}".format(name, age, main_lang))

profile("유재석", 20," 자바")
profile("김태호", 20," 자바바호")
#위와 같은 함수를 만들어서 인자를  받아야 하지만



# 나이가 동일한 친구들일 경우에 

#아래와 같이 직접 함수에다 값을 더미식으로 떄려박아놓을수도있음
def profile2(name, age=17, lang="파이썬"):
    print("이름: {}, 나이: {}, 언어 {}".format(name,age,lang))
profile2("유재석")
profile2("하하")



####전체 컨셉은 키워드 값을 이용한 구문
#함수에 들어가있는 순서대로 안넣어도된다는 소리.예를들면
def profile3(name, age, lang):
    print(name,age,lang)

#아래와 같이 순서상관없이 키와 밸류 식으로 매칭만 시켜주면됨.
profile3(age=20, lang="자바", name="유재석")


#####전체 컨셉은 가변인자
#아래와 같이 함수안에 넣어야할 인지가 현제는5개이지만 많아질 경우
def profile4(name, age, lang1, lang2, lang3):
     print("이름: {} ,나이 : {}, 사용언어 : {}, 사용언어2 : {}, 사용언어3 :{}".format(name, age, lang1,lang2,lang3))

profile4("유재석44", 20," 자바","파이싼","씨언어")


#할줄 아는 언어가 더 추가 되거나 삭제될 수도 있는 경우
#함수 안에서 더 추가 딜수도 있는 부분의 인자앞에 *을 붙이고
# 더 추가될 {}를 지우고 반복문 프린트로 바로 출력하도록
def profile5(name, age, *language):
    print("이름: {} ,나이 : {}, 사용언어 : ".format(name, age), end=" ")  #end=" "일경우 줄바꿈하여 다음라인에서도 윗라인과 이어져서 작성이 된다.
    for lang in language:
        print(lang, end =" ")
    print()
        
profile5("유재석", 20," 자바","파이싼","씨언어")
profile5("김태호", 11," 자바")
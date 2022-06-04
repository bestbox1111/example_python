
import pickle
import profile

#### 전체 컨셉 = pickle
# 저장하기
# profile_file = open("profile.pickle","wb")      #피클 쓰기용  w이고  b 는 바이너리..항상 b를 붙여야함.
# profile={"이름":"박명수","나이":40, "취미":["축구","골프","코딩"]}
# print(profile)
# pickle.dump(profile,profile_file)       #profile이라는 데이터를 profile_file이라는 파일에 저장하는

# profile_file.close()


# 불러오기
# profile_file = open("profile.pickle","rb")      #피클 쓰기용  w이고  b 는 바이너리..항상 b를 붙여야함.
# profile=pickle.load(profile_file)      #file에 있는 저오를 profile에 불러오기
# print(profile)

# profile_file.close()



#### 전체 컨셉은 with 
# with로 불러오기
# with open("profile.pickle","rb") as profile_file:
#     print(pickle.load(profile_file))


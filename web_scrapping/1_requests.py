import requests


# res=requests.get("http://naver.com")
# res=requests.get("https://www.melon.com")  #다른 숫자면 비정상.

# print("응답코드 :",res.status_code) #응답코드 200이면 정상  
# res.raise_for_status()  # 문제가 없으면 그냥 넘어가고 문제가 있으면 오류 생성.


# res=requests.get("http://naver.com")
# if res.status_code == requests.codes.ok:    # requests.codes.ok=200이란소리
#     print("정상입니다.")
# else:
#     print("문제가 생겼습니다.[에러코드 ", res.status_code,"]")



# 아래 두 라인을 구문으로 사용..위에11~15라인과 동일함.
res=requests.get("http://naver.com")
res.raise_for_status() 
print(len(res.text))


with open("mygoogle.html", "w", encoding="utf8") as f:
    f.write(res.text)
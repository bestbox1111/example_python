


# user_agent란...
# 링크로 접속할때는 접속이 되지만 request로 접속하게 되면
# pc가 접속을 제한 하는데, 그 제한을 푸는데 필요한 부분. 



from email import header
import requests

# res=requests.get("http://www.jolse.com/category/moisturizer/1017/?page=2")  #다른 숫자면 비정상.
# #메론 같은 경우 406d오류 지만..일단 주석으로 진행
# # res.raise_for_status()  # 문제가 없으면 그냥 넘어가고 문제가 있으면 오류 생성.
# with open("nadocoding.html", "w", encoding="utf8") as f:
#     f.write(res.text)
#뭔가 굉장히 부족한 html이 생성되지만.
    

# requests 가 막혔을때 사용하는 user-agent사용구문
url="http://www.jolse.com/category/moisturizer/1017/?page=2"
header={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36"} #구글에서 user-agent string으로 검색후 wahtigmybrowser사이트에서 나온주소가 내주소임.복붙해 사용
res=requests.get(url, headers=header)
with open("nadocoding2.html", "w", encoding="utf8") as f:
    f.write(res.text)
#완벽한 html구조로 생성됨.
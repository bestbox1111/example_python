
#  부몯ㅇ산 매물 (송파 헬리오 시티) 정보를 스크래핑 하는 프로그램.

"""
    조회조건
    1. https://www.daum.net/
    2.송파 헬리오시티 검색
    3. 다음 부도안 부분에 나오는 결과 정보
 """
 
 
#  출력결과
#  =======매물1 =======
#  거래:매물
#  면적: 84/67(공급/전용)
#  가격: 165,000
#  동: 314호
#  층 : 고 /34
 
#  ======매물 2 =========



from bs4 import BeautifulSoup
import requests


url="https://search.daum.net/search?w=tot&DA=UME&t__nil_searchbox=suggest&sug=&sugo=15&sq=%EC%86%A1%ED%8C%8C+%ED%97%AC%E3%84%B9&o=1&q=%EC%86%A1%ED%8C%8C+%ED%97%AC%EB%A6%AC%EC%98%A4%EC%8B%9C%ED%8B%B0"
# headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36"} #구글에서 user-agent string으로 검색후 wahtigmybrowser사이트에서 나온주소가 내주소임.복붙해 사용

res=requests.get(url)
res.raise_for_status()

soup=BeautifulSoup(res.text,"lxml")


inco= soup.find("ul", attrs={"class":"list_place"}).get_text()# 다음 부동산에서리스트에 뜬6개만 일단 가져오게됨. 
print(inco)

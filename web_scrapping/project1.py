


# 조건

# 1. 네이버에서 오늘 서울의 날씨 정보를 가져온다.
# 2. 헤드라인 뉴스 3건을 가져온다.
# 3. it뉴스 3건을 가져온다
# 4. 해커스 어학원 홈페이지에서 오늘의 영어 회화 지문을 가져온다.

# [1.출력예시]
# 흐림, 어제보다 00 높아요
# 체감 00 도  습도 00  바람 00 
# 오전 강수확율 00% /오후 강수확율 00%

# 미세먼지 00//좋음
# 초미세먼지 00// 좋음.


from bs4 import BeautifulSoup
import requests


url="https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%84%9C%EC%9A%B8%EB%82%A0%EC%94%A8&oquery=%EB%84%A4%EC%9D%B4%EB%B2%84%EB%82%A0%EC%94%A8%EC%A0%95%EB%B3%B4&tqi=hrfyfsprvTossNowgX8ssssstTw-303068"
res= requests.get(url)
res.raise_for_status()

soup =BeautifulSoup(res.text, "lxml")



yesterday_temp= soup.find("span",attrs={"class":"temperature"})
print(" 어제보다" ,yesterday_temp.text)

pysycal=soup.find("dl",attrs={"class":"summary_list"})
print(pysycal.text)



# morning=soup.find("span",attrs={"class":"weather_left"})
# print(morning.text)     #큰오류에 봉착.... 오전 온도와 오후 온도가 모두 동일한 클래스와 태크인대 어떻게 이걸 구분해야 할지...


morning=soup.find("li",attrs={"class":"week_item today"})
print(morning.text)

morning2= morning.find("div",attrs={"class":"cell_weather"})
print(morning2.text)




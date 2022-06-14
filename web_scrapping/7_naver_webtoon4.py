
import socketserver
from turtle import title
import requests
from bs4 import BeautifulSoup


url="https://comic.naver.com/webtoon/list?titleId=675554"
res=requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
#네이버 웹툰 가우스전자의 10회분  평가 점수 가져와서 점수 합계와 평균점수 구하기

scores = soup.find_all("div", attrs={"class":"rating_type"})

total_rate=0

for score in scores:
    avg= score.find("strong").get_text()
    print(avg)
    total_rate += float(avg)
    
    
print("전체 합계 :" , round(total_rate,2))
print("평균 점수 : " , round(total_rate/ len(scores),2))
    


from turtle import title
import requests
from bs4 import BeautifulSoup


# url="https://comic.naver.com/webtoon/weekday"
# res=requests.get(url)
# res.raise_for_status()

# soup = BeautifulSoup(res.text, "lxml")

# #네이버 웹툰 전체 목록 가져오기
# catoons =soup.find_all("a", attrs={"class":"title"})
# # class 속성이 title인 모든 목록 출력
# for cartoon in catoons:
#     print(cartoon.get_text())


url="https://comic.naver.com/webtoon/list?titleId=675554"
res=requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
#네이버 웹툰 전체 목록 가져오기
catoons =soup.find_all("td", attrs={"class":"title"})
# class 속성이 title인 모든 목록 출력
for cartoon in catoons:
    
    
    title=cartoon.a.get_text()
    link = "http://comic.naver.com" + cartoon.a["href"]
    
    print(title, link)

    
    # print(cartoon.get_text())
    # print(cartoon.a["href"])
    
    
    
# print(catoons[0].a.get_text())


# link= catoons[0].a['href']
# print(link)
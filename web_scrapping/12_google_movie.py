
from attr import attrs
from bs4 import BeautifulSoup
import requests
import time


url="https://play.google.com/store/movies"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36","Accept-Language":"ko-KR,ko"}
res= requests.get(url, headers=headers)
res.raise_for_status()


soup= BeautifulSoup(res.text, "lxml")

movies= soup.find_all("div", attrs={"class":["VfPpkd-EScbFb-JIbuQc", "MxsXJd"]})

print(len(movies))

# with open("movies.html","w",encoding="utf8") as f:
#     f.write(soup.prettify())

for movie in movies:
    title = movie.find("div", attrs={"class":"hP61id"}).get_text()
     
    # title = movie.find("div", attrs={"class":"Epkrse"}).get_text()
    print(title)
    
    
#### 현 사이트에서는 필요 없지만, 로딩되는 시간관련되서 스크롤내리기

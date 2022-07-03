

from bs4 import BeautifulSoup, BeautifulStoneSoup
import requests


url="https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90"
res=requests.get(url)
res.raise_for_status()


soup = BeautifulSoup(res.text,"lxml")   #res.text로 html 구조를 담은 soup객체를 만듬
links= soup.select(".news_tit")         #그 객체중에 클래스가 new_tit인 모든애들을 links에 저장.  select는 전부. 하나일때는  select_one


for link in links:          #links 가 배열식으로 전부 들어갔으니,  for문으로 하나씩 변수에 다시 저장해줘야함.
    title= link.text        #link중에 text인 애들만  title 로 저장.
    url= link.attrs["href"]     #link 중에 속성이 href인 애들만 url로 저장.
    print(title)
    print(url)
    print("=="*10)

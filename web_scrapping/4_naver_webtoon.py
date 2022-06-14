
from bs4 import BeautifulSoup
from email import header
import requests

# res=requests.get("http://www.jolse.com/category/moisturizer/1017/?page=2")  #다른 숫자면 비정상.
# #메론 같은 경우 406d오류 지만..일단 주석으로 진행
# # res.raise_for_status()  # 문제가 없으면 그냥 넘어가고 문제가 있으면 오류 생성.
# with open("nadocoding.html", "w", encoding="utf8") as f:
#     f.write(res.text)
#뭔가 굉장히 부족한 html이 생성되지만.
    

# requests 가 막혔을때 사용하는 user-agent사용구문
url="https://comic.naver.com/webtoon/weekday"
res=requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
# print(soup.title)
# print(soup.title.get_text())
# print(soup.a.attrs)
# print(soup.a["href"])


# print(soup.find("a", attrs={"class":"genreRecomImg2"})) a태크의 속성중 클래스가 ge....인애를 찾아라가됨.
# print(soup.find( attrs={"class":"genreRecomImg2"})) #class가 gen...인 애를 찾아줘


#웹툰 만화의 인기급상승 부분중 랭크부분 가져오기
# print(soup.find("li", attrs={"class":"rank01"}))    #이렇게 해버리면 랭크1에 해당하는 a태그 span태그 img태그 모든 걸 다가져오게됨.
rank01= soup.find("li", attrs={"class":"rank01"})   
# print(rank01.a)
# print(rank01.img)
# print(rank01.span)
# 위와 같이 원하는 태그만 찾아서 볼수도있음.

# print(rank01.get_text())    #해당 영역의 글자만 뽑기
# print(rank01.next_sibling.next_sibling) #해당 같은 영역이지만 다음 리스트읙글자만 뽑기 넥스트시블링 두번한건 일종의 스페이스가 존재함.


rank02= rank01.next_sibling.next_sibling
rank03=rank02.next_sibling.next_sibling
#위와 같이 똑같은 함수를 두번쓰는건 비효율적임.
rank02 = rank01.find_next_sibling("li") 
print(rank02.a.get_text())  

# print(rank03.a.get_text())  
# print(rank01.parent)    #rank01의 바로 윗 태그로 이동할수 있음. rank01~10까지 ol로 묶여있어서 그부분가지 출력됨.
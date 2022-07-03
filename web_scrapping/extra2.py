


from bs4 import BeautifulSoup, BeautifulStoneSoup
import requests
import pyautogui

name=pyautogui.prompt("검색어를 입력하세요??")

lastpage =int(pyautogui.prompt("원하는 페이지를 입력하세요??"))
pageNum=1

for i in range(1,lastpage*10,10):           # for문 돌리는 이유?   한페이지가 아닌  내가 지정한 페이지 만큼 스크랩을 해야하므로. url 안에 페이지 정보를 넣기 위해.   
    print()                                 # url 페이지 정보 입력시 1페이지 =1 , 2페이지 11, 3페이지 21, 4페이지31 이런식이라 페이지 알고리즘 팔요., 
    print()                                 # range(1= 시작점, lastpage*10= 끝페이지, 10= 고객이 정한 마지막 페이지를 10으로 나눠서 끝자리를 1로 맞추어서 페이지 정보를 맞추기위해.)
    print("======{} 페이지입니다=====".format(pageNum))
    url="https://search.naver.com/search.naver?where=news&sm=tab_pge&query={}&sort=0&photo=0&field=0&pd=0&ds=&de=&cluster_rank=58&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:all,a:all&start={}".format(name,i)       #입력받은 검색란과 페이지 정보란을 변수로  url 에 넣음.
    res=requests.get(url)       #리퀘스트를 써서 url 을 변수에 저장.
    res.raise_for_status()      #오류체크함수
    soup = BeautifulSoup(res.text,"lxml")   #뷰티풀스을 이용해  html 구조로 변환한 변수저장.
    links= soup.select(".news_tit")         #저장한 변수중 클래스가 new_tit인 애들을  links에 저장.
 
  
    for link in links:          #links 가 리스트니  for 문 사용해 하나씩 꺼내서 다시저장.
        
        title= link.text        #필요한 크롤링 부분 설정
        url= link.attrs["href"] #필요한 크롤링 부분 설정
 
        print(title)        #출력
        print(url)          #출력
        print("=="*20)      #출력
    pageNum+=1              #페이지 정보를 위해 pagenum=1에서  페이지의 마지막 정보 for 문 끝날때  num추가해줌.

print()
print()
print()
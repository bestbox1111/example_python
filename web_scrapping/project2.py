from bs4 import BeautifulSoup
import requests




def create_soup(url):
    res=requests.get(url)
    res.raise_for_status()
    soup=BeautifulSoup(res.text,"lxml")
    return soup


def head_news():
    print("[헤드라인뉴스]")
    url="https://news.naver.com"
    soup=create_soup(url)



    names= soup.find("ul", attrs={"class":"cc_text_list"}).find_all("li",limit=3)       #오류나서 안됨...이유모르겠음..ㅆㅂ...ㄹ쉬..   limit=객수제한..
    for inx, name in enumerate(names):
        title= name.find('a').get_text().strip()
        link= url +name.find('a')["href"].get_text()

        print("{}.  {}".format(inx+1, title))
        print(link)


head_news()

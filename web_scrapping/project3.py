from attr import attr
from bs4 import BeautifulSoup
import requests
import re



def create_soup(url):
    res=requests.get(url)
    res.raise_for_status()
    soup=BeautifulSoup(res.text,"lxml")
    return soup


def head_news():
    print("[해커스영어]")
    url="https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english&keywd=haceng_submain_lnb_eng_I_others_english&logger_kw=haceng_submain_lnb_eng_I_others_english"
    soup=create_soup(url)

    #  문제 영어와 한글이 같은 클래스 네임으로 되어있어서 구분하기 어려움.
    # en_sen=soup.find_all("div", attrs={"class":"conv_txt"})
    # for en in en_sen:
    #     print(en.text)
    
    
    sentence = soup.find_all("div", attrs={"id":re.compile("^conv_kor_t")})
    print()
    print("[영어 지문]")        # 해당 사이트에서 총8줄로 한글4, 영어 4줄을 유추가능.
    
    for sentences in sentence[len(sentence)//2:]:    #해당 사이트 한글이 먼저 나오고, 영어가 나중에 나옴.
        print(sentences.get_text().strip())           #인덱스로 0부터 7까지 중 4~7까지를 먼저 출력구문. 영어구문위해.
    
    print()
    print("한글지문")
    for sentences in sentence[:len(sentence)//2:]:    #이부분이 조금 헷갈리구만요....
        print(sentences.get_text().strip())    

head_news()
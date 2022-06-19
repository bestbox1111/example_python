
from bs4 import BeautifulSoup
import csv
import requests


url="https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page="              
file_name="naver_cospi_200.csv"             ##엑셀 파일로 저장하기 위해 필요한 구문
f= open(file_name,"w", encoding="utf-8-sig", newline="")        ##엑셀 파일로 저장하기 위해 필요한 구문```newline 및 utf-8-sig`
# new line ="" 인 이유는 공백이 아니면 데이터 받을떄
# ['1', '삼성전자', '60,700', '1,200', '-1.94%', '100', '3,623,658', '5,969,783', '50.19', '26,542,979', '9.53', '13.92', '']
# 공백..
#['2', 'LG에너지솔루션', '420,000', '6,500', '-1.52%', '500', '982,800', '234,000', '3.27', '274,703', '133.84', '10.68', '']
#이런식으로 공백이 생겨서 공백제거용으로.

writer = csv.writer(f)         ##엑셀 파일로 저장하기 위해 필요한 구문
title="N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE".split("\t")
writer.writerows(title)
print(type(title))

for page in range(1,2):
    res =requests.get(url +str(page))
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    
    data_rows = soup.find("table", attrs={"class":"type_2"}).find("tbody").find_all("tr")
    for row in data_rows:
        columns = row.find_all("td")
        if len(columns)<=1:             #네이버 주가 총액 가져올때 공백 부분 ['']으로 표기되는 부분들 제거하기 위한 구문이며
            continue
        data =[column.get_text().strip() for column in columns]             #column.get_Text()뒤에.stript()를 찍어주는 이유는 출력시 의미 없이 빈 공백이 많은 구문들때문 \n\n\n\n\n\n이런..
        # print(data)
        writer.writerows(data)             ##엑셀 파일로 저장하기 위해 필요한 구문
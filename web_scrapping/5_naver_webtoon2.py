
from bs4 import BeautifulSoup
# from email import header
import requests


url="https://comic.naver.com/webtoon/weekday"
res=requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")


webtoon = soup.find("a", text="외모지상주의")

print(webtoon)
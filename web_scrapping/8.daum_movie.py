import requests


from bs4 import BeautifulSoup

url="https://search.daum.net/search?w=tot&q=2021%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR"

res=requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

images =soup.find_all("img",attrs={"class":"thumb_img"})

# for image in images:
#     # print(image["src"])
#     image_url = image["src"]
#     if image_url.startswith("//"):
#         image_url="https:" +image_url
        
#     print(image_url)
#     image_res = requests.get(image_url)
#     image_res.raise_for_status()
    
    
#한해에 해당하는 부분할때적용
for idx, image in enumerate(images):
    image_url = image["src"]
    if image_url.startswith("//"):
        image_url="https:" +image_url
    print(image_url)
    image_res = requests.get(image_url)
    image_res.raise_for_status()
    with open("movie{}.jpg".format(idx+1), "wb") as f:
        f.write(image_res.content)
    if idx >=4:
        break
    
#d원하는 해당 년도 부터 적용하기위한 2중 for문

for year in range(2015,2022):
    res=requests.get("https://search.daum.net/search?w=tot&q={}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR".format(year))
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "lxml")

    images =soup.find_all("img",attrs={"class":"thumb_img"})
    
    
    
    for idx, image in enumerate(images):
        image_url = image["src"]
        if image_url.startswith("//"):
            image_url="https:" +image_url
        print(image_url)
        image_res = requests.get(image_url)
        image_res.raise_for_status()
        with open("movie{}년{}.jpg".format(year, idx+1), "wb") as f:
            f.write(image_res.content)
        if idx >=4:
            break
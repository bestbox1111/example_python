from openpyxl import Workbook
from openpyxl.drawing.image import Image


wb= Workbook()
ws=wb.active

#전체 컨셉은 이미지 저장하기.

img= Image("car2.png")      #car2라는 이미지 파일을 img 에 저장


ws.add_image(img,"C2")  #img를 C2에 이미지 저장.

wb.save("sample_image.xlsx")    
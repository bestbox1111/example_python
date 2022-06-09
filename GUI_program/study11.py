from tkinter import *
import tkinter.messagebox as msbox
import tkinter.ttk as ttk
import time
from turtle import right

#### 전체 컨셉 = 프레임
root = Tk()
root.title("킹왕짱스 프로그램")     #프로그램 창의 이름
root.geometry("640x480+100+200")    #프로그램의 넓이,높이,x좌표,y좌표



Label(root, text="메뉴를 선택해 주세요.").pack(side="top")

frame_burger =Frame(root, relief="solid", bd=1) #relief ="외각선" ,    bd= 굴기
frame_burger.pack(side="left", fill="both", expand=True)
Button(frame_burger, text="햄버거").pack()
Button(frame_burger, text="치즈햄버거").pack()
Button(frame_burger, text="불고기햄버거").pack()
Button(frame_burger, text="빅햄버거").pack()



frame_drink =LabelFrame(root, text="음료") 
frame_drink.pack()
Button(frame_drink, text="콜라").pack()
Button(frame_drink, text="사이다").pack()
Button(frame_drink, text="스프라이트").pack()



# frame_burger2 =Frame(root, relief="solid", bd=1) #relief ="외각선" ,    bd= 굴기
# frame_burger2.pack(side="right")
# Button(frame_burger2, text="햄버거").pack()
# Button(frame_burger2, text="치즈햄버거").pack()
# Button(frame_burger2, text="불고기햄버거").pack()
# Button(frame_burger2, text="빅햄버거").pack()


# frame_burger3 =Frame(root, relief="solid", bd=1) #relief ="외각선" ,    bd= 굴기
# frame_burger3.pack(side="left")
# Button(frame_burger3, text="햄버거").pack()
# Button(frame_burger3, text="치즈햄버거").pack()
# Button(frame_burger3, text="불고기햄버거").pack()
# Button(frame_burger3, text="빅햄버거").pack()



# frame_burger3 =Frame(root, relief="solid", bd=1) #relief ="외각선" ,    bd= 굴기
# frame_burger3.pack(side="left" ,fill="both")
# Button(frame_burger3, text="햄버거").pack(fill="both")
# Button(frame_burger3, text="치즈햄버거").pack(fill="both")
# Button(frame_burger3, text="불고기햄버거").pack(fill="both")
# Button(frame_burger3, text="빅햄버거").pack(fill="both")


# frame_burger4 =Frame(root, relief="solid", bd=1) #relief ="외각선" ,    bd= 굴기
# frame_burger4.pack(side="left" ,fill="both" ,expand="true")     #fill ="위아래로 꽉꽉 채우고", expand ="양얖으로 "
# Button(frame_burger4, text="햄버거").pack(fill="both")
# Button(frame_burger4, text="치즈햄버거").pack(fill="both")
# Button(frame_burger4, text="불고기햄버거").pack(fill="both")
# Button(frame_burger4, text="빅햄버거").pack(fill="both")






Label(root, text="메뉴를 선택해 주세요.").pack(side="bottom")





#각 함수에 맞는 이미지가 같이 사용됨. waring노랑이 err빨강이
root.mainloop()
from tkinter import *
import tkinter.messagebox as msbox
import tkinter.ttk as ttk
import time
from turtle import right

#### 전체 컨셉 = 스크롤바
root = Tk()
root.title("킹왕짱스 프로그램")     #프로그램 창의 이름
root.geometry("640x480+100+200")    #프로그램의 넓이,높이,x좌표,y좌표


frame =Frame(root)
frame.pack()

scrolbar= Scrollbar(frame)
scrolbar.pack(side="right", fill="y")         #스크롤바도 프레임에 들어야함.  fill="y"는 y츅으로 없으면 해보면암.

        
        
        
listbox=Listbox(frame, selectmode="extended", height=10, yscrollcommand=scrolbar.set)   #ysccontrlcomaand= scrollbar.set안넣으면 스크롤 안땡겨짐. 
for i in range(1,32):
    listbox.insert(END, str(i)+ "일")

listbox.pack(side="left")      #리스트 박스도 프레임에 들어가 있는것이 일반적임
scrolbar.config(command=listbox.yview)      #스크롤바를 내림과 동시에 listbox 에 맵핑되어 서로 합을 맞추는 역할



#각 함수에 맞는 이미지가 같이 사용됨. waring노랑이 err빨강이
root.mainloop()
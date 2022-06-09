
from tkinter import *
import tkinter.messagebox as msbox
import tkinter.ttk as ttk
import time
from turtle import right

#### 전체 컨셉 = 그리드기본
# 그리드의 기본적으로 안드로이드 그리드와 마찬가지로 00,01,02와 같은 이중배열구조임


root = Tk()
root.title("킹왕짱스 프로그램")     #프로그램 창의 이름
root.geometry("640x480+100+200")    #프로그램의 넓이,높이,x좌표,y좌표







# btn1.pack(side="left")
# btn2.pack(side="left")

# btn1.grid(row=0, column=0)      #그리드로 만들시 로우와 컬럼으로 작업한다고보면됨...이것도 노가다인디...ㅆㄲ
# btn2.grid(row=1, column=1)      #그리드로 만들시 로우와 컬럼으로 작업한다고보면됨...이것도 노가다인디...ㅆㄲ


#예시로 키보드 우측 숫자 키보드를 만드는 예시임.


#먼저 버튼을 root에 쒸우고 텍스트 만듬.
btn1= Button(root, text="F9", width=5, height=2)  #padx,y 는 글자기준으로 버튼에서 적용된다.   가끔 긴글자때문에 각 사이즈가 안맞는 경우가 생기므로 그냥 버튼의 width와 height로 무식하게 작업하는게 짱임.
btn2 =Button(root, text="F10", width=5, height=2)   
btn3= Button(root, text="F11", width=5, height=2)
btn4 =Button(root, text="F12", width=5, height=2)

btn5= Button(root, text="clear", width=5, height=2)
btn6 =Button(root, text="=", width=5, height=2)
btn7= Button(root, text="/", width=5, height=2)
btn8 =Button(root, text="*", width=5, height=2)

btn9= Button(root, text="7", width=5, height=2)
btn10 =Button(root, text="8", width=5, height=2)
btn11= Button(root, text="9", width=5, height=2)
btn12 =Button(root, text="-", width=5, height=2)

btn13= Button(root, text="4", width=5, height=2)
btn14 =Button(root, text="5", width=5, height=2)
btn15= Button(root, text="6", width=5, height=2)
btn16 =Button(root, text="+", width=5, height=2)

btn17= Button(root, text="1", width=5, height=2)
btn18 =Button(root, text="2", width=5, height=2)
btn19 =Button(root, text="3", width=5, height=2)
btn20= Button(root, text="enter", width=5, height=2)
btn21 =Button(root, text="0", width=5, height=2)
btn22= Button(root, text=".", width=5, height=2)



#그후에 pack() 하는거 대신 .grid로 실제 작업
btn1.grid(row=0, column=0, sticky=N+E+W+S, padx=3, pady=3)     #, sticky=N+E+W+S  지정한 방향으로 확장한다는 뜻이더강함.   padx, pady는 버튼에다가 주면 글자기준이며, 그리드에다 주면 외부기준에 버튼이 적용됨
btn2.grid(row=0, column=1, sticky=N+E+W+S, padx=3, pady=3)   
btn3.grid(row=0, column=2, sticky=N+E+W+S, padx=3, pady=3)     
btn4.grid(row=0, column=3, sticky=N+E+W+S, padx=3, pady=3)  

btn5.grid(row=1, column=0, sticky=N+E+W+S, padx=3, pady=3)     
btn6.grid(row=1, column=1, sticky=N+E+W+S, padx=3, pady=3)  
btn7.grid(row=1, column=2, sticky=N+E+W+S, padx=3, pady=3)     
btn8.grid(row=1, column=3, sticky=N+E+W+S, padx=3, pady=3)  

btn9.grid(row=2, column=0, sticky=N+E+W+S, padx=3, pady=3)     
btn10.grid(row=2, column=1, sticky=N+E+W+S, padx=3, pady=3)  
btn11.grid(row=2, column=2, sticky=N+E+W+S, padx=3, pady=3)     
btn12.grid(row=2, column=3, sticky=N+E+W+S, padx=3, pady=3)  

btn13.grid(row=3, column=0, sticky=N+E+W+S, padx=3, pady=3)     
btn14.grid(row=3, column=1, sticky=N+E+W+S, padx=3, pady=3)  
btn15.grid(row=3, column=2, sticky=N+E+W+S, padx=3, pady=3)     
btn16.grid(row=3, column=3, sticky=N+E+W+S, padx=3, pady=3)  

btn17.grid(row=4, column=0, sticky=N+E+W+S, padx=3, pady=3)     
btn18.grid(row=4, column=1, sticky=N+E+W+S, padx=3, pady=3)  
btn19.grid(row=4, column=2, sticky=N+E+W+S, padx=3, pady=3)     
btn20.grid(row=4, column=3, rowspan=2, sticky=N+E+W+S, padx=3, pady=3)  

btn21.grid(row=5, column=0, columnspan=2, sticky=N+E+W+S, padx=3, pady=3)     
btn22.grid(row=5, column=2, sticky=N+E+W+S, padx=3, pady=3)  



#각 함수에 맞는 이미지가 같이 사용됨. waring노랑이 err빨강이
root.mainloop()
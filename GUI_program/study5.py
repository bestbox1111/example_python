from tkinter import *


#### 전체 컨셉 = 체크 박스
root = Tk()
root.title("킹왕짱스 프로그램")     #프로그램 창의 이름
root.geometry("640x480+100+200")    #프로그램의 넓이,높이,x좌표,y좌표


checkvar=IntVar()
checkbox= Checkbutton(root, text="오늘 하루보지 않기", variable=checkvar)
checkbox.select()   #자동 선택 처리
checkbox.pack()



def btncmd():
    print(checkvar.get())       #체크가 되었을때는 1로 리턴, 체크가 안되었을때는 0으로리턴
    
btn=Button(root, text="클릭",command=btncmd)        #command의 함수만들시 반드시 함수는 command란 보다 위에서 선언해야 얘가 찾을수 잇음
btn.pack()

    
    
root.mainloop()
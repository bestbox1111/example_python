from tkinter import *


#### 전체 컨셉은 텍스트 엔트리 글자 입력할수 있는 텍스트area
root = Tk()
root.title("킹왕짱스 프로그램")     #프로그램 창의 이름
root.geometry("640x480+100+200")    #프로그램의 넓이,높이,x좌표,y좌표


txt= Text(root, width=30, height=5) #줄 너비와 라인을 정해줘서 엔터로 다음줄 넘어갈수있음
txt.pack()

txt.insert(END,"글자를 입력하세요") # 힌트같은 문구임.

e = Entry(root, width=30)   # 한줄로만 표기되어서 엔터로 줄넘김이 안됨.
e.pack()
e.insert(0,"한줄만 입력요망")


def btncmd():
    print(txt.get("1.0",END))   #txt.get(txt변수를 가져오는데)  (1,0,END) 첫번째 라인의 0번쨰 컬럼부터   END마지막까지 글자를 가져오너라
    print(e.get())   #엔트리는 e.get()으로만 호출하면끝

    txt.delete("1.0",END)   #지우는 인자는 동일함
    e.delete(0,END)         #지우는 인자는 동일함. 두번쨰 인자에 END로.


btn=Button(root, text="클릭",command=btncmd)        #command의 함수만들시 반드시 함수는 command란 보다 위에서 선언해야 얘가 찾을수 잇음
btn.pack()

    
    
root.mainloop()
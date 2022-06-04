from tkinter import *
import tkinter.ttk as ttk
import time

#### 전체 컨셉 = 프로그래스 바
root = Tk()
root.title("킹왕짱스 프로그램")     #프로그램 창의 이름
root.geometry("640x480+100+200")    #프로그램의 넓이,높이,x좌표,y좌표


label =Label(root, text="메뉴를 선택하시오")
label.pack()

progressbar = ttk.Progressbar(root, maximum=100, mode="indeterminate")  #maximum=100의 수치 , 
#  mode="indeterminate"언제 끝날지 모르는 작업..로딩할때 보이는 그런거.
#  mode ="determinate" 확실하게 진행되는 음직임
progressbar.start(10)   #1초마다 음직임
progressbar.pack()


p_var2=DoubleVar()
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)  #maximum=100의 수치 , 
progressbar2.pack()


def btncmd():
    # print(progressbar.get())
    # print(p_var2.get())
    for i in range(1,101):
        time.sleep(0.01)
        p_var2.set(i)
        progressbar2.update()
        print(p_var2.get())
        
        # 아래와 같이 조건을 주어 완료 진행 상황을 공지할수있음
        if i == 60:
            print("절반 이상완료되었습니다.")
        elif i == 80:
            print("거의 완료되었습니다.")
    
    
btn=Button(root, text="선택",command=btncmd)        #command의 함수만들시 반드시 함수는 command란 보다 위에서 선언해야 얘가 찾을수 잇음
btn.pack()

    
    
root.mainloop()
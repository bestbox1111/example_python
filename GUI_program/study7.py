from tkinter import *
import tkinter.ttk as ttk

#### 전체 컨셉 = 콤보박스
root = Tk()
root.title("킹왕짱스 프로그램")     #프로그램 창의 이름
root.geometry("640x480+100+200")    #프로그램의 넓이,높이,x좌표,y좌표


label =Label(root, text="메뉴를 선택하시오")
label.pack()



values=[str(i) +"일" for i in range(1,32)]
# 일반 for 문이지만 한줄 for문으로  for i in range(1,31)을 한 애를 i라는 변수에 넣어준후 +"일"을 해준 값을 values에 넣어준 구문

#콤보박스=== 셀렉트박스
combobox= ttk.Combobox(root, height=5, values=values)   # 이상태로 실행하면 콤보박스에 글자입력하면 글자입력이 됨
combobox.pack()
combobox.set("카드 결제일")     #콤보박스에 비어있는 줄에 웹상에서 힌트라고보면됨

combobox2=ttk.Combobox(root, height=0, values=values, state="readonly")         #height= 클릭시 보여지는 라인 0개는 모두. state="readonly는 말그대로 읽기만할수이씀"
combobox2.current(0)            #첫번째 인덱스값 선택이니 1일이 선택됨.
combobox.set("카드 결제일")     #콤보박스에 비어있는 줄에 웹상에서 힌트라고보면됨

combobox2.pack()





def btncmd():
    print(combobox.get())
    print(combobox2.get())

btn=Button(root, text="선택",command=btncmd)        #command의 함수만들시 반드시 함수는 command란 보다 위에서 선언해야 얘가 찾을수 잇음
btn.pack()

    
    
root.mainloop()
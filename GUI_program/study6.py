from tkinter import *


#### 전체 컨셉 = 라디오 버튼
root = Tk()
root.title("킹왕짱스 프로그램")     #프로그램 창의 이름
root.geometry("640x480+100+200")    #프로그램의 넓이,높이,x좌표,y좌표


label =Label(root, text="메뉴를 선택하시오")
label.pack()


#햄버거를 주문하는 라디오버튼
burder_Var= IntVar()            #IntVar()를 이용하요 해당변수에 인트형으로 해당값을 담는다.
btn_burger1=Radiobutton(root,text="햄보거", value=1, variable=burder_Var)
btn_burger2=Radiobutton(root,text="치즈햄보거", value=2, variable=burder_Var)
btn_burger3=Radiobutton(root,text="치킨햄보거", value=3, variable=burder_Var)
btn_burger4=Radiobutton(root,text="불고기햄보거", value=4, variable=burder_Var)

btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()
btn_burger4.pack()

#음료를 주문하는 라디오 버튼
label =Label(root, text="음료를 선택하시오")
label.pack()

drink_var= StringVar()            #IntVar()를 이용하요 해당변수에 인트형으로 해당값을 담는다.
btn_drink1=Radiobutton(root,text="콜라", value="콜라", variable=drink_var)
btn_drink1.select()         #t셀렉트를 지정해 놓지 않으면 4개가 다 선택되는 그지같은 경우 생김.
btn_drink2=Radiobutton(root,text="사이다", value="사이다", variable=drink_var)
btn_drink3=Radiobutton(root,text="스프리츠", value="스프리츠", variable=drink_var)
btn_drink4=Radiobutton(root,text="에이드", value="에이드", variable=drink_var)

btn_drink1.pack()
btn_drink2.pack()
btn_drink3.pack()
btn_drink4.pack()



def btncmd():
    print(burder_Var.get())   
    print(drink_var.get())   


btn=Button(root, text="클릭",command=btncmd)        #command의 함수만들시 반드시 함수는 command란 보다 위에서 선언해야 얘가 찾을수 잇음
btn.pack()

    
    
root.mainloop()
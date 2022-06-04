

from tkinter import *


#전체 컨셉은 프로그램 창 만들기 및 사이즈

root = Tk()
root.title("킹왕짱스 프로그램")     #프로그램 창의 이름
root.geometry("640x480+100+200")    #프로그램의 넓이,높이,x좌표,y좌표

# root.resizable(True,False)      #v프로그램 사이즈(x좌표는 드래그로 수정가능,y좌표는 수정불가능)
# root.resizable(False,False)      #v프로그램 사이즈(x좌표는 드래그로 수정불가능,y좌표는 수정불가능)


#전체 컨셉은 버튼

btn1= Button(root, text="버튼1")    #버튼 함수 정의하고 Button()에 root를 담고
btn1.pack()     #pack으로 실행시켜주면됨


btn2= Button(root,padx=5, pady=10 ,text="버튼2")    #padx와 pady 는 버튼 안에 글자와의 패딩값
btn2.pack()     #pack으로 실행시켜주면됨

btn3= Button(root,padx=10, pady=5 ,text="버튼3")     #pady와 padx 는 버튼 안에 글자와의 패딩값
btn3.pack()     #pack으로 실행시켜주면됨


btn4= Button(root,padx=10, pady=5 ,text="버튼4akakakakaka4")     #버튼안에 글자가 많아지면 버튼이 유연하게 변경됨
btn4.pack()  

btn5= Button(root,width=10,height=3,text="버튼gsgsgsgsgs5")     #버튼의 글자가 많아지더라도 아예 버튼의 사이즈를 먼저세팅해놈.
btn5.pack()  

btn6= Button(root,width=10,height=3,text="버튼6", bg="red")     #버튼의 글자가 많아지더라도 아예 버튼의 사이즈를 먼저세팅해놈.
btn6.pack()  

photo =PhotoImage(file="GUI_program\img.png")   
btn7= Button(root,image=photo)  #버튼 속성에 이미지를 주면 넓이,길이가 이미지에서 처리한 애로 나옴
btn7.pack()  

def btncmd():
    print("버튼이 클릭됐어요")

btn8= Button(root,text="동작버튼",command=btncmd)  #버튼 속성에 command는  버튼에 대한 행위= 즉 실행 함수 처리 하는 명령어임.
btn8.pack()  


root.mainloop()     # 창이 닫히지 않게 해줌.  - 윈도우 창 -

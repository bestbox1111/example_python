

from tkinter import *

root = Tk()

root.title("킹왕짱's 프로그래밍")
root.geometry("640x480+300+100")    #프로그램의 넓이,높이,x좌표,y좌표

#### 전체 컨셉은 레이블

label1 =Label(root, text="안녕하세요")  #메인 프로그램안에 글자 넣어주는 작업
label1.pack()   


photo =PhotoImage(file="GUI_program\\img.png")  
label2 =Label(root, image=photo)   #글자 넣어주는 거와 동일하게 메인 프로그램에 이미지 넣어주는작업
label2.pack()   


def change():                           #btn  버튼 클릭했을때 label1의 text가 변경되는 함수
    label1.config(text="방가방가")      #confing()실행후, 안에 변경 텍스트입력
    
    
    global photo2       #함수끝난후 이미지 소멸되는거 막기위해  전역변수로 선언
    photo2 =PhotoImage(file="GUI_program\\x.png")  
  
    # 일반적으로 클릭하면 이미지2가 사라지는데 이유는 가비지 컬렉터로 메모리 관리하는 놈이 지역변수로 선언된놈이라 함수끝나면 지움.
    #따라서 전역변수로 선언
    label2.config(image=photo2)
    
    
    
    
    
btn= Button(root, text="click", command=change)     
btn.pack()


root.mainloop()
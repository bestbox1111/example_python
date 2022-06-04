from tkinter import *


#### 전체 컨셉은 텍스트 엔트리 글자 입력할수 있는 텍스트area
root = Tk()
root.title("킹왕짱스 프로그램")     #프로그램 창의 이름
root.geometry("640x480+100+200")    #프로그램의 넓이,높이,x좌표,y좌표


listbox= Listbox(root,selectmode="extended", height=0)  #extended는 쉬프트 누르면 여러개 선택가능
listbox.insert(0,"사과")    #인서트 첫번째 인자는 인덱스개념, 두번째는 내용
listbox.insert(1,"바나나")
listbox.insert(2,"망고")
listbox.insert(END,"딸기")  # END면 맨마지막에 알아서 들어감.
listbox.insert(END,"수박")  # END면 맨마지막에 알아서 들어감.
listbox.pack()


listbox2= Listbox(root,selectmode="single", height=3)   #single같은 경우 하나만 선택할수있음        height 0일겨우는 해당리스트 전부보여주지만, 3이면 3개면 오픈됨
listbox2.insert(0,"사과")   
listbox2.insert(1,"바나나")
listbox2.insert(2,"망고")
listbox2.insert(END,"딸기") 
listbox2.insert(END,"수박") 
listbox2.pack()


def btncmd():
    # 삭제
    # listbox.delete(0)   #첫버째  순서대로 지워짐
    # listbox.delete(END) #맨 뒤의 순서대로 지워짐
    
    #갯수확인
    # print("리스트에는 ",listbox.size(), "개가있어요")
    
    #항목확인
    #  print("1번째 부터 3번쨰까지의 항목 :",listbox.get(0,2))        #get(시작항목, 끝항목)
    
    
    #선택된 항목확인
    print("선택된 항목은 :",listbox.curselection())    #선택된 항목이 인덱스 값으로 나옴 0,1,2 이런식으로
    
btn=Button(root, text="클릭",command=btncmd)        #command의 함수만들시 반드시 함수는 command란 보다 위에서 선언해야 얘가 찾을수 잇음
btn.pack()

    
    
root.mainloop()
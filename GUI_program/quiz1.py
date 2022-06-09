
"""tkinter 를 이용한 메모장 프로그램을 만드시오

조건
1. title: 제목없음 - window메모장     ==done
2. 메뉴:파일, 편집, 서식, 보기, 도움말      ==done
3. 실제 메뉴 구현, 파일 메뉴 내에서 열기, 저장, 끝내기 3개만 처리   ==done
3.1열기 mynote.txt 파일 내용 열어서 보여주기    == half
3.2저장 mynote.txt 파일에 현재 내용 저장하기    == half
3.3끝내기: 프로그램 종료        ==done
4. 프로그램 시작시 본문은 비어있는 상태     ==done
5. 하단 status 바는 필요 없음
6.프로그램 크기, 위치는 자유롭게 하되 크기 조정 가능해야함  ==done
7. 본문 우측에 상하 스크롤바 넣기
"""

import pickle
import profile
import os   # 파일 여부 확인 위해
from tkinter import *
import tkinter.ttk as ttk


#전체 컨셉은 프로그램 창 만들기 및 사이즈

root = Tk()
root.title("windows 메모장")     #프로그램 창의 이름
root.geometry("640x480+100+200")    #프로그램의 넓이,높이,x좌표,y좌표

root.resizable(True,True)      #v프로그램 사이즈(x,y좌표는 드래그로 수정가능)
   

menu= Menu(root)  


#열기. 저장 파일 이름
filename= "mynote.txt"



def open_file():
    if os.path.isfile(filename):    # 해당 파일이 있으면 
        with open(filename, "r", encoding="utf8") as file:
            txt.delete("1.0",END)   #이구문 없으면 기존에 있던 글이 계속 추가됨.
            txt.insert(END, file.read())

        
        
    
    
def save_file():
     with open(filename, "w", encoding="utf8") as file:
        file.write(txt.get("1.0",END))





#File 메뉴
menu_file =Menu(menu, tearoff=0)    #menu라는 애를 menu_file로 세분화 시키고
menu_file.add_command(label="열기",command=open_file )        #menu_file에 이름과 add.command로 menu_file에 넣어줄 애덜 만들어줌
menu_file.add_command(label="저장",command=save_file)
menu_file.add_separator()   #구분자 만들고
menu_file.add_command(label="Exit", command=root.quit)  
menu.add_cascade(label="파일", menu=menu_file)      #file메뉴가 생겼고 file메뉴안에 있는 내용은 menu_file로 채워짐.


#편집 메뉴( 빈값)
menu_edit=Menu(menu,tearoff=0)
menu.add_cascade(label="편집",menu=menu_edit)      #edit 메뉴 만들고 빈 깡통.

#서식 메뉴( 빈값)
menu_form=Menu(menu,tearoff=0)
menu.add_cascade(label="서식",menu=menu_form)      #서식 메뉴 만들고 빈 깡통.

#보기 메뉴( 빈값)
menu_view=Menu(menu,tearoff=0)
menu.add_cascade(label="보기",menu=menu_view)      #서식 메뉴 만들고 빈 깡통.

#서식 메뉴( 빈값)
menu_help=Menu(menu,tearoff=0)
menu.add_cascade(label="도움말",menu=menu_help)      #서식 메뉴 만들고 빈 깡통.


#스크롤바


scrolbar= Scrollbar(root)
scrolbar.pack(side="right", fill="y")    



#본문 영역

txt =Text(root, yscrollcommand=scrolbar.set)
txt.pack(fill="both", expand=True, side="left")

scrolbar.config(command=txt.yview)   

root.config(menu=menu)
root.mainloop()     #
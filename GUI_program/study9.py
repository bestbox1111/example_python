from tkinter import *
import tkinter.ttk as ttk
import time

#### 전체 컨셉 = 메뉴
root = Tk()
root.title("킹왕짱스 프로그램")     #프로그램 창의 이름
root.geometry("640x480+100+200")    #프로그램의 넓이,높이,x좌표,y좌표




def create_new_file():
    print("새로운 파일을 만급니다.")

menu= Menu(root)    #Menu라는 임포트한 애를 menu라는 변수로 변경한다.


#File 메뉴
menu_file =Menu(menu, tearoff=0)    #menu라는 애를 menu_file로 세분화 시키고
menu_file.add_command(label="New File", command=create_new_file)        #menu_file에 이름과 add.command로 menu_file에 넣어줄 애덜 만들어줌
menu_file.add_command(label="New window")
menu_file.add_separator()   #구분자 만들고
menu_file.add_command(label="open file...")
menu_file.add_separator()
menu_file.add_command(label="save all", state="disable")
menu_file.add_separator()
menu_file.add_command(label="Exit", command=root.quit)  
menu.add_cascade(label="File", menu=menu_file)      #file메뉴가 생겼고 file메뉴안에 있는 내용은 menu_file로 채워짐.






#edit 메뉴( 빈값)
menu_edit=Menu(menu,tearoff=0)

menu_edit.add_command(label="다시실행")
menu_edit.add_command(label="실행취소")
# menu_edit.add_separator()
menu.add_cascade(label="edit" ,menu=menu_edit)      #edit메뉴 만들고 빈 깡통.



def lang():
    print(menu_lang.get())


# language 메뉴 추가 --- 라디오버튼으로
menu_lang=Menu(menu, tearoff=0)

menu_lang.add_radiobutton(label="python", command=lang)
menu_lang.add_radiobutton(label="java", command=lang)
menu_lang.add_radiobutton(label="C", command=lang)
menu.add_cascade(label="Language",menu=menu_lang)


#view  메뉴추가 ----체크박스로

menu_view=Menu(menu,tearoff=0)

menu_view.add_checkbutton(label="명령팔렛트")
menu_view.add_checkbutton(label="뷰열기")
menu_view.add_separator()
menu.add_cascade(label="보기",menu=menu_view)


root.config(menu=menu)
root.mainloop()
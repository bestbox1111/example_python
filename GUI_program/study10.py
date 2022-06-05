from tkinter import *
import tkinter.messagebox as msbox
import tkinter.ttk as ttk
import time

#### 전체 컨셉 = 메뉴
root = Tk()
root.title("킹왕짱스 프로그램")     #프로그램 창의 이름
root.geometry("640x480+100+200")    #프로그램의 넓이,높이,x좌표,y좌표


def info():
    msbox.showinfo("알림","정상적으로 예매완료")
btn=Button(root, text="버튼을 클릭",command=info)
btn.pack()



def warning():
    msbox.showwarning("경고","해당 좌석은 매진되었어요")
btn=Button(root, text="버튼을 클릭",command=warning)
btn.pack()

def err():
    msbox.showerror("에러","결제오류가 방생했어요")
btn=Button(root, text="버튼을 클릭",command=err)
btn.pack()


def okcancel():
    msbox.askokcancel("확인/ 취소","해완견 겸용좌석입니다. 예매하시겠습니까??")     #고객에게 다시 한번 ok. no에 대한 응답메세지박스 뛰움
btn=Button(root, text="버튼을 클릭",command=okcancel)
btn.pack()


def retry():
    msbox.askretrycancel("재시도/ 취소","일시적인 오류입니다. 다시 시도하시겠습니까??") #다시 한번 시도 할꺼나 취소할꺼냐에 대한 매시지 박스뛰움
btn=Button(root, text="버튼을 클릭",command=retry)
btn.pack()


def yesno():
    msbox.askyesno("예/ 아니오", "해당 좌석은 남자 전용입니다. 예메하시겠어요??") #
btn=Button(root, text="버튼을 클릭",command=yesno)
btn.pack()


def yesnocancel():
    msbox.askyesnocancel(title=None, message="예매 내역이 저장되지 않았는데 저장할까여?") #타이틀= 위에 나오는 제목같은거 massage=text와 같은 부분들임.
btn=Button(root, text="버튼을 클릭",command=yesnocancel)
btn.pack()



def yesnocancel():
    response= msbox.askyesnocancel(title=None, message="예매 내역이 저장되지 않았는데 저장할까여?") #타이틀= 위에 나오는 제목같은거 massage=text와 같은 부분들임.
    #예: 저장후 종료        True    1
    #아니오 : 저장하지 않고 종료    False   0
    #취소 : 프로그램 나가기     None    그외
    print("응답은:{}".format(response))
    if response == 1:
        print("예매를 진행하겠습니다.")
    elif response ==0:
        print("예매를 진행하지 않겠습니다.")
    else:
        print("프로그램을 종료하겠습니다.")


btn=Button(root, text="응답에 따른 반응 예제",command=yesnocancel)
btn.pack()



#각 함수에 맞는 이미지가 같이 사용됨. waring노랑이 err빨강이
root.mainloop()
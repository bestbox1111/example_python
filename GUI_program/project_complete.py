

'''여러 이미지를 합치는 프로그램을 만드시오

[사용자 시나리오]
1. 사용자는 합치려는 이미지를 1개 이상 선택한다.
2. 합쳐진 이미지가 저장될 경로를 지저안다.
3. 가로넓이, 간격, 포맷, 옵션을 지정한다.
4. 시작 버튼을 통해 이미지를 합친다.
5. 닫기 버튼을 통해 프로그램을 종료한다.

[기능 명세]
 1. 파일추가 : 리스트 박스에 파일 추가
 2. 선택 삭제 : 리스트 박스에서 선택된 항목삭제
 3. 찾아보기 : 저장 폴더를 선택하면 텍스트위젝에 입력
 4. 가로 넓이 : 이미지 넓이 지정(원본, 1024, 800, 640)
 5. 간격 : 이미지 간의 간격 지정(없음, 좁게, 보통, 넓게)
 6. 포맷 : 저장 이미지 포맷 지정(png, jpg, bmp)
 7. 시작 : 이미지 합치기 작업 실행
 8. 진행 상황 : 현제 진행중인 파일 순서에 맞게 반영
 9. 닫기 : 프로그램 종료'''
 
 
import os
from PIL import Image as im
import tkinter.messagebox as mgbox
from tkinter import *
import tkinter.ttk as ttk
from turtle import width
from tkinter import filedialog      #import *을 했지만,  서브모듈을 사용하려면 따로 임포트를 해줘야함.

# 프로그램 창 만들기 및 사이즈
root = Tk()
root.title("킹왕짱스 이미지 합치기 프로그램")     #프로그램 창의 이름
root.geometry("600x540+200+100")    #프로그램의 넓이,높이,x좌표,y좌표
root.resizable(False,False)      #v프로그램 사이즈(x좌표-y좌표는 수정불가능)


#추가파일 함수
def add_file():
    files= filedialog.askopenfilenames(title="이미지 파일을 선택하세여",filetypes=(("모든파일","*.*"),("PNG파일","*.PNG"),("JPG파일","*.jpg"),("BMP파일","*.bmp")),initialdir=r"C:\Users\park\Desktop\Rounding")
#사용자가 선택한 파일 목록
    for file in files:
        list_file.insert(END, file)


    # reverse와 reversed 의 차이
    #p =[1,2,3]   p.reverse() 는 [3,2,1]을 출력
    #p2= reversed(p)    [3,2,1]을 p2에 저장하여... list(p2)로 출력확인가능.


#삭제파일 함수
def del_file():
    # print(list_file.curselection())
    for index in reversed(list_file.curselection()):
        list_file.delete(index)
        
        
#저장 경로 함수
def browse_dest_path():
    folder_selected=filedialog.askdirectory()
    if folder_selected == '':   #사용자가 취소를 누를때
        return
    else:
       txt_dest_path.delete(0,END)
       txt_dest_path.insert(0,folder_selected)





def merger_image():
    # print(list_file.get(0,END))     #해당 이미지의 주소를 프린트에 표시하는 함수.
    # images = [Image.open(x) for x in list_file.get(0,END)]
    # # Image에는 size --> size[0]:width , size[1]: height
    
    images = [im.open(x) for x in list_file.get(0,END)]         #Image.open으로 해야 하는데 오류가 존내나서 as로 모듈이름이 겹치는거같아서 다른 이름로 바꿈.
    # widths =[x.size[0] for x in images]
    # heights =[x.size[1] for x in images]
    #zip 방식으로 위를 바꾼다면
    widths, heights = zip(*(x.size for x in images))  #위 구문을 zip으로 바꾸면 이렇게됨.
    
    
    
    
    
    # #가로 넓이 옵션부분
    img_width= cmb_width.get()
    if img_width == "원본유지":
        img_width = -1   #-1일 때는 원본 기준으로 유지.
    
    else:
        img_width = int(img_width)  #img_width에 받아서 들어있는 문자를 숫자로 형변환해서 같은 변수에저장.
    
    # 간격 옵션 부분
    img_space = cmb_space.get()
    if img_space == "좁게":
        img_space = 10
    elif img_space == "보통":
        img_space = 50
    elif img_space == "넓게":
        img_space = 100
    else:
        img_space = 0
        
    
    # #포맷 옵션 부분
    img_format = cmb_format.get().lower()   #PNG,JPG,BMP를 소문자로 변경
    
    # #이미지 사이즈 리스트에 넣어서 하나씩 처리
    image_sizes =[] #리스트 변수 만듬. width1,height1   width2,height2....순으로 리스트
    if img_width >-1:       #계산이 좀 필요ㅏㅁ
        # x = width = size[0]
        # y = height = size[1]
        # x' = img_width # 이 값으로 변경 해야함
        # y' = x'y / x    x= img_width*size[1] /size[0]
        image_sizes =[(int(img_width), int(img_width * x.size[1]/x.size[0])) for x in images ]
    else:       #원본 이미지 사용될시에는 원본 위드와 헤이드만 가져와서 반복문 돌리고 리스트에 넣어줌.
        image_sizes=[(x.size[0], x.size[1]) for x in images]
    
    
    widths, heights = zip(*(image_sizes))       #위 78~81 라인의 내용을 한줄로 변경한 부분. 
    
    # 최대 넓이, 전체 높이를 구해야함... 사진이 여러장이므로. 크기도 제각각.
    max_width, total_height = max(widths), sum(heights)   #max_widths는  입력받은 여러가지 이미지들 중에 최대너비를 뽑음,   sum(heights)는 여러이미지들의 높이의 합이 됨.여러장일테니



    if img_space >0:        #이미지 간격 옵션 적용뷰뷴
        total_height+=(img_space * (len(images)-1))


    # 스케치북
    result_img = im.new("RGB", (max_width, total_height),(255,255,255))
    y_offset =0  # y축의 위치==이미지를 쌇을수록. x축은 상관없지만 y축으로 계속 쌓여지므로.
   
    # for img in images:
    #     result_img.paste(img,(0, y_offset))
    #     y_offset+=img.size[1]       #이미지 y축으로 쌇는 건 되지만, 프로그레스바는 건드리지 못해서.아래와같이
        
        
    for idx, img in enumerate(images):    
        
        
    #     #width가 원본유지가 아닐때에는 이미지 크기 조정
        if img_width > -1:
            img=img.resize(image_sizes[idx])
        
        result_img.paste(img,(0, y_offset))
      
        y_offset+= (img.size[1] + img_space)  #  원본 크키에 맞게 변경된 크기가 추가된 y크기 
        
        
        progress =(idx +1)/len(images) *100     #실제 퍼센트 정보를 계산 //인덱스가0 부터니까 1번째 사진을 위해 +1해줌
        p_var.set(progress)
        prgress_bar.update()
      
        
        
        
        
    # 포맷 옵션 처리
    #이미지가 저장되는 경로에 file_name부분도 추가됨
    
    file_name="kingwangjjang."+ img_format 
    dest_path=os.path.join(txt_dest_path.get(), file_name) 
    
    result_img.save(dest_path)      
    mgbox.showinfo("알림","작업이 완료되었습니다.")





#시작 버튼 함수
def start():
    #각 옵션들 값을 확인
    # 넓이, 공간, 폼
    # print("가로 넓이", cmb_width.get())    
    # print("간격", cmb_space.get())  
    # print("포맷", cmb_format.get())    
    
    # 파일 목록 확인  == 파일이 없을 때에도 있으니까.. 
    if list_file.size() ==0:
        mgbox.showwarning("주의","이미지를 추가하고 사용하셔야 합니다.")
        return

    # 저장 경로 확인이 부어있으면 안되니까
    if len(txt_dest_path.get())== 0:
        mgbox.showwarning("주의","저장 경로를 설정하고 사용하셔야 합니다.")
        return
    
    
    #이미지 통합 작업   
    merger_image()
    
    
    
    
    


def close():
    pass










#파일 프레임 (파일추가, 파일삭제)
file_frame =Frame(root)  #메인 프로그램안에 글자 넣어주는 작업
file_frame.pack(fill="x",padx=5, pady=5)   
#버튼
add_file= Button(file_frame,padx=5, pady=3 ,width=15, text="파일추가",command=add_file)    #버튼 함수 정의하고 Button()에 root를 담고
add_file.pack(side="left")     #pack으로 실행시켜주면됨
del_file= Button(file_frame,padx=5, pady=3 ,width=15,text="파일삭제",command=del_file)    #padx와 pady 는 버튼 안에 글자와의 패딩값
del_file.pack(side="right")     #pack으로 실행시켜주면됨




#리스트 프레임
list_frame=Frame(root)
list_frame.pack(fill="both",padx=5)
#스크롤바
scrollbar= Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")
#리스트목록부분
list_file=Listbox(list_frame, selectmode="extended", height=15, yscrollcommand=scrollbar.set)
list_file.pack(side="left", fill="both", expand=True)
scrollbar.config(command=list_file.yview)







#저장 경로 프레임
path_frame= LabelFrame(root, text="저장경로")
path_frame.pack(fill="x",padx=5, pady=5)
#저장경로 입 출력란.
txt_dest_path= Entry(path_frame)
txt_dest_path.pack(side="left",fill="x",padx=5, expand=True, ipady=4)  #ipady = 엔트리 영역이 조금 높아짐.
#저장 경로 버튼
btn_dest_path= Button(path_frame,text="찾아보기", width=10,command=browse_dest_path)
btn_dest_path.pack(side="right",padx=3)




#옵션 프레임    (가로넓이, 간격, 파일포맷)
frame_option =LabelFrame(root,text="옵션")
frame_option.pack(fill="x",padx=5, pady=5)
#가로넓이레이블
lbl_width= Label(frame_option, text="가로넓이",width=10, padx=5, pady=10, height=1)
lbl_width.pack(side="left",padx=3, pady=3)
#가로넓이콤보박스=셀렉트박스
option_width=["원본유지","1024","800","640"]
cmb_width=ttk.Combobox(frame_option,state="readonly", values=option_width, width=10)
cmb_width.current(0)
cmb_width.pack(side="left",padx=3, pady=3)

#간격레이블
lbl_space= Label(frame_option, text="간격",width=10, padx=5, pady=10)
lbl_space.pack(side="left",padx=3, pady=3)
#간격콤보박스-셀렉트박스
option_space=["좁게","보통","넓게"]
cmb_space=ttk.Combobox(frame_option,state="readonly", values=option_space, width=10)
cmb_space.current(0)
cmb_space.pack(side="left",padx=3, pady=3)

#파일포맷레이블
lbl_format= Label(frame_option, text="포맷",width=10, padx=5, pady=10)
lbl_format.pack(side="left",padx=5, pady=5, ipady=5)
#파일포맷옵션콤보박스-셀렉트박스
option_format=["PNG","JPG","JPEG","BMP"]
cmb_format=ttk.Combobox(frame_option,state="readonly", values=option_format, width=10)
cmb_format.current(0)
cmb_format.pack(side="left",padx=5, pady=5)



#진행 상황 progressbar
frame_progress = LabelFrame(root, text="진행상황")
frame_progress.pack(fill="x",padx=3, pady=3)
p_var=  DoubleVar()
prgress_bar= ttk.Progressbar(frame_progress, maximum=100, variable=p_var)
prgress_bar.pack(fill="x",padx=5, pady=5)



#실행 프레임(시작버튼과, 클로즈버튼)
#실행프레임
frame_run =Frame(root)
frame_run.pack(fill="x",padx=3, pady=3)
#클로즈버튼
btn_close=Button(frame_run, text="끝내기", padx=5, pady=5, width=15, command= root.quit)
btn_close.pack(side='right',padx=3, pady=3)
#시작버튼
btn_start=Button(frame_run, text="시작", padx=5, pady=5, width=15,command=start)
btn_start.pack(side='right',padx=3, pady=3)




root.mainloop()     # 창이 닫히지 않게 해줌.  - 윈도우 창 -

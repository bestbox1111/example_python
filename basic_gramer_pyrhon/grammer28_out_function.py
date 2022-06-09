


#list of python modules 검색란에 
#### 외장함수 ####


# glob :경로내의 폴더 / 파일 목록 조회 (윈도우 dir)
# import glob
# print(glob.glob("*.xlsx"))  #확장자가 xlsx인 모든 파일찾아줌





# os :운영체제에서 제공하는 기본 기능
# import os
# print(os.getcwd())  #현제 디렉토리 경로
# folder="sample_dir"
# if os.path.exists(folder):
#     print(folder+" 경로가 존재합니다.")
#     os.rmdir(folder)
#     print(folder,"폴더를 삭제했어여")
# else:
#     os.makedirs(folder) #폴더를 만드는 명령어
#     print(folder + "폴더를 생성하였습니다.")
    
    
    
# import time
# print(time.localtime()) #현제 시간을 기계적인 표기법으로
# print(time.strftime("%Y년 %m월 %d일 %H시 %M분 %S초"))   #사람이 보기좋게 설정해서 표기함


import datetime
print("오늘 날짜는", datetime.date.today())


today= datetime.date.today()
td= datetime.timedelta(days=100)

print("우리가 만난지 100일은",td+today,"입니다")
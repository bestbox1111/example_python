#파일 한번에 100개 만들기 처리 하기

import os , sys

# # print(os.getcwd())

os.mkdir('my_dir')     #디렉토리 만들기

os.chdir(".\my_dir")        #디렉토리 변경(이동)
# print(os.getcwd())          #현제 디텍토리 확인.

for i in range(100):        #파일 100개 for 문으로 만들기.
    f= open('file'+str(i),'w',encoding='utf8')
    f.close()
    

first= os.listdir('.')  #현제있는 디렉토리 파일들을 받아오는거


#파일이름 변경.. 기존파일에 약간의 기준으로 변경함.
for fid in first:
    f_name=fid[0:4]
    f_num=fid[4::]
    
    if int(f_num)<50:
        os.replace(fid,'2019_' +fid)
    else:
        os.replace(fid,'2022_' +fid)
        
        
os.mkdir('2019_data')
os.mkdir('2022_data')


first= os.listdir('.')  #현제있는 디렉토리 파일들을 받아오는거


#2019년끼리 같이 묶고 싶지만...디렉토리 까지 같이 묶여버림.

#filter를 사용

from itertools import compress

idx= list(map(lambda x: "file" in x, first))        #file 이란 이름이 들어간 애만 idx에 저장함.

# flist2=compress(flist, idx)     #compress로 flist로 묶은후그걸 다시 아래와같이 list화

flist2= list(compress(first,idx))
# print(flist2)







# os.chdir(".\my_dir")        #디렉토리 변경(이동)
# first= os.listdir('.')  #현제있는 디렉토리 파일들을 받아오는거from itertools import compress
# idx= list(map(lambda x: "file" in x, first))        #file 이란 이름이 들어간 애만 idx에 저장함.
# # flist2=compress(flist, idx)     #compress로 flist로 묶은후그걸 다시 아래와같이 list화
# flist2= list(compress(first,idx))

#flist2 =[x for x in flist if 'file' in x]  위와 같은 방법임..
# print(flist2)


# import glob
# os.chdir(".\my_dir")        #디렉토리 변경(이동)
# os.listdir('.')  #현제있는 디렉토리 파일들을 받아오는거
# print(glob.glob('*2019*'))


#파일 이동시 필요한 모듈
import shutil

for f_cur in flist2:
    f_name=f_cur[0:9]
    f_num=f_cur[9::]
    if int(f_num)<50:
        shutil.move(f_cur, '.\\2019_data')
    else:
        shutil.move(f_cur, '.\\2022_data')
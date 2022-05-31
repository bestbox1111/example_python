import pyautogui    #임포트 전에 인스톨 먼저해야함 pip install pyautogui 터미널창에서

#전체 컨셉 = 화면 크기알아보기

# size =pyautogui.size()  #현제 화면의 스크린 사이즈를 가져옴
# print(size)     #가로, 세로 크기를 알수 있음


# #전체 컨셉 = 마우스 이동

# pyautogui.moveTo(100,100, duration=2)   #지정한 위치로 마우스를 이동 duration="이동하는 시간"
# print(pyautogui.position()) #현제 좌표위치 확인

# pyautogui.move(100,100) #현제 위치에서 x=100 y=100으로 이동
# print(pyautogui.position())
#moveto와  moveTo의 차이는 이동시 절대좌표와 현제좌표의 차이임.



#전체 컨셉 = 마우스 관련 조작

# pyautogui.sleep(2)
# print(pyautogui.position())

# pyautogui.click(1099,13,  duration=2)   # 원하는 좌펴 입력후 마우스 클릭


# pyautogui.mouseDown()   # 마우스를 눌렸을때...(예를들면 드래고 같은 작업)
# pyautogui.mouseUp()     # 마우스를 뛰었을때 ..(클릭과 비슷한 맥락임.)


# pyautogui.click(clicks=2)   # 마우스 클릭의 횟수를 조절가능함.


#   100,100에서 마우스 클릭후 300,300에 마우스뛰는거 아이콘 이동같은작업.
# pyautogui.moveTo(100,100)
# pyautogui.mouseDown()
# pyautogui.moveTo(300,300)
# pyautogui.mouseUp()

# pyautogui.rightClick()  #a마우스 우클릭
# pyautogui.middleClick() #마우스 휠 클릭



# 포지션값 확인전에 먼저 2초쉬어줌.
# pyautogui.sleep(2)
# print(pyautogui.position())
# pyautogui.moveTo(623,466)
# pyautogui.drag(299,0,duration=0.2)  #정해진 좌표에 있는 아이콘을 정한 좌표만큼 이동


# pyautogui.sleep(2)
# print(pyautogui.position())
# pyautogui.moveTo(623,466)
# pyautogui.dragTo(800,800,duration=0.2)  #정해진 좌표에 있는 아이콘을 정한 절대좌표로 이동


#마우스스크롤
# pyautogui.scroll(300)   #   -면 아래로 +면 위로 이동하기/.
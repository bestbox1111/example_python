import pyautogui    #임포트 전에 인스톨 먼저해야함 pip install pyautogui 터미널창에서


# 전체 컨셉은 마우스 인포라는 툴

# pyautogui.mouseInfo()   #마우스 인포 현제좌표 위치의 색상 등 확인가능.


# 전체 컨셉은 스크린 샷
# img = pyautogui.screenshot()
# img.save("auto2.png")       #스크린샷 저징

# 전체 컨셉은 pixel 



# pyautogui.pixelMatchesColor(100,100,(58))
# 1549,596 30,30,30 #1E1E1E

pixel =pyautogui.pixel(1549,596)    #원하는 좌표를 pixel에 넣으면
print(pixel) #하게되면 해당 좌표의 픽셀값이 나옴.mouseinfo rgb의 값과 동일함.(30, 30, 30)

print(pyautogui.pixelMatchesColor(1549,596,(30,30,30))) #좌표를 비교하여 픽셀값을 비교하여 블리언으로 출력해줌.


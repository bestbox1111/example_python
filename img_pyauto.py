from PIL import Image

import pyautogui



# pyautogui.moveto(100,100)을 한후, 클릭사용안해도 아래와 같이 한방에사용가능
# pyautogui.click(100, 100)



locateOnScreen 같은 경우 좌표를 매번확인 할수 없을 경우 이미지로 저장하여
그이미지를 찾으라는 의미임 (좌,우,이미지넓이, 이미지 높이나옴)
i=pyautogui.locateOnScreen('nn.png')
q= pyautogui.center(i)
pyautogui.click()



# 보충필요함....이해안됨.....부족.
# pyautogui.screenshot('1.png', region=(110,750,30,30))
# num = pyautogui.locateCenterOnScreen('nn.png')
# pyautogui.click(num, clicks=2)




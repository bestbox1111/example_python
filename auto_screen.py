from PIL import ImageGrab
import time
import keyboard

## 스크린 이미지를 자동 저장하는 프로그램

time.sleep(5)
for i in range(1,11):       #2초 간격으로 10개 이미지 저장
    auto_img = ImageGrab.grab()  # 현제 스크린 이미지를 가져옴
    auto_img.save("auto_image{}.png".format(i)) #파일로 저장됨.
    time.sleep(5)   #2초 간격임.





# def screenshot():
#     cur_time= time.strftime("%Y%M%d_%S")
#     img = ImageGrab.grab()
#     img.save("hot{}.png".format(cur_time))

# keyboard.add_hotkey("F9",screenshot)

# keyboard.wait("esc")

# screenshot()
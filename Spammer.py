import pyautogui
import time

time.sleep(5)

text = "REEEEEEEEEEEE"

for i in range(0,100):
    
    pyautogui.typewrite(text)
    pyautogui.press('enter')

#on linux, add $xhost + for correct run
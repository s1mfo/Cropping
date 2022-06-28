# pynput 이란 키보드와 마우스를 제어할 수 있는 파이썬 라이브러리.
# Listener 등록을 통해 키보드와 마우스로부터 들어오는 값을 가져올 수 있다.
from pynput.mouse import Listener
import keyboard
from PIL import Image
import pyautogui
import os


coord = []

# saving screenshot image to D drive
myScreenshot = pyautogui.screenshot()
myScreenshot.save('D:/myscreenshot.jpg')


im = Image.open(r'D:/myscreenshot.jpg')

# getting mouse coordinates when mouse click.
def click(x,y,buton,pressed):
    if pressed:
        x = int(x)
        y = int(y)
        coord.append(x)
        coord.append(y)

        if len(coord) == 4:
            return False

with Listener(on_click = click) as Listener:
    Listener.join()

left = coord[0]
top = coord[1]
right = coord[2]
bottom = coord[3]

im1 = im.crop((left,top,right,bottom))

os.remove('D:/myscreenshot.jpg')
os.startfile('D:/')
im1.show()
im1.save('D:/cropped.jpg')




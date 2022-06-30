import pyautogui
import tkinter as tk
from pynput.mouse import Listener
import keyboard
from PIL import Image
import os

def cropping(event):   
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
    with Listener(on_click = click) as listener:
        listener.join()
        
    left = coord[0]
    top = coord[1]
    right = coord[2]
    bottom = coord[3]
    im1 = im.crop((left,top,right,bottom))
    os.remove('D:/myscreenshot.jpg')
    os.startfile('D:/')
    im1.show()
    im1.save('D:/cropped.jpg')

root = tk.Tk()
root.title('BetterWork')
canvas1 = tk.Canvas(root, width = 400, height = 100)
canvas1.pack()

def crop():
    if onButton['text'] == 'OFF':
        onButton['text'] = 'ON'
        onButton['bg'] = 'blue'
        root.bind('<Shift-Z>', cropping)
    else:
        root.unbind('<Shift-Z>')
        onButton['text'] = 'OFF'
        onButton['bg'] = 'red'
        
onButton = tk.Button(text = 'OFF', command = crop, bg='red', fg='white', font=15, width=25)
canvas1.create_window(200, 50, window = onButton)

root.mainloop()
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
import numpy as np
import pyautogui as pg
import time
import random
import PIL
from PIL import Image
import keyboard
import os

root = Tk()
root.title('Draw Automation')
root.geometry('400x500')


def accept_image_method():
    img_file = askopenfilename(initialdir="/", title="Select file",
                               filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
    Label(root, text=img_file).place(x=80, y=20)

    main_img = Image.open(img_file)

    convert_bw = main_img.convert('1')
    convert_bw.save('temp_bw_img.jpg')

    main_bw_img = Image.open('temp_bw_img.jpg')
    main_bw_img = PIL.Image.Image.rotate(main_bw_img, 90, expand=1)

    bw_img_array = np.array(main_bw_img, dtype=int)

    search_zero = np.argwhere(bw_img_array == 0)

    main_array = []

    for i in range(len(search_zero)):
        temp_var = [(search_zero[i][0] + 30), (search_zero[i][1] + 300)]
        main_array.append(temp_var)

    random.shuffle(main_array)

    name_after_draw = name.get()

    os.startfile('C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Accessories/Paint.lnk')
    time.sleep(10)

    for j in main_array:
        pg.click(j)

    time.sleep(5)

    keyboard.press_and_release('ctrl + s')

    time.sleep(5)

    keyboard.write(name_after_draw)

    keyboard.press_and_release('return')

    time.sleep(5)

    os.remove(main_bw_img)

    os.system('TASKKILL /F /IM mspaint.exe')

    messagebox.showinfo(title='Draw Automation', message='Your File has been save!')


name = StringVar()
Label(root, text='Save File Name : ').place(x=10, y=20)
Entry(root, textvariable=name).place(x=150, y=20)
accept_image = Button(root, text='Select File', command=accept_image_method).place(x=10, y=50)

root.mainloop()

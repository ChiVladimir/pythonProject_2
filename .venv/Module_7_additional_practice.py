# Дополнительная практика по модулю 7

import tkinter
from fileinput import filename
from tkinter import font
from tkinter import filedialog
import os
import subprocess

def file_select():
    filename = filedialog.askopenfilename(initialdir = "/", title = "Выберите файл",
                                          filetypes =(('Текстовый файл', '.txt'), ('Все файлы', '*')))
    text['text'] = text['text'] + '' + filename
#    os.startfile(filename)

    subprocess.call(["open", filename])  # для MacOS


window = tkinter.Tk()
window.title('Проводник')
window.geometry('450x150')
window.configure(bg='deep sky blue')
font1 = font.Font(family= "Arial", size=14, weight="bold", slant="roman")
font2 = font.Font(family= "Verdana", size=12, weight="bold", slant="roman")
window.resizable(True, False)
text = tkinter.Label(window,
                     text='Файл: ',
                     width=55,
                     height=5,
                     fg='blue2',
                     background='light steel blue',
                     font=font1)
text.grid(column=1, row=1)
button_select = tkinter.Button(window,
                               text='Выбрать файл',
                               width=16,
                               height=3,
                               fg='blue2',
                               background='sky blue',
                               font=font1,
                               command=file_select)
button_select.grid(column = 1, row = 2, pady = 5)
window.mainloop()


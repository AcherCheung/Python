# !/usr/bin/env python
# -*- coding: utf-8 -*-
import tkinter
from tkinter import *
from tkinter.filedialog import askopenfilename, askdirectory
import tkinter.messagebox

frameT = Tk()
frameT.geometry('500x200+400+200')
frameT.title('选择需要输入处理的文件')
frame = Frame(frameT)
frame.pack(padx=10, pady=10)  # 设置外边距
frame_1 = Frame(frameT)
frame_1.pack(padx=10, pady=10)  # 设置外边距
frame1 = Frame(frameT)
frame1.pack(padx=10, pady=10)
v = StringVar()

ent = Entry(frame, width=50, textvariable=v).pack(fill=X, side=LEFT)  # x方向填充,靠左



def fileopen():
    file_sql = askdirectory()
    if file_sql:
        file_sql = eval(repr(file_sql).replace('/', '\\'))
        v.set(file_sql)


def match():
    print(v.get())
    tkinter.messagebox.showinfo(title='None', message='done！please check watermark folder')

btn = Button(frame, width=20, text='总文件', font=("宋体", 14), command=fileopen).pack(fil=X, padx=10)
ext = Button(frame1, width=10, text='运行', font=("宋体", 14), command=match).pack(fill=X, side=LEFT)
etb = Button(frame1, width=10, text='退出', font=("宋体", 14), command=frameT.quit).pack(fill=Y, padx=10)
frameT.mainloop()

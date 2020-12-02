from pymouse import *
from pykeyboard import *
import time
import win32clipboard as w
import win32con
import win32api
import win32clipboard
import os
from os.path import join, getsize
import _thread
import tkinter
from tkinter import *

isRuning = False

def main():
    CreateWindow()

def CreateWindow():
    def begin():
        space =float(input.get())
        global isRuning
        if isRuning == False:
            _thread.start_new_thread(do_auto_write, (space,))
        isRuning = True

    def pause():
        global isRuning
        isRuning = False

    def Cancel():
        global isRuning
        isRuning = False
        top.destroy()
    top = tkinter.Tk()
    top.title("自动祝福")
    top.geometry("300x150")
    tips = Text(top,width = 300, height = 1)
    tips.insert(END,'输入语句可在config.txt中修改')
    confirm = Button(top,text ="开始",command = begin)
    pause = Button(top,text ="暂停",command = pause)
    cancel = Button(top,text ="结束",command = Cancel)
    tips2 = Text(top, width=300, height=1)
    tips2.insert(END, '输入间隔（秒）：')
    input = Entry(top)
    tips.pack()
    tips2.pack()
    input.pack()
    confirm.pack()
    pause.pack()
    cancel.pack()
    top.mainloop()

def do_auto_write( space ):
    global isRuning
    lines = copy_from_file("config.txt")
    while isRuning == True:
            for line in lines:
                if isRuning == False:
                    break
                time.sleep(space);
                copy_txt(line.replace('\n',''))
                pasteToOther();
    isRuning = False

def copy_txt( aString ):
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardData(win32clipboard.CF_UNICODETEXT,aString)
    w.CloseClipboard()

def copy_from_file( aString ):
    fo = open(aString,encoding='utf-8')
    linesToReturn = fo.readlines()
    fo.close()
    return linesToReturn

def pasteToOther():
    win32api.keybd_event(17, 0, 0, 0)  # ctrl的键位码是17
    win32api.keybd_event(86, 0, 0, 0)  # v的键位码是86
    win32api.keybd_event(86, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键
    win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)
    win32api.keybd_event(13, 0, 0, 0)  # Enter的键位码是13
    win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)

if __name__ == '__main__':
    main()
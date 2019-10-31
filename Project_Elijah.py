from tkinter import *
import tkinter
import webbrowser
chrome_path = "C:\\Program Files (x86\\Google\\Chrome\\Application\\chrome.exe"
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
window = tkinter.Tk()
window.title("beans")
window.geometry('500x300')
frame = Frame(window)
bottomframe = Frame(window)
bottomframe.pack(side=BOTTOM)

def callback1():
    webbrowser.open('http://www.google.com', new=2)
btn1 = tkinter.Button(window, text="test", command=callback1)
btn1.pack(side='bottom')

def callback2():
    webbrowser.open('https://drive.google.com/drive/u/0/my-drive', new=2)
btn2 = tkinter.Button(window, text="come on", command = callback2)
btn2.pack(side='top')

def callback3():
    webbrowser.open('https://drive.google.com/drive/u/0/my-drive', new=2)
btn3 = tkinter.Button(window, text="come on", command = callback3)
btn3.pack(side='left')

def callback4():
    webbrowser.open('https://drive.google.com/drive/u/0/my-drive', new=2)
btn4 = tkinter.Button(window, text="come on", command = callback4)
btn4.pack(side='right')

def callback5():
    webbrowser.open('https://drive.google.com/drive/u/0/my-drive', new=2)
btn5 = tkinter.Button(window, text="come on", command = callback5)
btn5.pack(side='top')

def callback6():
    webbrowser.open('https://drive.google.com/drive/u/0/my-drive', new=2)
btn6 = tkinter.Button(window, text="come on", command = callback6)
btn6.pack(side='top')
window.mainloop()
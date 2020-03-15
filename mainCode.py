#import module from tkinter for UI
from tkinter import *
import os
import subprocess
from datetime import datetime;
#creating instance of TK
root=Tk()

root.configure(background="#DFDFDF")

# root.geometry("300x300")

def function1():
    os.system("python3 detectSigns.py")
    
def function2():
    os.system("python3 detectWord.py")

def function3():
    root.destroy()

#stting title for the window
root.title("Sign To Text Converter")

#creating a text label
Label(root, text="SignText",font=("times new roman",20),fg="white",bg="#e51a4c",height=3).grid(row=0,rowspan=2,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#creating first button
Button(root,text="Detect Symbol",font=("times new roman",20),bg="#ffffff",fg='black',command=function1).grid(row=3,columnspan=2,sticky=W+E+N+S,padx=10,pady=10)

#creating second button
Button(root,text="Detect Word",font=("times new roman",20),bg="#ffffff",fg="#000000",command=function2).grid(row=4,columnspan=2,sticky=N+E+W+S,padx=10,pady=10)

#creating ninth button              
Button(root,text="Exit",font=('times new roman',20),bg="#e51a4c",fg="white",command=function3).grid(row=12,columnspan=2,sticky=N+E+W+S,padx=10,pady=10)


root.mainloop()

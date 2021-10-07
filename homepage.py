# -*- coding: utf-8 -*-
"""
Created on Fri Oct 9 20:39:40 2020

@author: Adrak
"""

from tkinter import *
import tkinter
from PIL import ImageTk,Image
import tkinter.messagebox
import os

def blogopen():
	os.system('c:/Users/Alpha/Desktop/DBMS/DBMS_Final_Run/Blog/Blog.html')

def moreopen():
	os.system('c:/Users/Alpha/Desktop/DBMS/DBMS_Final_Run/Blog/Main.html')

def gotomarket():
    root.destroy()
    import Storepage
def gotostore():
    root.destroy()
    import sellerpage
    
#Root Window
root = Tk()
root.iconbitmap("images/icona.ico")
root.title("Farmers Market")
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (width, height))
root.state('zoomed')

#images
root.logo_icon=ImageTk.PhotoImage(file="images/finLogo45h.png")
root.bg_img=ImageTk.PhotoImage(file="images/80my.jpg")
root.box1_grain=ImageTk.PhotoImage(file="images/grain.jpg")
root.box2_vegetable=ImageTk.PhotoImage(file="images/veget2.jpg")
root.box3_dairy=ImageTk.PhotoImage(file="images/dairy.jpg")

#Menu bar
title_frame=Frame(root,bg="white")
title_frame.place(x=0,y=0,relwidth=1)
spacer1=Label(title_frame, bg="white",width=75)
spacer1.grid(row=0, column=1,padx=5, pady=5)
Marketbut=Button(title_frame,text="Go-to MARKET",font=("times_new_roman",12,"bold"),cursor="hand2",bg="white",fg="black",activebackground="white",activeforeground="blue",relief=GROOVE,bd=0,command=gotomarket)
Marketbut.grid(row=0, column=2,padx=5, pady=5)
blogbut=Button(title_frame,text="BLOG",font=("times_new_roman",12,"bold"),cursor="hand2",bg="white",fg="black",activebackground="white",activeforeground="green",relief=GROOVE,bd=0,command=blogopen) 
blogbut.grid(row=0, column=3,padx=5, pady=5)
homelogo=Button(title_frame,image=root.logo_icon,bd=0,bg="white",activebackground="white")
homelogo.grid(row=0, column=4,padx=5, pady=5)
morebut=Button(title_frame,text="MORE",font=("times_new_roman",12,"bold"),cursor="hand2",bg="white",fg="black",activebackground="white",activeforeground="green",relief=GROOVE,bd=0,command=moreopen)
morebut.grid(row=0, column=5,padx=5, pady=5)
Storebut=Button(title_frame,text="Go-to STORE",font=("times_new_roman",12,"bold"),cursor="hand2",bg="white",fg="black",activebackground="white",activeforeground="blue",relief=GROOVE,bd=0,command=gotostore)
Storebut.grid(row=0, column=6,padx=5, pady=5)      

#background
back=Label(root,image=root.bg_img,bg="black")
back.place(x=0,y=60,relwidth=1)

#store links
boxa=Button(root,image=root.box1_grain,bd=0,bg="white",cursor="circle",command=gotomarket)
boxa.place(x=150,y=450)
boxb=Button(root,image=root.box2_vegetable,bd=0,bg="white",cursor="circle",command=gotomarket)
boxb.place(x=618,y=450)
boxc=Button(root,image=root.box3_dairy,bd=0,bg="white",cursor="circle",command=gotomarket)
boxc.place(x=1086,y=450)

status=Label(root,text="©Abhi groups of softwares",bd=1,relief=SUNKEN,anchor=W)
status.pack(side=BOTTOM,fill=X)

root.mainloop()
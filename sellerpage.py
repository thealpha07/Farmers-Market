# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 20:02:34 2020

@author: Abhijith
"""
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 11:24:26 2020

@author: Adrak
"""

from tkinter import *
try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk

from PIL import ImageTk,Image
from tkinter import ttk
from tkinter import filedialog
import pymysql
import tkinter.messagebox
import os
import smtplib
#Data Base Connection
con=pymysql.connect(host="localhost",user="root",password="",database="registration")
cur=con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS Products(Product_ID INTEGER(50) NOT NULL PRIMARY KEY, Product_Name VARCHAR(100) NOT NULL, Product_Quantity VARCHAR(200) NOT NULL,Product_Price VARCHAR(100) NOT NULL, Product_Category VARCHAR(100) NOT NULL, ImagePath VARCHAR(500) NOT NULL)")
cur.execute("CREATE TABLE IF NOT EXISTS feedback(p_id INTEGER(50) NOT NULL PRIMARY KEY,p_name VARCHAR(100) NOT NULL, p_date DATE NOT NULL, descr VARCHAR(1000) NOT NULL)")
cur.execute("CREATE TABLE IF NOT EXISTS register(f_name VARCHAR(20) NOT NULL, l_name VARCHAR(20) NOT NULL, userid VARCHAR(20) NOT NULL PRIMARY KEY, password VARCHAR(20) NOT NULL, c_pass VARCHAR(20) NOT NULL, phone INTEGER(10) NOT NULL, email VARCHAR(20) NOT NULL, type VARCHAR(20) NOT NULL )")


def logout():
    root.destroy()
    import homepage


def makeitnull():
    f_nametxt.delete(0, END)
    l_nametxt.delete(0, END)
    usertxt.delete(0, END)
    passtxt.delete(0, END)
    conf_passtxt.delete(0, END)
    phonetxt.delete(0, END)
    emailtxt.delete(0, END)


def registerdata():
    if f_nametxt.get()=="" or l_nametxt.get()=="" or usertxt.get()=="" or passtxt.get()=="" or conf_passtxt.get()=="" or phonetxt.get()=="" or emailtxt.get()=="":
         tkinter.messagebox.showinfo(title="Error", message="All fields are required")
    elif passtxt.get()!=conf_passtxt.get():
        tkinter.messagebox.showinfo(title="Error", message="password and confirm passord must be same")
    else:
        tkinter.messagebox.showinfo(title="Success", message="Registeration Successful")
        return 1

def gotologin():
    regiswindow.destroy()
    Loginwin()        

def move_login_customer():
    regiswindow.destroy()
    root.destroy()
    import Storepage
    
def move_login_seller():
    regiswindow.destroy()
    
def regcustomer(): 
    a=registerdata()
    if a==1:
        try:
            
            cur.execute("insert into register (f_name,l_name,userid,password,c_pass,phone,email,type) values (%s,%s,%s,%s,%s,%s,%s,%s)",
                        (
                            f_nametxt.get(),
                            l_nametxt.get(),
                            usertxt.get(),
                            passtxt.get(),
                            conf_passtxt.get(),
                            phonetxt.get(),
                            emailtxt.get(),
                            "customer"
                            ))
            
            con.commit()
            makeitnull()
            move_login_customer()
            
        except:
            print(EXCEPTION)
            
               
            
def regseller():
    a=registerdata()
    if a==1:
        try:
            
            cur.execute("insert into register (f_name,l_name,userid,password,c_pass,phone,email,type) values (%s,%s,%s,%s,%s,%s,%s,%s)",
                        (
                            f_nametxt.get(),
                            l_nametxt.get(),
                            usertxt.get(),
                            passtxt.get(),
                            conf_passtxt.get(),
                            phonetxt.get(),
                            emailtxt.get(),
                            "seller"
                            ))
            
            con.commit()
            makeitnull()
            move_login_seller()
                
        except:
            print(EXCEPTION)

def registerwin(): 
    global regiswindow,f_nametxt,l_nametxt,usertxt,passtxt,conf_passtxt,phonetxt,emailtxt
    regiswindow=Toplevel()   
    regiswindow.iconbitmap("images/veggie.ico")
    regiswindow.title("Farmers Market")
    width = regiswindow.winfo_screenwidth()
    height = regiswindow.winfo_screenheight()
    regiswindow.geometry("%dx%d+0+0" % (width, height))
    regiswindow.state("zoomed") #fits the window to the screen
    regiswindow.bg_icon=ImageTk.PhotoImage(file="images/peawide.jpg")
    back=Label(regiswindow,image=regiswindow.bg_icon).pack(expand=1)
    
    #FILLER TABLE       
    title=Label(regiswindow,text="Register With Us",font=("calibri",35,"italic"),bg="#FEBD83")
    title.place(x=0,y=0,relwidth=1)
            
    register_frame=Frame(regiswindow,bg="snow2",relief=RAISED)
    register_frame.place(x=475,y=100)
    
    new_frame=Frame(regiswindow,bd=0,bg="#FEBD83")
    new_frame.place(x=660,y=570)
    
    f_name=Label(register_frame,text="First Name*",font=("times_new_roman",14,"bold"),bg="snow2")
    f_name.grid(row=0,column=0,padx=10, pady=5)
    
    f_nametxt=Entry(register_frame,bd=5,relief=GROOVE,font=("",15))
    f_nametxt.grid(row=0,column=1,padx=10, pady=5)
    
    l_name=Label(register_frame,text="Last Name",font=("times_new_roman",14,"bold"),bg="snow2")
    l_name.grid(row=1,column=0,padx=10, pady=5)
    
    l_nametxt=Entry(register_frame,bd=5,relief=GROOVE,font=("",15))
    l_nametxt.grid(row=1,column=1,padx=10, pady=5)
    
    user=Label(register_frame,text="User ID*",font=("times_new_roman",14,"bold"),bg="snow2")
    user.grid(row=2,column=0,padx=10, pady=5)
    
    usertxt=Entry(register_frame,bd=5,relief=GROOVE,font=("",15))
    usertxt.grid(row=2,column=1,padx=10, pady=5)
    
    password=Label(register_frame,text="Password*",font=("times_new_roman",14,"bold"),bg="snow2")
    password.grid(row=3,column=0,padx=10, pady=5)
    
    passtxt=Entry(register_frame,bd=5,relief=GROOVE,font=("",15),show='*')
    passtxt.grid(row=3,column=1,padx=10, pady=5)
    
    conf_password=Label(register_frame,text="Confirm Password*",font=("times_new_roman",14,"bold"),bg="snow2")
    conf_password.grid(row=4,column=0,padx=10, pady=5)
    
    conf_passtxt=Entry(register_frame,bd=5,relief=GROOVE,font=("",15),show='*')
    conf_passtxt.grid(row=4,column=1,padx=10, pady=5)
    
    phone=Label(register_frame,text="Phone Number*",font=("times_new_roman",14,"bold"),bg="snow2")
    phone.grid(row=5,column=0,padx=10, pady=5)
    
    phonetxt=Entry(register_frame,bd=5,relief=GROOVE,font=("",15))
    phonetxt.grid(row=5,column=1,padx=10, pady=5)
    
    email=Label(register_frame,text="Email ID*",font=("times_new_roman",14,"bold"),bg="snow2")
    email.grid(row=6,column=0,padx=10, pady=5)
    
    emailtxt=Entry(register_frame,bd=5,relief=GROOVE,font=("",15))
    emailtxt.grid(row=6,column=1,padx=5)
    
    label_note=Label(register_frame,text="Register as a:",font=("times_new_roman",14,"bold"),bg="snow2")
    label_note.grid(row=7,columnspan=3,pady=5)
    
    #BUTTONS
    btn=Button(register_frame,text="SELLER",command=regseller,relief=RAISED,bd=3,font=("times new roman",15,"bold"),bg="#FEBD83",fg="black")
    btn.grid(row=9,column=0, pady=10)
    
    btn=Button(register_frame,text="CUSTOMER",command=regcustomer,relief=RAISED,bd=3,font=("times new roman",15,"bold"),bg="#FEBD83",fg="black")
    btn.grid(row=9,column=1, pady=10)
    
    btn2= Button(new_frame, text="go to login",command=gotologin,relief=RAISED,bd=3,font=("times new roman",12,"italic"),bg="#FEBD83", fg="black")
    btn2.grid(row=0,column=0,padx=0, pady=0)
    
    status=Label(regiswindow,text="©Abhi groups of softwares",bd=1,relief=SUNKEN, anchor=W)
    status.pack(side=BOTTOM,fill=X)
    
    regiswindow.mainloop()

#Login window
def Loginwin():
  global loginwindow
  loginwindow= Toplevel()
  loginwindow.iconbitmap("images/veggie.ico")
  loginwindow.title("Farmers Market")
  loginwindow.geometry("550x750+500+25")
  loginwindow.bg_icon=ImageTk.PhotoImage(file="images/background2.jpg")
  loginwindow.logo_icon=ImageTk.PhotoImage(file="images/fic.png")
  back=Label(loginwindow,image=loginwindow.bg_icon).pack(expand=1)
          
  title=Label(loginwindow,text="Login System",font=("calibri",35,"italic"))
  title.place(x=0,y=0,relwidth=1)
          
  login_frame=Frame(loginwindow,bg="#EFEFEF")
  login_frame.place(x=80,y=100)
  
  global usertxt,passtxt

  logo=Label(login_frame,image=loginwindow.logo_icon,bd=0,bg="#EFEFEF")
  logo.grid(row=0,columnspan=2,pady=10)
  user=Label(login_frame,text="User ID",font=("times_new_roman",14,"bold"),bg="#EFEFEF")
  user.grid(row=1,column=0,pady=10)
  usertxt=Entry(login_frame,bd=5,relief=GROOVE,font=("",15))
  usertxt.grid(row=1,column=1,padx=10)
  passw=Label(login_frame,text="Password",font=("times_new_roman",14,"bold"),bg="#EFEFEF")
  passw.grid(row=2,column=0,pady=10)
  passtxt=Entry(login_frame,bd=5,relief=GROOVE,font=("",15),show='*')
  passtxt.grid(row=2,column=1,padx=10)
  btn=Button(login_frame,text="Login",command=login,relief=RAISED,font=("times_new_roman",15,"bold"),bg="white",fg="black")
  btn.grid(row=3,column=1,padx=(20,20), pady=30)
  btn1=Button(login_frame,text="Signup",command=move_register,relief=RAISED,font=("times_new_roman",15,"bold"),bg="white",fg="black")
  btn1.grid(row=3,column=0,padx=(60,0), pady=30)
  #btn2=Button(login_frame, text="Forgot Password",relief=RAISED,font=("times_new_roman",15,"bold"),bg="white",fg="black")
  #btn2.grid(row=4,columnspan=3,pady=10)

  frame2=Frame(loginwindow,bd=0,bg="#EFEFEF")
  frame2.place(x=235,y=675)

  btn3= Button(frame2, text="Cancel" , font=("times_new_roman",12,"bold"),bg="white", fg="black")
  btn3.grid(row=0,column=0,padx=1, pady=1)

  status=Label(loginwindow,text="©Abhi groups of softwares",bd=1,relief=SUNKEN, anchor=W)
  status.pack(side=BOTTOM,fill=X)


def move_register():
      loginwindow.destroy()
      registerwin()
      
def login():
    if usertxt.get()=="" or passtxt.get()=="":
         tkinter.messagebox.showinfo(title="Error", message="All fields are required")
    else:
        try:
            cur.execute("select * from register where userid=%s and password=%s",(usertxt.get(),passtxt.get()))
            row=cur.fetchone()
            
            if row==None:
                 tkinter.messagebox.showinfo(title="Error", message="Invalid username or password")
            else:
                 tkinter.messagebox.showinfo(title="Success", message="Login Successful")
                 loggedin(row[7])
        except EXCEPTION as e:
            print(e)

    
def loggedin(val):

    usertxt.delete(0, END)
    passtxt.delete(0, END)
    print(val)
    if val=='seller':
        loginwindow.destroy()
    
    else:
        loginwindow.destroy()
        root.destroy()
        import Storepage

    
def hide_all_frames():
	#loop to destroy child widgets
	for widget1 in frame_1.winfo_children():
	    widget1.destroy()

	for widget2 in frame_2.winfo_children():
		widget2.destroy()

	for widget3 in frame_3.winfo_children():
		widget3.destroy()
	#to forget the frame and show other frame
	pgback.pack_forget()
	frame_1.pack_forget()
	frame_2.pack_forget()
	frame_3.pack_forget()
    
   

def frame_1_show():

   hide_all_frames()

  #frame 1 Functions
   def clear_entry():
      Itementry.delete(0, END)
      Prodentry.delete(0, END)
      Quantityentry.delete(0, END)
      Priceentry.delete(0, END)
      Categoryentry.delete(0, END)

   def delete_all_rows():
      for row in Main_Inventory.get_children():
         Main_Inventory.delete(row)
      cur.execute("DELETE FROM products")
      con.commit()

   def delete_selected():
      temp=Main_Inventory.selection()
      for thing in temp:
          Main_Inventory.delete(thing)
      id_del=Itementry.get()
      cur.execute("DELETE FROM products WHERE Product_ID=(%s)",(id_del))
      con.commit()



   def select_row():
      clear_entry()
      Selected=Main_Inventory.focus()
      values=Main_Inventory.item(Selected, 'values')
      Itementry.insert(0, values[0])
      Prodentry.insert(0, values[1])
      Quantityentry.insert(0, values[2])
      Priceentry.insert(0, values[3])
      Categoryentry.insert(0, values[4])

   def Choose_img():
    global pathvar
    pathvar=filedialog.askopenfilename(title="Choose Image:",filetypes=(("PNG files","*.png"),("JPEG File","*.jpg"),("All files","*.*")))
    if (pathvar==""):
      tkinter.messagebox.showerror("Error","No Image is selected")
      return
    else:
      tkinter.messagebox.showinfo("DONE...","Image Added")


   def update_row():
      if Itementry.get()=="" or Prodentry.get()=="" or Quantityentry.get()=="" or Priceentry.get()=="" or Categoryentry.get()=="" :
        tkinter.messagebox.showerror(title="Error", message="Enter the Info")
        return
      Selected=Main_Inventory.focus()
      values=Main_Inventory.item(Selected, text="", values=(Itementry.get(), Prodentry.get(), Quantityentry.get(),Priceentry.get(), Categoryentry.get()))
      id_sel=Itementry.get()
      name_sel=Prodentry.get()
      quan_sel=Quantityentry.get()
      price_sel=Priceentry.get()
      cat_sel=Categoryentry.get()
      cur.execute("UPDATE products SET Product_Name=(%s),Product_Quantity=(%s),Product_Price=(%s),Product_Category=(%s) WHERE Product_ID=(%s)",(name_sel,quan_sel,price_sel,cat_sel,id_sel))
      con.commit()
      clear_entry()

   def add_row():
      if Itementry.get()=="" or Prodentry.get()=="" or Quantityentry.get()=="" or Priceentry.get()=="" or Categoryentry.get()=="" :
         tkinter.messagebox.showerror(title="Error", message="Enter the Info")
      global count
      Main_Inventory.insert(parent='',index='end',iid=count,text="",values=(Itementry.get(), Prodentry.get(), Quantityentry.get(),Priceentry.get(), Categoryentry.get()))
      count+=1

      try:
        cur.execute("INSERT INTO products (Product_ID,Product_Name,Product_Quantity,Product_Price,Product_Category,ImagePath) values (%s,%s,%s,%s,%s,%s)",
                (
                  Itementry.get(),
                  Prodentry.get(),
                  Quantityentry.get(),
                  Priceentry.get(),
                  Categoryentry.get(),
                  pathvar,
                            ))
        con.commit()
      except:
        print(EXCEPTION)

      clear_entry()

  #Frame 1 Contents
   frame_1.pack(side=LEFT)
   #add_prod=Frame(frame_1).place(x=100,y=100)
   Main_Inventory=ttk.Treeview(frame_1)

   Main_Inventory['columns']=("Prod_ID","Prod_Name","Prod_Quantity","Price/Kg","Category")

   Main_Inventory.column("#0",width=0,stretch=NO)
   Main_Inventory.column("Prod_ID",anchor=CENTER,width=80)
   Main_Inventory.column("Prod_Name",anchor=CENTER,width=120)
   Main_Inventory.column("Prod_Quantity",anchor=CENTER,width=140)
   Main_Inventory.column("Price/Kg",anchor=CENTER,width=100)
   Main_Inventory.column("Category",anchor=CENTER,width=100)

   Main_Inventory.heading("#0",text="Prod_ID",anchor=CENTER)
   Main_Inventory.heading("Prod_ID",text="Prod_ID",anchor=CENTER)
   Main_Inventory.heading("Prod_Name",text="Prod_Name",anchor=CENTER)
   Main_Inventory.heading("Prod_Quantity",text="Prod_Quantity",anchor=CENTER)
   Main_Inventory.heading("Price/Kg",text="Price/Kg",anchor=CENTER)
   Main_Inventory.heading("Category",text="Category",anchor=CENTER)

   #tags for strip rows
   Main_Inventory.tag_configure('OddRow',background="white")
   Main_Inventory.tag_configure('EvenRow',background="#A3DE89")
    

   #Records from database
   global count
   count=0 

   cur.execute("SELECT * FROM products")
   data=cur.fetchall()

   for record in data:
	   if count%2==0:
            Main_Inventory.insert(parent='',index='end',iid=count,text="",values=(record[0],record[1],record[2],record[3],record[4]),tags=('EvenRow', ))
            count=count+1
	   else:
            Main_Inventory.insert(parent='',index='end',iid=count,text="",values=(record[0],record[1],record[2],record[3],record[4]),tags=('OddRow', ))
            count=count+1

   Main_Inventory.pack(padx=380,pady=80,anchor=CENTER)


   #frame to hold Label and Entry
   entryframe=Frame(frame_1,bg='light steel blue')
   entryframe.pack(side=TOP,anchor=CENTER)

   ItemLabel=Label(entryframe,text="Prod_ID",bg='light steel blue',justify=CENTER)
   ItemLabel.grid(row=0,column=0)
   Itementry=Entry(entryframe,font=("",16))
   Itementry.grid(row=1,column=0)

   ProdLabel=Label(entryframe,text="Prod_Name",bg='light steel blue',justify=CENTER)
   ProdLabel.grid(row=0,column=1)
   Prodentry=Entry(entryframe,font=("",16))
   Prodentry.grid(row=1,column=1)

   QuantityLabel=Label(entryframe,text="Prod_Quantity",bg='light steel blue',justify=CENTER)
   QuantityLabel.grid(row=0,column=2)
   Quantityentry=Entry(entryframe,font=("",16))
   Quantityentry.grid(row=1,column=2)

   PriceLabel=Label(entryframe,text="Price/Kg",bg='light steel blue',justify=CENTER)
   PriceLabel.grid(row=0,column=3)
   Priceentry=Entry(entryframe,font=("",14))
   Priceentry.grid(row=1,column=3)

   CategoryLabel=Label(entryframe,text="Category",bg='light steel blue',justify=CENTER)
   CategoryLabel.grid(row=0,column=4)
   Categoryentry = ttk.Combobox(entryframe,font=("",16),width=10,height=5) 
   Categoryentry['values'] = ('', 'Fruit', 'Vegetable', 'Dairy', 'Grains', 'Pulses','Spices','Grocery') 
   Categoryentry.current(0) 
   Categoryentry.grid(row=1,column=4)


  #Add an image button
   addimg=Button(frame_1,width=20,height=2,text="Choose Image",command=Choose_img)
   addimg.pack(side=TOP,padx=50,pady=(20,10))
  #frame for buttons
   ButFrame=Frame(frame_1,bg='black')
   ButFrame.pack(side=TOP,padx=20,pady=12)
   
  #Select a row
   SelectRow=Button(ButFrame,width=20,height=2,text="Select Product",command=select_row)
   SelectRow.pack(side=LEFT,padx=40,pady=20)

  #update order button   
   Update=Button(ButFrame,width=20,height=2,text="Update",command=update_row)
   Update.pack(side=LEFT,padx=40,pady=20)

  #add a row
   AddRow=Button(ButFrame,width=20,height=2,text="Add a Row",command=add_row)
   AddRow.pack(side=LEFT,padx=40,pady=20)

  #Delete all rows Button
   DelAll=Button(ButFrame,width=20,height=2,text="Delete ALL",command=delete_all_rows)
   DelAll.pack(side=LEFT,padx=40,pady=20)

  #Delete specific row button
   DelOne=Button(ButFrame,width=20,height=2,text="Delete Product",command=delete_selected)
   DelOne.pack(side=LEFT,padx=40,pady=20)
   
   Dispmssg4=Label(frame_1,text="View Product Details Here",font=("",24))
   Dispmssg4.pack(side=BOTTOM,fill=X)

def Detail_destroy():
    Detail.destroy()
    

def sendemail():
    chosen=Sub_Inventory.focus()
    vali=Sub_Inventory.item(chosen, 'values')
    oid=vali[0]
    payment=vali[2]
    cur.execute("select * from ordert where orderid=(%s)",(oid))
    data=cur.fetchall()
    for item in data:
        email=item[3]
        print(email)
    TO = email
    SUBJECT = 'FARMERS MARKET'
    TEXT = 'Your Order is Confirmed by the farmer'
    
    # Gmail Sign In
    gmail_sender = 'farmersmarket250@gmail.com'
    gmail_passwd = 'farmers143'
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(gmail_sender, gmail_passwd)
    
    BODY = '\r\n'.join(['To: %s' % TO,
                        'From: %s' % gmail_sender,
                        'Subject: %s' % SUBJECT,
                        '', TEXT])
    
    try:
        server.sendmail(gmail_sender, [TO], BODY)
        print ('email sent')
    except:
        print ('error sending mail')
    
    server.quit()

def confirm():
    Detail.destroy()
    sendemail()
    chosen=Sub_Inventory.focus()
    vali=Sub_Inventory.item(chosen, 'values')
    oid=vali[0]
    cur.execute("delete from ordert where orderid=(%s)",(oid))
    cur.execute("delete from transaction where oid=(%s)",(oid))
    con.commit()
    frame_2_show()
    
  
    
def show_Detail():
    global Detail
    Detail= Toplevel()
    Detail.iconbitmap("images/veggie.ico")
    Detail.title("Order Details")
    Detail.geometry("450x450+550+150")
    frame_1=Frame(Detail,bd=3,relief=RIDGE,bg="white")
    frame_1.pack(fill=BOTH)
    
    row1=Frame(frame_1)
    row1.pack(side=TOP,anchor=CENTER)
    
    
    Name=Label(row1,text="Name",font=("times new roman",15,"bold"),fg="black",anchor=W)
    Name.grid(row=0,column=0,padx=10,pady=10)
    Nametxt=Label(row1,font=("times new roman",15,"bold"),bg="lightyellow",fg="black",anchor=CENTER)
    Nametxt.grid(row=0,column=1,padx=10,pady=10)
    
    phone=Label(row1,text="Phone",font=("times new roman",15,"bold"),fg="black",anchor=W)
    phone.grid(row=1,column=0,padx=10,pady=10)
    phonetxt=Label(row1,font=("times new roman",15,"bold"),bg="lightyellow",fg="black",anchor=CENTER)
    phonetxt.grid(row=1,column=1,padx=10,pady=10)
    
    email=Label(row1,text="Email",font=("times new roman",15,"bold"),fg="black",anchor=W)
    email.grid(row=2,column=0,padx=10,pady=10)
    emailtxt=Label(row1,font=("times new roman",15,"bold"),bg="lightyellow",fg="black",anchor=CENTER)
    emailtxt.grid(row=2,column=1,padx=10,pady=10)
    
    city=Label(row1,text="City",font=("times new roman",15,"bold"),fg="black",anchor=W)
    city.grid(row=3,column=0,padx=10,pady=10)
    citytxt=Label(row1,font=("times new roman",15,"bold"),bg="lightyellow",fg="black",anchor=CENTER)
    citytxt.grid(row=3,column=1,padx=10,pady=10)
    
    state=Label(row1,text="State",font=("times new roman",15,"bold"),fg="black",anchor=W)
    state.grid(row=4,column=0,padx=10,pady=10)
    statetxt=Label(row1,font=("times new roman",15,"bold"),bg="lightyellow",fg="black",anchor=CENTER)
    statetxt.grid(row=4,column=1,padx=10,pady=10)
    
    pin=Label(row1,text="Pincode",font=("times new roman",15,"bold"),fg="black",anchor=W)
    pin.grid(row=5,column=0,padx=10,pady=10)
    pintxt=Label(row1,font=("times new roman",15,"bold"),bg="lightyellow",fg="black",anchor=CENTER)
    pintxt.grid(row=5,column=1,padx=10,pady=10)
    
    addr=Label(row1,text="Address",font=("times new roman",15,"bold"),fg="black",anchor=W)
    addr.grid(row=6,column=0,padx=10,pady=10)
    addrtxt=Label(row1,font=("times new roman",15,"bold"),bg="lightyellow",fg="black",anchor=CENTER)
    addrtxt.grid(row=6,column=1,padx=10,pady=10)
    
    closebut=Button(frame_1,width=15,text="Close",command=Detail_destroy)
    closebut.pack(side=RIGHT,padx=40,pady=10)
    confbut=Button(frame_1,width=15,text="Confirm",command=confirm)
    confbut.pack(side=LEFT,padx=40,pady=10)
    
    chosen=Sub_Inventory.focus()
    vali=Sub_Inventory.item(chosen, 'values')
    oid=vali[0]
    payment=vali[2]
    cur.execute("select * from ordert where orderid=(%s)",(oid))
    data=cur.fetchall()
    for item in data:
        Nametxt.config(text=item[1])
        phonetxt.config(text=item[2])
        emailtxt.config(text=item[3])
        citytxt.config(text=item[4])
        statetxt.config(text=item[5])
        pintxt.config(text=item[6])
        addrtxt.config(text=item[7])



def frame_2_show():
  hide_all_frames()
  frame_2.pack(side=LEFT,fill=BOTH,expand=1)
  global Sub_Inventory
  Sub_Inventory=ttk.Treeview(frame_2)

  Sub_Inventory['columns']=("Order_ID","Transaction_ID","Mode")

  #"#0" is a must syntax which is used for parent child relation column
  #strech=NO make it invisible
  Sub_Inventory.column("#0",width=70,stretch=NO)
  Sub_Inventory.column("Order_ID",anchor=CENTER,width=160)
  Sub_Inventory.column("Transaction_ID",anchor=CENTER,width=180)
  Sub_Inventory.column("Mode",anchor=CENTER,width=180)

  	
  Sub_Inventory.heading("#0",text="orders",anchor=CENTER)
  Sub_Inventory.heading("Order_ID",text="Order_ID",anchor=CENTER)
  Sub_Inventory.heading("Transaction_ID",text="Transaction_ID",anchor=CENTER)
  Sub_Inventory.heading("Mode",text="Mode",anchor=CENTER)
  
  #tags for strip rows
  Sub_Inventory.tag_configure('OddRow',background="white")
  Sub_Inventory.tag_configure('EvenRow',background="#A3DE89")
  Sub_Inventory.tag_configure('lightRow' ,background="#A3DE89")
  
  try:
      global pro,user,oid
      cur.execute("select *  from transaction group by tid")
      data=cur.fetchall()
      i=0
      #print(data)
# =============================================================================
#       cur.execute("select *  from transaction")
#       data2=cur.fetchall()   
#       print(data2)
# =============================================================================
      for record in data:
          oid=record[4]
          tid=record[0]
          mode=record[1]
          pid=record[2]
          user=record[3]
          cur.execute("select *  from transaction where oid=%s",(oid))
          data2=cur.fetchall()   
          #print(data2)
          
          Sub_Inventory.insert(parent='',index='end',iid=i,text="",values=(record[4],record[0],record[1]),tags=('lightRow', ))
          for r in data2:
              pro=r[2]
              
              #print(pro,user)
              cur.execute("select * from products where Product_ID=%s ",(pro))
              row=cur.fetchall()
              #print(row)
              j=0
              for k in row:
                  #print(k)
                  
                  Sub_Inventory.insert(parent=i,index='end',text="",values=("Product_Name","Quantity","Amount"),tags=('EvenRow', ))
                  Sub_Inventory.insert(parent=i, index='end',text="",values=(k[1],"1 Kg",k[3]),tags=('OddRow', ))
                  j+=1
          i+=1
# =============================================================================
#           if not Sub_Inventory.exists(tid):
#               Sub_Inventory.insert(parent='',index='end',iid=i,text="",values=(record[3],record[0],record[1]))
#           else:
#               print("error")
# =============================================================================
  except EXCEPTION as e:
      print(e)


  #Records from database called 
# =============================================================================
#   cur.execute("SELECT * FROM products")
#   data=cur.fetchall()
# =============================================================================

# =============================================================================
#   #diplays it 
#   count=0
# 
#   for record in data:
#   	Sub_Inventory.insert(parent='',index='end',iid=count,text="",values=(record[0],record[1],record[2],record[3],record[4]))
#   	count+=1
# =============================================================================

  Sub_Inventory.pack(padx=355,pady=130,anchor=CENTER)
  
  Disp_info=Button(frame_2,text="Details",font=("",15),command=show_Detail)
  Disp_info.pack(pady=(30,70))

# =============================================================================
  Dispmssg2=Label(frame_2,text="View Orders Details Here",font=("",24))
  Dispmssg2.pack(side=TOP,fill=X)
# =============================================================================


def frame_3_show():
    hide_all_frames()
    frame_3.pack(side=LEFT,fill=BOTH,expand=1)

    Sub1_Inventory=ttk.Treeview(frame_3)
    
    Sub1_Inventory['columns']=("Prod_ID","Prod_Name","Date","Description")

	#"#0" is a must syntax which is used for parent child relation column
	#strech=NO make it invisible
    Sub1_Inventory.column("#0",width=0,stretch=NO)
    Sub1_Inventory.column("Prod_ID",anchor=CENTER,width=80)
    Sub1_Inventory.column("Prod_Name",anchor=CENTER,width=100)
    Sub1_Inventory.column("Date",anchor=CENTER,width=100)
    Sub1_Inventory.column("Description",anchor=CENTER,width=360)  
    
    Sub1_Inventory.heading("#0",text="head",anchor=CENTER)
    Sub1_Inventory.heading("Prod_ID",text="Prod_ID",anchor=CENTER)
    Sub1_Inventory.heading("Prod_Name",text="Prod_Name",anchor=CENTER)
    Sub1_Inventory.heading("Date",text="Date",anchor=CENTER)
    Sub1_Inventory.heading("Description",text="Description",anchor=CENTER)
    
    #tags for strip rows
    Sub1_Inventory.tag_configure('OddRow',background="white")
    Sub1_Inventory.tag_configure('EvenRow',background="#A3DE89")
    
    try:
      count=0
      cur.execute("SELECT * FROM feedback")
      row=cur.fetchall()
      for i in row:
        if count%2==0:
            Sub1_Inventory.insert('', 'end', values=i,tags=('EvenRow', ))
            count=count+1
        else:
            Sub1_Inventory.insert('', 'end', values=i,tags=('OddRow', ))
            count=count+1
    except:
      print(EXCEPTION)   
      
    Sub1_Inventory.pack(padx=330,pady=200,anchor=W)
    
    Dispmssg3=Label(frame_3,text="View Feedback Details Here",font=("",24))
    Dispmssg3.pack(side=TOP,fill=X)

def home_show():
    hide_all_frames()
    pgback.pack(side=LEFT)


#Root Window
root = Tk()
root.iconbitmap("images/icona.ico")
root.title("Farmers Market")
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (width, height))
root.configure(background = 'white')
root.state("zoomed")

logo_icon=ImageTk.PhotoImage(file="images/fullLogo.png")
backg_page=ImageTk.PhotoImage(file="images/pgbck.png")
icon=ImageTk.PhotoImage(file="images/fic.png")
  
Loginwin()

#Style is a TTK widget for treeview 
style=ttk.Style()
#themes are used to effect the map and make treeview wide changes
style.theme_use("default")
#configuration
style.configure("Treeview",
                background="#A3DE89",
                foregroundcolor="black",
                font=('times_new_roman',12),
                rowheight=25,
                fieldbackground="white")
style.configure("Treeview.Heading",font=('times_new_roman',12))
#Map is used so that the fieldbackground is in effect
style.map("Treeview",
          background=[('selected','#47732F')])

#Headerbar for Seller
title_bar=LabelFrame(root,bd=1,bg='white')
title_bar.pack(side=TOP,fill=X)
logo=Label(title_bar,image=logo_icon,bd=0,bg='white',activebackground="white")
logo.grid(row=0,column=1,padx=590,pady=3)
logout=Button(title_bar,text="logout",command=logout,font=("times_new_roman",10,"bold"),bg="white")
logout.grid(row=0,column=2,padx=10,pady=3)

#conatainer for side menu and its frames
whole_container=LabelFrame(root,bg='white',bd=0)
whole_container.place(x=0,y=60)
#container for side menu
side_menu=LabelFrame(whole_container,bd=0,bg='white',width=275, height=1925,padx=20)
side_menu.pack(side=LEFT,fill=Y)

#buttons to switch frames
shift_frame_0=Button(side_menu,text="Home",width=15,font=("times_new_roman",15,"bold"),bg='snow2',command=home_show)
shift_frame_0.pack(pady=20)
shift_frame_1=Button(side_menu,text="Product Operations",width=15,font=("times_new_roman",15,"bold"),bg='snow2',command=frame_1_show)
shift_frame_1.pack(pady=20)

shift_frame_2=Button(side_menu,text="View Orders",width=15,font=("times_new_roman",15,"bold"),bg='snow2',command=frame_2_show)
shift_frame_2.pack(pady=20)

shift_frame_3=Button(side_menu,text="Feedback",width=15,font=("times_new_roman",15,"bold"),bg='snow2',command=frame_3_show)
shift_frame_3.pack(pady=20)

#container for the differnt frames
#first frame
#Subframe for alignment
Sub_root=Frame(root)
Sub_root.place(x=225,y=55)

page_frame=LabelFrame(whole_container,width=2155,height=725)
page_frame.pack(side=LEFT)
#so this is the background which we an change with simple color
pgback=Label(page_frame,image=backg_page)
pgback.pack(side=LEFT)


but1=Button(pgback,image=icon,text="Product Operations",command=frame_1_show,compound=TOP,height=250,width=200,font=("times_new_roman",15,"bold")).place(x=170,y=250)
but2=Button(pgback,image=icon,text="View Orders",command=frame_2_show,compound=TOP,height=250,width=200,font=("times_new_roman",15,"bold")).place(x=540,y=250)
but3=Button(pgback,image=icon,text="Feedback",command=frame_3_show,compound=TOP,height=250,width=200,font=("times_new_roman",15,"bold")).place(x=910,y=250)

#first frame
frame_1=Label(page_frame,image=backg_page,width=2155,height=725,padx=100)

#second frame
frame_2=Label(page_frame,image=backg_page,width=2155,height=725)

#third frame
frame_3=Label(page_frame,image=backg_page,width=2155,height=725)

#Lower status bar as usual
status=Label(root,text="©Abhi groups of softwares",bd=1,relief=SUNKEN,anchor=W)
status.pack(side=BOTTOM,fill=X)

root.mainloop()

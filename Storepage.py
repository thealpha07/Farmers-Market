# -*- coding: utf-8 -*-
"""
Created on Fri Oct 9 21:39:40 2020

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
import time
import tkinter.messagebox
import pymysql
import random
#SQLconnections
con=pymysql.connect(
	host="localhost",
	user="root",
	password="",
	database="registration"
               )

cur=con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS register(f_name VARCHAR(20) NOT NULL, l_name VARCHAR(20) NOT NULL, userid VARCHAR(20) NOT NULL PRIMARY KEY, password VARCHAR(20) NOT NULL, c_pass VARCHAR(20) NOT NULL, phone INTEGER(10) NOT NULL, email VARCHAR(20) NOT NULL, type VARCHAR(20) NOT NULL )")
cur.execute("CREATE TABLE IF NOT EXISTS cart(CProduct_ID INTEGER(50) NOT NULL , CProduct_Name VARCHAR(100) NOT NULL, CProduct_Quantity VARCHAR(200) NOT NULL, CProduct_Price INT(100) NOT NULL, userid VARCHAR(100) REFERENCES register(userid))")
cur.execute('''
    CREATE TABLE IF NOT EXISTS Ordert (
    orderid integer(50)  PRIMARY KEY,
    name varchar(50) NOT NULL , 
    phone integer(100) NOT NULL, 
    email VARCHAR(200) NOT NULL ,
    city VARCHAR(100) NOT NULL, 
    state VARCHAR(100) NOT NULL, 
    pincode integer(10) NOT NULL, 
    address longtext NOT NULL,
    usern varchar(20) references register(userid) )''')
    
cur.execute("CREATE TABLE IF NOT EXISTS transaction(tid INTEGER(50) NOT NULL , mode VARCHAR(100) NOT NULL,pid integer(10),usrn varchar(15) references register(userid),oid integer(50) references ordert(orderid))")
def move_register():
	   loginwindow.destroy()
	   registerwin()


#Register Window
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
    Loginwin() 
    
def move_login_seller():
    regiswindow.destroy()
    root.destroy()
    import sellerpage  

   
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
            #con.close()
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
            #con.close()
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
    title=Label(regiswindow,text="Register With Us",font=("times_new_roman",35,"italic"),bg="#FEBD83")
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
	        
    title=Label(loginwindow,text="Login System",font=("times_new_roman",35,"italic"))
    title.place(x=0,y=0,relwidth=1)
        
    login_frame=Frame(loginwindow,bg="#EFEFEF")
    login_frame.place(x=70,y=100)
	
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

    frame2=Frame(loginwindow,bd=0,bg="#EFEFEF")
    frame2.place(x=235,y=675)

    btn3= Button(frame2, text="Cancel" , font=("times_new_roman",12,"bold"),bg="white", fg="black")
    btn3.grid(row=0,column=0,padx=1, pady=1)

    status=Label(loginwindow,text="©Abhi groups of softwares",bd=1,relief=SUNKEN, anchor=W)
    status.pack(side=BOTTOM,fill=X)
	    
def login():
    if usertxt.get()=="" or passtxt.get()=="":
         tkinter.messagebox.showinfo(title="Error", message="All fields are required")
    else:
        try:
            cur.execute("select * from register where userid=%s and password=%s",(usertxt.get(),passtxt.get()))
            row=cur.fetchone()
            
            if row==None:
                 tkinter.messagebox.showinfo(title="Error", message="Invalid username or password")
                 loginwindow.deiconify()
            else:
                 tkinter.messagebox.showinfo(title="Success", message="Login Successful")
                 loggedin(row[7])
        except EXCEPTION as e:
            print(e)

    
def loggedin(val):
    global user_ID
    user_ID=usertxt.get()
    user_info.config(text=user_ID)
    usertxt.delete(0, END)
    passtxt.delete(0, END)
    print(val)
    if val=='customer':
        loginwindow.destroy()
    
    else:
        loginwindow.destroy()
        root.destroy()
        import sellerpage
        
def logout():
    root.destroy()
    import homepage    
        
#Root Window
root = tk.Tk()
root.iconbitmap("images/icona.ico")
root.title("Farmers Market")
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (width, height))
root.configure(background = "white")
root.state('zoomed')

#images
logo_icon=PhotoImage(file="images/fullLogo.png")
notific=PhotoImage(file="images/notif.png")
search_pic=PhotoImage(file="images/search.png")
cartic=PhotoImage(file="images/cart.png")
cartad=PhotoImage(file="images/cartadd.png")
user_pic=PhotoImage(file="images/man.png")
feedbut_pic=PhotoImage(file="images/fedbck.png")
backg_page=PhotoImage(file="images/pgbck.png")

off1=PhotoImage(file="images/offer1.png")
off2=PhotoImage(file="images/offer2.png")

Loginwin()

#hovering status update
def searchbar(e):
	status.config(text="Enter the product you want to search.......")

def butsearch(e):
	status.config(text="Commence the search.......")

def butnotif(e):
	status.config(text="Notifications.......")

def butcart(e):
	status.config(text="Check Your Cart.......")

def butuser(e):
	status.config(text="USER Information.......")

def butoffer(e):
	status.config(text="Offer you can redeem today.......")
	offerBut.config(image=off2)

def butfeedback(e):
	status.config(text="Filter your search.......")	

def butaddcart(e):
	status.config(text="Add this product to yout Cart.......")

def buthoverstop(e):
	status.config(text="©Abhi groups of softwares.")
	offerBut.config(image=off1)

def AddToCart(prodID,prodname,Prodquant,prodprice):
	try:
		Prodquant="1 Kg"
		cur.execute("INSERT INTO cart (CProduct_ID, CProduct_Name, CProduct_Quantity, CProduct_Price, userid) values (%s,%s,%s,%s,%s)",
				(
					prodID,
					prodname,
					Prodquant,
					prodprice,
					user_ID,
							))
		con.commit()

	except:
		print(EXCEPTION)
	

def Disp_img(newtext):
	global prodID,prodname,Prodquant,prodprice    
	for widget1 in product_frame.winfo_children():
	    widget1.destroy()
	disp_category.config(text=newtext)
	global countcol,countrow
	countcol=0
	countrow=0
	try:
		cur.execute("SELECT * FROM `Products` WHERE Product_Category=(%s)",(newtext))
		prodlist = cur.fetchall()
		for i in range (0,len(prodlist)):
			prodID=prodlist[i][0]
			prodname=prodlist[i][1]
			Prodquant=prodlist[i][2]
			prodprice=prodlist[i][3]
			prodcateg=prodlist[i][4]
			imgsavepath=prodlist[i][5] 
			#print("%s \n%s \n%s \n%s \n%s \n%s \n\n"%(prodID,prodname,Prodquant,prodprice,prodcateg,imgsavepath))
			if (countcol%5==0):
				countrow=countrow+1
				countcol=0
			prod_name=prodname
			prod_price=prodprice
			Prod_disc="  "+prod_name+"\n   ₹"+prod_price+"/Kg"
			for_product=Frame(product_frame,bg="green",width=200,height=300)
			for_product.grid(row=countrow,column=countcol,padx=20,pady=20)
			prod=ImageTk.PhotoImage(file=imgsavepath)
			item_view_Label=Label(for_product,image=prod,bd=0,padx=10)
			item_view_Label.image=prod
			item_view_Label.place(x=0,y=0)
			cartadd=Button(for_product,image=cartad,bd=1,relief=RAISED,command=lambda prodID=prodID,prodname=prodname,Prodquant=Prodquant,prodprice=prodprice: AddToCart(prodID,prodname,Prodquant,prodprice))
			cartadd.place(x=165, y=0)
			description=Label(for_product,text="",bd=0,bg="white",font=("times_new_roman",20,"bold"),justify=CENTER)
			description.place(x=0,y=200)
			description.config(text=Prod_disc)
			countcol=countcol+1
				
	except Exception as e:
		print("Exception occurred :",e)


#Program to create tool tips
class CreateToolTip(object):
  
    def __init__(self, widget, text='widget info'):
        self.waittime = 500     #miliseconds
        self.wraplength = 180   #pixels
        self.widget = widget
        self.text = text
        self.widget.bind("<Enter>", self.enter)
        self.widget.bind("<Leave>", self.leave)
        self.widget.bind("<ButtonPress>", self.leave)
        self.id = None
        self.tw = None

    def enter(self, event=None):
        self.schedule()

    def leave(self, event=None):
        self.unschedule()
        self.hidetip()

    def schedule(self):
        self.unschedule()
        self.id = self.widget.after(self.waittime, self.showtip)

    def unschedule(self):
        id = self.id
        self.id = None
        if id:
            self.widget.after_cancel(id)

    def showtip(self, event=None):
        x = y = 0
        x, y, cx, cy = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 15
        y += self.widget.winfo_rooty() + 30
        # creates a toplevel window
        self.tw = tk.Toplevel(self.widget)
        # Leaves only the label and removes the app window
        self.tw.wm_overrideredirect(True)
        self.tw.wm_geometry("+%d+%d" % (x, y))
        label = tk.Label(self.tw, text=self.text, justify='left',
                       background="#ffffff", relief='solid', borderwidth=1,
                       wraplength = self.wraplength)
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tw
        self.tw= None
        if tw:
            tw.destroy()

def storedata():
    print(transtxt.get())
    if Nametxt.get()=="" or phonetxt.get()=="":
         tkinter.messagebox.showinfo(title="Error", message="All fields are required")
     
    else:
        tkinter.messagebox.showinfo(title="Success", message="Registeration Successful")
        return 1

def store():
  global useridfetched,orderids
  try:
        cur.execute("select userid from register where email=%s",(emailtxt.get()))
        row=cur.fetchone()
        orderids=random.randint(0, 1000)
        
        useridfetched=row[0]
        print(emailtxt.get())
        print(citytxt.get())
        print(statetxt.get())
        print(pintxt.get())
        print(addrtxt.get("1.0",END))
        print(useridfetched)
        print(phonetxt.get())
        print(Nametxt.get())
        cur.execute("insert into ordert (orderid,name,phone,email,city,state,pincode,address,usern) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                    (
                        orderids,
                        Nametxt.get(),
                        phonetxt.get(),
                        emailtxt.get(),
                        citytxt.get(),
                        statetxt.get(),
                        pintxt.get(),
                        addrtxt.get("1.0",END),
                        user_ID
                        ));
        print("hi")
        cur.execute("SELECT CProduct_ID, CProduct_Name, CProduct_Quantity, CProduct_Price FROM `cart` where userid=(%s) ",(user_ID));
        data=cur.fetchall()
        print(data)
        for i in range(0,len(data)):
                pidd=data[i][0]
                print(pidd)
                print(transtxt.get())
                print(modetxt.get())
                print(user_ID)
                try:
                    cur.execute("insert into transaction (tid,mode,pid,usrn,oid) values (%s,%s,%s,%s,%s)",(transtxt.get(),modetxt.get(),pidd,user_ID,orderids ))
                except EXCEPTION as e:
                    print(e)
                    
        con.commit()
        orderids+=1
        tkinter.messagebox.showinfo(title="ORDER", message="Order Placed Successfully")
  except EXCEPTION as e:
      print(EXCEPTION)
  croot.destroy()
  
        

def orderwin():
    global Nametxt,phonetxt,emailtxt,citytxt,statetxt,addrtxt,transtxt,modetxt,pintxt
    cartwindow.destroy()
    #root.destroy()
    
    
    #Root Window
    global croot
    croot = Toplevel()
    croot.iconbitmap("images/icona.ico")
    croot.title("Farmers Market")
    width = croot.winfo_screenwidth()
    height = croot.winfo_screenheight()
    croot.geometry("%dx%d+0+0" % (width, height))
    croot.configure(background = "black")
    croot.state('zoomed')
    croot.bg_icon=ImageTk.PhotoImage(file="images/pgbck.png")
    back=Label(croot,image=croot.bg_icon).pack(expand=1)
    title=Label(croot,text="Shopping Cart",font=("times new roman",25,"bold"),bg="#262626",fg="white",anchor="center",padx=10)
    title.place(x=0,y=0,relwidth=1)
    
    frame_1=Frame(croot,bd=3,relief=RIDGE)
    frame_1.place(x=110,y=100,width=800,height=600)
    title2=Label(frame_1,text="Enter Details",font=("times new roman",15,"bold"),bg="#262626",fg="white",anchor="center",padx=10)
    title2.place(x=0,y=0,relwidth=1)
    
    Name=Label(frame_1,text="Name",font=("times new roman",15,"bold"),fg="black")
    Name.place(x=10,y=80)
    Nametxt=Entry(frame_1,font=("times new roman",15,"bold"),bg="lightyellow",fg="black",width=25)
    Nametxt.place(x=100,y=80)
    
    phone=Label(frame_1,text="Phone",font=("times new roman",15,"bold"),fg="black")
    phone.place(x=400,y=80)
    phonetxt=Entry(frame_1,font=("times new roman",15,"bold"),bg="lightyellow",fg="black")
    phonetxt.place(x=500,y=80)
    
    email=Label(frame_1,text="Email",font=("times new roman",15,"bold"),fg="black")
    email.place(x=10,y=120)
    emailtxt=Entry(frame_1,font=("times new roman",15,"bold"),bg="lightyellow",fg="black",width=25)
    emailtxt.place(x=100,y=120)
    
    city=Label(frame_1,text="City",font=("times new roman",15,"bold"),fg="black")
    city.place(x=400,y=120)
    citytxt=Entry(frame_1,font=("times new roman",15,"bold"),bg="lightyellow",fg="black")
    citytxt.place(x=500,y=120)
    
    state=Label(frame_1,text="State",font=("times new roman",15,"bold"),fg="black")
    state.place(x=10,y=160)
    statetxt=Entry(frame_1,font=("times new roman",15,"bold"),bg="lightyellow",fg="black",width=25)
    statetxt.place(x=100,y=160)
    
    pin=Label(frame_1,text="Pincode",font=("times new roman",15,"bold"),fg="black")
    pin.place(x=400,y=160)
    pintxt=Entry(frame_1,font=("times new roman",15,"bold"),bg="lightyellow",fg="black")
    pintxt.place(x=500,y=160)
    
    addr=Label(frame_1,text="Address",font=("times new roman",15,"bold"),fg="black")
    addr.place(x=10,y=200)
    addrtxt=Text(frame_1,font=("times new roman",15,"bold"),bg="lightyellow",fg="black")
    addrtxt.place(x=100,y=200,height=100,width=600)
    
    
    info=Label(frame_1,text='''Note On Payment: 
               
        Please pay the amount to the following through Gpay/Phonepay/NEFT/RTGS 
        and enter UTR/Transaction details, 
        UPI ID = farmersmarker@axis or gpay=9292929292 
        Bank account_number = 54262315223684,
        IFSC Code =  ALLA201920 
        Thank You....!''',justify=LEFT,font=("times new roman",15,"bold"),fg="black")
    info.place(x=10,y=330)

    #second
    frame2=Frame(croot,bd=3,relief=RIDGE)
    frame2.place(x=940,y=100,width=500,height=350)
    
    
    global cart_list, count, totalAmount
    cart_list=ttk.Treeview(frame2)
    cart_list['columns']=("Product_No.","Product_Name","Quantity","Total Price")
    
    cart_list.column("#0",width=0,stretch=NO)
    cart_list.column("Product_No.",anchor=W,width=100)
    cart_list.column("Product_Name",anchor=W,width=140)
    cart_list.column("Quantity",anchor=W,width=140)
    cart_list.column("Total Price",anchor=W,width=100)
    
    cart_list.heading("#0",text="",anchor=W)
    cart_list.heading("Product_No.",text="Product_No.",anchor=W)
    cart_list.heading("Product_Name",text="Product_Name",anchor=W)
    cart_list.heading("Quantity",text="Quantity",anchor=W)
    cart_list.heading("Total Price",text="Total Price",anchor=W)
    
    count=0

    try:
        cur.execute("SELECT CProduct_ID, CProduct_Name, CProduct_Quantity, CProduct_Price FROM `cart` where userid=(%s) ",(user_ID))
        data=cur.fetchall()
        for item in data:
            cart_list.insert(parent='',index='end',iid=count,text="",values=(item[0],item[1],item[2],item[3])) 
            count+=1
    except:
        print(EXCEPTION)
    
    cart_list.place(x=5,y=40)
        
    Finalbill= "TOTAL BILL:  ₹"+ str(totalAmount) 
    totalview=Label(frame2,text=Finalbill, bg="white",font=("times_new_roman",16,"bold"))
    totalview.place(x=300,y=290)
    
    title4=Label(frame2,text="Cart",font=("times new roman",15,"bold"),bg="#262626",fg="white",anchor="center",padx=10)
    title4.place(x=0,y=0,relwidth=1)
    
    #third
    frame3=Frame(croot,bd=3,relief=RIDGE)
    frame3.place(x=940,y=450,width=500,height=250)
    
    title3=Label(frame3,text="Transaction Details",font=("times new roman",15,"bold"),bg="#262626",fg="white",anchor="center",padx=10)
    title3.place(x=0,y=0,relwidth=1)
    
    trans=Label(frame3,text="Transaction Id",font=("times new roman",15,"bold"),fg="black")
    trans.place(x=10,y=80)
    transtxt=Entry(frame3,font=("times new roman",15,"bold"),bg="lightyellow",fg="black")
    transtxt.place(x=200,y=80)
    
    mode=Label(frame3,text="Mode of payment",font=("times new roman",15,"bold"),fg="black")
    mode.place(x=10,y=120)
    modetxt=Entry(frame3,font=("times new roman",15,"bold"),bg="lightyellow",fg="black")
    modetxt.place(x=200,y=120)
    
    btn=Button(frame3,text="Submit",relief=RAISED,command=store,font=("times new roman",15,"bold"),bg="white",fg="black")
    btn.place(x=300,y=190,width=100)
    
    
    croot.mainloop()    

def Feedwin():
	Feedwindow = Toplevel()
	Feedwindow.iconbitmap("images/icona.ico")
	Feedwindow.title("Feedback")
	Feedwindow.geometry("400x400+500+150")
	Feedwindow.configure(background = "#EFEFEF")
	def submit():
		if pidtxt.get()=="" or pntxt.get()=="" or pidecrtxt=="" or pdatetxt=="":
			tkinter.messagebox.showinfo(title="Error", message="All fields are required")
		else:
			try:
				cur.execute("INSERT INTO feedback (p_name,p_id,p_date,descr) values (%s,%s,%s,%s)",
							(
								pntxt.get(),
								pidtxt.get(),
								pdatetxt.get(),
								pidecrtxt.get(),
								))
				
				con.commit()
				tkinter.messagebox.showinfo(title="Success", message="Feedback Recorded Successfully")
			except:
				print(EXCEPTION)
	title=Label(Feedwindow,text="Feedback",font=("times_new_roman",15,"italic"),height=1,background="light steel blue")
	title.pack(fill=X,side=TOP)
	Sub_Feedwindow=Frame(Feedwindow)
	Sub_Feedwindow.pack(side=TOP)
	page_frame=LabelFrame(Sub_Feedwindow,width=400,height=400,bd=0,bg="#EFEFEF",pady=20)
	page_frame.pack(side=TOP)


	pn=Label(page_frame,text="Product Name",font=("times_new_roman",12,"bold"),bg="#EFEFEF")
	pn.grid(row=1,column=0,pady=10)
	pntxt=Entry(page_frame,bd=5,relief=GROOVE,font=("",12))
	pntxt.grid(row=1,column=1,padx=10)
	pid=Label(page_frame,text="Product Id",font=("times_new_roman",12,"bold"),bg="#EFEFEF")
	pid.grid(row=2,column=0,pady=10)
	pidtxt=Entry(page_frame,bd=5,relief=GROOVE,font=("",12))
	pidtxt.grid(row=2,column=1,padx=10)
	pdate=Label(page_frame,text="Purchase Date",font=("times_new_roman",12,"bold"),bg="#EFEFEF")
	pdate.grid(row=3,column=0,pady=10)
	pdatetxt=Entry(page_frame,bd=5,relief=GROOVE,font=("",12))
	pdatetxt.grid(row=3,column=1,padx=10)
	pidecr=Label(page_frame,text="Feedback",font=("times_new_roman",12,"bold"),bg="#EFEFEF")
	pidecr.grid(row=4,column=0,pady=10)
	pidecrtxt=Entry(page_frame,bd=5,relief=GROOVE,font=("",12))
	pidecrtxt.grid(row=4,column=1,padx=10,ipady=50,ipadx=30)
	btn=Button(page_frame,text="Submit",relief=RAISED,command=submit,font=("times_new_roman",12,"bold"),bg="white",fg="black")
	btn.grid(row=5,column=1, pady=10)

	Feedwindow.mainloop()

def gotoorder():
    cartwindow.destroy()
    orderwin()
    
def shop():
    cartwindow.destroy()
    
def refresh():
	Finalbill= "TOTAL BILL:  ₹"+ str(totalAmount)
	totalview.config(text=Finalbill)
	return
    
    
def Cartwin():
	global cartwindow
	cartwindow = Toplevel()
	cartic=PhotoImage(file="images/cart.png")
	cartwindow.iconbitmap("images/cart.png")
	cartwindow.title("Cart")
	cartwindow.geometry("600x500+500+150")
	cartwindow.configure(background = "white")
	cartwindow.bg_icon=ImageTk.PhotoImage(file="images/pgbck.png")
	back=Label(cartwindow,image=cartwindow.bg_icon)
	back.place(x=0,y=0)

	ordercartframe=Frame(cartwindow,bg="white")
	ordercartframe.pack(side=TOP)
	titlename=Label(ordercartframe,text="Cart",bg='lightblue',width=14,font=('',14),justify=CENTER)
	titlename.pack(side=LEFT)

	global cart_list
	cart_list=ttk.Treeview(cartwindow)
	cart_list['columns']=("Product_No.","Product_Name","Quantity","Total Price")

	cart_list.column("#0",width=0,stretch=NO)
	cart_list.column("Product_No.",anchor=W,width=100)
	cart_list.column("Product_Name",anchor=W,width=140)
	cart_list.column("Quantity",anchor=W,width=140)
	cart_list.column("Total Price",anchor=W,width=100)

	cart_list.heading("#0",text="",anchor=W)
	cart_list.heading("Product_No.",text="Product_No.",anchor=W)
	cart_list.heading("Product_Name",text="Product_Name",anchor=W)
	cart_list.heading("Quantity",text="Quantity",anchor=W)
	cart_list.heading("Total Price",text="Total Price",anchor=W)

	global count, totalAmount, Amountadd,totalview
	count=0
	totalAmount=0
	Amountadd=0

	try:
		cur.execute("SELECT CProduct_ID, CProduct_Name, CProduct_Quantity, CProduct_Price FROM `cart` where userid=(%s) ",(user_ID))
		data=cur.fetchall()
		for item in data:
			cart_list.insert(parent='',index='end',iid=count,text="",values=(item[0],item[1],item[2],item[3]))
			Amountadd=item[3]
			totalAmount=totalAmount+Amountadd
			count+=1
	except Exception as e:
		print(e)

	cart_list.pack(padx=10,pady=10,anchor=CENTER)
	
	Finalbill= "TOTAL BILL:  ₹"+ str(totalAmount) 
	totalview=Label(cartwindow,text=Finalbill, bg="white",font=("times_new_roman",16,"bold"))
	totalview.pack(anchor=E, padx=100,pady=20)

	RmProd=Button(cartwindow,width=20,height=2,text="Remove Product",command=rm_item)
	RmProd.pack(padx=50,pady=12)

	cartbutframe=Frame(cartwindow,bg="green")
	cartbutframe.pack(side=BOTTOM,anchor=S,pady=1)
	cart_but=Button(cartbutframe,text="Continue Shopping",command=shop,bd=0,font=("Ravie",16,"bold"),bg="black",fg="white",activeforeground="green",activebackground="black",cursor="hand2")
	cart_but.grid(row=0,column=0,padx=15,pady=15)
	cart_but=Button(cartbutframe,text="Checkout & Bill",command=gotoorder,bd=0,font=("Ravie",16,"bold"),bg="black",fg="white",activeforeground="green",activebackground="black",cursor="hand2")
	cart_but.grid(row=0,column=1,padx=15,pady=15)


def rm_item():
	global totalAmount,Amountminus
	temp=cart_list.focus()
	valuehold=cart_list.item(temp, 'values')
	id_del=valuehold[0]
	Amountminus=valuehold[3]
	totalAmount=totalAmount-int(Amountminus)
	refresh()
	cur.execute("DELETE FROM cart WHERE CProduct_ID=(%s)",(id_del))
	cart_list.delete(temp)
	con.commit()


#Headerbar for user
title_bar=LabelFrame(root,bg="white",height=60)
title_bar.pack(side=TOP,fill=X)

#Logo
logo=Label(title_bar,image=logo_icon,bd=0,bg="white",activebackground="white")
logo.grid(row=0,column=1,padx=30,pady=3)
spacer3=Label(title_bar,width=10,bg="white",bd=0)
spacer3.grid(row=0, column=2)

#search should lead to the product
search_name=Label(title_bar,text="Search",font=("times_new_roman",10,"bold"),bg="white",bd=0)
search_name.grid(row=0, column=3,padx=5)
search_bar=Entry(title_bar,font=("",12),width=70 ,cursor="xterm",relief=RAISED)
search_bar.grid(row=0,column=4)
search_bar.bind("<Enter>" ,searchbar)
search_bar.bind("<Leave>" ,buthoverstop)
search_but=Button(title_bar,image=search_pic,bd=0,bg="white",activebackground="#F0F0F0",cursor="hand2")
search_but.grid(row=0,column=5,padx=20)
spacer4=Label(title_bar,width=10,bg="white",bd=0)
spacer4.grid(row=0, column=6)
search_but.bind("<Enter>" ,butsearch)
search_but.bind("<Leave>" ,buthoverstop)
search_but_ttp=CreateToolTip(search_but,"Search")

#notification on products or orders 


#leads to the cart table
cart_but=Button(title_bar,text="Cart",image=cartic,compound=LEFT,bd=0,font=("times_new_roman",12,"bold"),bg="white",activebackground="#F0F0F0",cursor="hand2",command=Cartwin)
cart_but.grid(row=0,column=7,padx=(30,10))
cart_but.bind("<Enter>" ,butcart)
cart_but.bind("<Leave>" ,buthoverstop)
cart_but_ttp=CreateToolTip(cart_but,"View Cart")

#if it could show the user name? it would look normal
global user_info
user_info=Button(title_bar,text="USER",image=user_pic,compound=LEFT,font=("times_new_roman",12,"bold"),bd=0,bg="white",activebackground="#F0F0F0",cursor="hand2",command=logout)
user_info.grid(row=0,column=8,padx=(100,10))
user_info.bind("<Enter>" ,butuser)
user_info.bind("<Leave>" ,buthoverstop)
user_info_ttp=CreateToolTip(user_info,"Logout")

#Subframe for alignment
Sub_root=Frame(root)
Sub_root.place(x=0,y=55)

#frame- categories and sub-search
option_frame=LabelFrame(Sub_root,bg="white",bd=4,width=275, height=725)
option_frame.pack(side=LEFT)

#Mainframe 2 for the products and page heading
page_frame=LabelFrame(Sub_root,width=1255,height=725)
page_frame.pack(side=LEFT)
#so this is the background which we an change with simple color
pgback=Label(page_frame,image=backg_page,width=1255,height=740)
pgback.place(x=0,y=0)

#page heading
page_heading=Frame(page_frame,bg="white",width=1255,height=50)
page_heading.place(x=0,y=0)

disp_category=Label(page_heading,text="Choose A Category",font=("Jokerman",22,"bold"),bd=0,bg="white",fg="green")
disp_category.place(x=40,y=2)

feedbut=Button(page_heading,image=feedbut_pic,text="Feedback",compound=LEFT,font=("times_new_roman",12,"bold"),bg="white",activebackground="#F0F0F0",cursor="hand2",bd=0,command=Feedwin)
feedbut.place(x=1100,y=5)
feedbut.bind("<Enter>" ,butfeedback)
feedbut.bind("<Leave>" ,buthoverstop)
feedbut_ttp=CreateToolTip(feedbut,"Feedback")

#Product page with the product images
product_frame=Frame(page_frame,width=1261,height=740,bg="black",padx=5)
product_frame.place(x=0,y=50)

#frame for category with buttons
sub_frame1=Frame(option_frame,bg="white",width=200,height=500) #category
sub_frame1.place(x=15,y=10)
categorylabel=Label(sub_frame1,text="  Categories ",bd=0,bg="white",font=("times_new_roman",26,"bold"),anchor=N,padx=15,pady=10)
categorylabel.pack(fill=X)
but_fruit=Button(sub_frame1,text="Fruits",bg="#F0F0F0",font=("times_new_roman",14,"bold"),bd=0,activebackground="white",cursor="hand2",command=lambda: Disp_img("Fruit"))
but_fruit.pack(fill=X)
but_veget=Button(sub_frame1,text="Vegetables",bg="white",font=("times_new_roman",14,"bold"),bd=0,activebackground="#F0F0F0",cursor="hand2",command=lambda: Disp_img("Vegetable"))
but_veget.pack(fill=X)
but_dairy=Button(sub_frame1,text="Dairy",bg="#F0F0F0",font=("times_new_roman",14,"bold"),bd=0,activebackground="white",cursor="hand2",command=lambda: Disp_img("Dairy"))
but_dairy.pack(fill=X)
but_pulse=Button(sub_frame1,text="Pulses",bg="white",font=("times_new_roman",14,"bold"),bd=0,activebackground="#F0F0F0",cursor="hand2",command=lambda: Disp_img("Pulses"))
but_pulse.pack(fill=X)
but_grain=Button(sub_frame1,text="Grains",bg="#F0F0F0",font=("times_new_roman",14,"bold"),bd=0,activebackground="white",cursor="hand2",command=lambda: Disp_img("Grains"))
but_grain.pack(fill=X)
but_spice=Button(sub_frame1,text="Spices",bg="white",font=("times_new_roman",14,"bold"),bd=0,activebackground="#F0F0F0",cursor="hand2",command=lambda: Disp_img("Spices"))
but_spice.pack(fill=X)
but_groce=Button(sub_frame1,text="Grocery",bg="#F0F0F0",font=("times_new_roman",14,"bold"),bd=0,activebackground="white",cursor="hand2",command=lambda: Disp_img("Grocery"))
but_groce.pack(fill=X)

#frame for farmers problems and how this helps
sub_frame3=Frame(option_frame,bg="#F0F0F0",width=235,height=150,padx=2,pady=2)
sub_frame3.place(x=15,y=325)
Note_1=Label(sub_frame3,text="Why The Struggle?",font=("times_new_roman",14,"bold"),fg="black",bd=0,justify="center",bg="white")
Note_1.pack(fill=BOTH)
sub_note_1=Label(sub_frame3,text="The ongoing farmer’s protest \nagainst the govt’s new agricultural \nlaws isn’t just a battle to secure a \nlegal guarantee for minimum \nsupport price, or seek repeal of the \nthree legislations. The battle is \nalso to stop rich capitalists from \nsmuggling out farmers’ labour power \nwithout paying the cost.",bg="white",font=("times_new_roman",10,"bold"),fg="black",bd=0,justify="center")
sub_note_1.pack(fill=BOTH)

#Offers button/label (we could replace this with facts that change every minute or so later)
sub_frame2=Frame(option_frame,bg="white",width=235,height=180) 
sub_frame2.place(x=15,y=520)
offerBut=Button(sub_frame2,image=off1,bd=0,bg="white",activebackground="white",cursor="hand2")
offerBut.pack(fill=BOTH)
offerBut.bind("<Enter>" ,butoffer)
offerBut.bind("<Leave>" ,buthoverstop)

#a timer or clock that i added simply. Reposition it or else remove it
timerframe=Frame(option_frame)
timerframe.place(x=65,y=660)
timerdisp=Label(timerframe,font=("Elephant",20,"bold"),bg="white",fg="green")
timerdisp.pack(fill=BOTH)
#timerclock()

#lowerstatus Bar
status=Label(root,text="©Abhi groups of softwares",bd=1,relief=SUNKEN,anchor=W)
status.pack(side=BOTTOM,fill=X)

root.mainloop()
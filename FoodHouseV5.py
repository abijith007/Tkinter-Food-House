from tkinter import *
from tkinter import ttk
from functools import partial
from PIL import ImageTk,Image  
from tkinter import messagebox
import pickle as p
import os
import webbrowser
import time
def init_glo():
    global northmenu,southmenu,snacksmenu,beveragemenu,cartlist,litems,lprice,lab1,lab2,lab3,tempo
    northmenu = [['Chole Bhatura',1,30,30],['Pav Bhaji',1,25,25],['Aloo Paratha',1,20,20]]
    southmenu = [['Dosa',1,20,20],['Idli',1,15,15],['Vada',1,20,20]]
    snacksmenu = [['Samosa',1,10,10],['Pani Puri',1,15,15],['Aloo Roll',1,30,30]]
    beveragemenu = [['Coffee',1,15,15],['Tea',1,15,15],['Hot Chocolate',1,25,25]]
    cartlist,tempo=[],[[],[],[],[]]


def button_exit():
    main.destroy()

def signup():
    global uname,pword,ftname,ltname,mob,signup,address
    
    signup=Tk()
    signup.title("Food House")
    signup.geometry("300x200")
    #Add the FoodHouse.png image here

    Label(signup, text="First Name: ").grid(row=5, sticky=W, padx=3)
    ftname=Entry(signup,width=20)
    ftname.grid(row=5,column=1,sticky=W,padx=0)

    Label(signup, text="Last Name: ").grid(row=6, sticky=W, padx=3)
    ltname=Entry(signup,width=20)
    ltname.grid(row=6,column=1,sticky=W,padx=0)

    Label(signup, text="Address: ").grid(row=7, sticky=W, padx=3)
    address=Entry(signup,width=20)
    address.grid(row=7,column=1,sticky=W,padx=0)

    Label(signup, text="Mobile Number: ").grid(row=8, sticky=W, padx=3)
    mob=Entry(signup,width=20)
    mob.grid(row=8,column=1,sticky=W,padx=0)

    Label(signup, text="Username: ").grid(row=9, sticky=W, padx=3)
    uname=Entry(signup,width=20)
    uname.grid(row=9,column=1,sticky=W,padx=0)

    Label(signup, text="Password: ").grid(row=10, sticky=W, padx=3)
    pword=Entry(signup,width=20)
    pword.grid(row=10,column=1,sticky=W,padx=0)

    Button(signup,text="Submit",command=Add_Customer).place(relx=0.5,rely=0.8,anchor=CENTER)
    signup.mainloop()

def settings():
    global uname,pword,ftname,ltname,mob,address
    global setup
    main.destroy()
    setup=Tk()
    setup.title("Food House")
    setup.geometry("300x230")

    l1=Label(setup,text='Settings')
    l1.config(font=("Courier", 20))
    l1.grid(row=0,columnspan=5,padx=90,pady=20)

    Label(setup,text='Enter the new details: ').grid(row=6,sticky=W)

    Label(setup, text="Address: ").grid(row=7, sticky=W, padx=3)
    address=Entry(setup,width=20)
    address.grid(row=7,column=1,sticky=W,padx=0)

    Label(setup, text="Mobile Number: ").grid(row=8, sticky=W, padx=3)
    mob=Entry(setup,width=20)
    mob.grid(row=8,column=1,sticky=W,padx=0)

    Label(setup, text="Username: ").grid(row=9, sticky=W, padx=3)
    uname=Entry(setup,width=20)
    uname.grid(row=9,column=1,sticky=W,padx=0)

    Label(setup, text="Password: ").grid(row=10, sticky=W, padx=3)
    pword=Entry(setup,width=20)
    pword.grid(row=10,column=1,sticky=W,padx=0)

    Button(setup,text='Back To Main Menu',command=partial(move,9)).place(relx=0.7,rely=0.9,anchor=CENTER)
    Button(setup,text="Submit",command=update_customer).place(relx=0.3,rely=0.9,anchor=CENTER)
    setup.mainloop()

def current_customer(y):
    global n1,n2
    if y!=1:
        f=open("Users.dat",'rb+')
        l=p.load(f)
        f.close()
        for i in range(len(l)):
            if l[i][1]==y:
                n1=l[i][2]
                n2=l[i][3]
    else:
        return([n1,n2])
    
def update_customer():
    a=current_customer(1)
    element=[uname.get(),pword.get(),a[0],a[1],address.get(),mob.get()]
    print(element,end='\n\n\n')
    f=open("Users.dat",'rb+')
    l=p.load(f)
    for i in range(len(l)):
        if l[i][2]==element[2]:
            k=i
            print(k)
    l[k]=element
    print(l)
    f.close()
    f=open("Users.dat",'wb+')
    p.dump(l,f)
    print(l)
    f.close()
    setup.destroy()

def Add_Customer():
    element=[uname.get(),pword.get(),ftname.get(),ltname.get(),address.get(),mob.get()]
    print(element,end='\n\n\n')
    l=[]
    if os.path.isfile('Users.dat')==False:
        f=open('Users.dat','wb+')
        l=[]
        l.append(element)
        p.dump(l,f)

    else:
        f=open("Users.dat",'rb+')
        l=p.load(f)
        l.append(element)
        f.seek(0)
        p.dump(l,f)
    f.close()

    signup.destroy()

def login():
    global root
    global username
    global password
    global render
    root=Tk()
    root.title("Food House")
    root.geometry("300x200")

    load= Image.open('FoodHouse.ppm')
    load=load.resize((300,100))
    render=ImageTk.PhotoImage(load)
    img=Label(root,image=render)
    img.image=render
    img.grid(columnspan=3,rowspan=2)	

    Label(root, text="Username :").grid(row=5, padx=3)
    username=Entry(root,width=20)
    username.grid(row=5,column=1,sticky=W,padx=0)        #Obtain the data entered in the textbox and perform the authentication
    Label(root, text="Password :").grid(row=6, padx=3)
    password=Entry(root,width=20,show='*')
    password.grid(row=6,column=1,sticky=W,padx=0)

    Button(root,text="Log In",command=Check_Login).grid(row=7,column=1,sticky=W,padx=8,pady=5)
    Button(root,text="Sign Up",command=signup).grid(row=7,column=1,sticky=W,padx=60,pady=5)
    root.mainloop()
    

def Check_Login():                   			# This is the authentication part
    f=open("Users.dat",'rb')
    l=p.load(f)
    f.close()
    k=0
    x=username.get()
    y=password.get()
    for i in l:
        if((i[0]==x) and (i[1]==y)):
            k=1
    if (k==1):
        messagebox.showinfo("Success","Login Successful")
        current_customer(y)
        Main_Page()
        root.destroy()
    else:
        messagebox.showerror("Error","Incorrect Username or Password")

def move(val):
    if (val==0):			#For Displaying Categories in Cuisines
        main.destroy()
        cuisines_fun()
    if(val==1):				#For returning to Main menu from cuisines
        cuisines.destroy()
        Main_Page()
    if(val==2):				#Back For North India
        befret(val-2)
        north.destroy()
        cuisines_fun()
    if(val==3):				#Back For South India
        befret(val-2)
        south.destroy()
        cuisines_fun()
    if(val==4):				#Back For Snacks
        befret(val-2)
        snacks.destroy()
        cuisines_fun()
    if(val==5):				#Back for Desserts
        befret(val-2)
        beve.destroy()
        cuisines_fun()
    if(val==6):				#Back for Cart
        cart.destroy()
        Main_Page()
    if(val==7):				#Back for Cart onto payment
    	cart.destroy()
    	payment()
    if(val==8):
    	mon.destroy()
    	done()
    if(val==9):
        setup.destroy()
        Main_Page()
    


def Main_Page():
    global main
    main=Tk()
    main.title("Food House")
    main.geometry('300x300')

    
    l1=Label(main,text='Main Menu')
    l1.config(font=("Courier", 26))
    l1.place(x=150,y=60,anchor=CENTER)

    order_but=Button(main,text="Order Up",command=partial(move,0),height=1,width=10)
    order_but.config(font=('verdana',11))
    order_but.place(relx=0.5, rely=0.4, anchor=CENTER)
    
    view_but=Button(main,text="View Cart",command=cart_view,height=1,width=10)
    view_but.config(font=('verdana',11))
    view_but.place(relx=0.5, rely=0.5, anchor=CENTER)
    

    settings_but=Button(main,text="Settings",command=settings,height=1,width=10)
    settings_but.config(font=('verdana',11))
    settings_but.place(relx=0.5, rely=0.6, anchor=CENTER)
    

    exit_but=Button(main,text="Exit",command=button_exit,height=1,width=10)
    exit_but.config(font=('verdana',11))
    exit_but.place(relx=0.5, rely=0.7, anchor=CENTER)

def cart_view():
    global cart
    main.destroy()
    cart=Tk()
    cart.title("Food House")
    cart.geometry('300x350')
    price=0
    l=cartlist
    i=0
    l1=Label(cart,text='My Cart')
    l1.config(font=("Courier", 20))
    l1.grid(row=0,columnspan=5,padx=90,pady=20)

    Label(cart,text='Sl.No').grid(row=1,column=0)
    Label(cart,text='Item').grid(row=1,column=1)
    Label(cart,text='Rate').grid(row=1,column=3)
    Label(cart,text='Quantity').grid(row=1,column=2)
    Label(cart,text='Price').grid(row=1,column=4)

    for i in range(len(l)):
        ttk.Label(cart, text = str(i+1)).grid(row = (i+2), column = 0)
        ttk.Label(cart, text = l[i][0]).grid(row = (i+2), column = 1)
        ttk.Label(cart, text = l[i][1]).grid(row = (i+2), column = 2)
        ttk.Label(cart, text = l[i][2]).grid(row = (i+2), column = 3)
        ttk.Label(cart, text = l[i][3]).grid(row = (i+2), column = 4)
        price+=l[i][3]
    
    if(price==0):
        l4=Label(cart,text='Empty')
        l4.config(font=('Courier',14))
        l4.place(x=120,y=130)
        Button(cart,text='Back To Main Menu',command=partial(move,6)).place(x=270,y=270,anchor=E)

    else:
        l2=ttk.Label(cart,text='Total Price:')
        l2.config(font=("Courier", 10))
        l2.grid(row=i+5,column=3)
    
        l3=ttk.Label(cart,text=str(price))
        l3.grid(row=i+5,column=4)
        l3.config(font=("Courier", 10))
        Button(cart,text='Back To Main Menu',command=partial(move,6)).place(x=270,y=270,anchor=E)
        Button(cart,text='Go to payment',command=partial(move,7)).place(x=130,y=270,anchor=E)
    
    cart.mainloop()

def cuisines_fun():
    global cuisines
    cuisines=Tk()
    cuisines.title("Food House")
    cuisines.geometry('400x300')

    l1=Label(cuisines,text='Cuisines')
    l1.config(font=("Courier", 26))
    l1.place(x=130,y=50)

    south_but=Button(cuisines,text="North Indian",command=north_india,height=1,width=10)
    south_but.config(font=('verdana',16))
    south_but.place(x=50, y=150, anchor=W)
    
    south_but=Button(cuisines,text="South Indian",command=south_india,height=1,width=10)
    south_but.config(font=('verdana',16))
    south_but.place(x=350, y=150, anchor=E)

    snacks_but=Button(cuisines,text="Snacks",command=snacks_india,height=1,width=10)
    snacks_but.config(font=('verdana',16))
    snacks_but.place(x=50, y=220, anchor=W)

    desserts_but=Button(cuisines,text="Beverages",command=beverages,height=1,width=10)
    desserts_but.config(font=('verdana',16))
    desserts_but.place(x=350, y=220, anchor=E)
    
    Button(cuisines,text='Back To Main Menu',command=partial(move,1)).place(x=390,y=270,anchor=E)

    cuisines.mainloop()

def north_india():
    cuisines.destroy()
    global north
    north=Tk()
    north.title('Food House')
    north.geometry('300x300')
    Label(north,text='Sl.No').grid(row=0,column=0,sticky=N,padx=5,pady=5)
    Label(north,text='Item Name').grid(row=0,column=1,sticky=N,padx=5,pady=5)
    Label(north,text='Rate (Rupees)').grid(row=0,column=2,sticky=N,padx=5,pady=5)

    Label(north,text='1.').grid(row=1,column=0,sticky=N,padx=5,pady=5)
    Label(north,text='Chole Bhatura').grid(row=1,column=1)
    Label(north,text='30').grid(row=1,column=2,sticky=N,padx=5,pady=5)
    Button(north,text=' - ',command=partial(chole,0)).grid(row=1,column=4,sticky=N,padx=5,pady=5)
    Button(north,text=' + ',command=partial(chole,1)).grid(row=1,column=7,sticky=N,padx=5,pady=5)


    Label(north,text='2.').grid(row=2,column=0,sticky=N,padx=5,pady=5)
    Label(north,text='Pav Bhaji').grid(row=2,column=1)
    Label(north,text='25').grid(row=2,column=2,sticky=N,padx=5,pady=5)
    Button(north,text=' - ',command=partial(pav,0)).grid(row=2,column=4,sticky=N,padx=5,pady=5)
    Button(north,text=' + ',command=partial(pav,1)).grid(row=2,column=7,sticky=N,padx=5,pady=5)
    
    Label(north,text='3.').grid(row=3,column=0,sticky=N,padx=5,pady=5)
    Label(north,text='Aloo Paratha').grid(row=3,column=1)
    Label(north,text='20').grid(row=3,column=2,sticky=N,padx=5,pady=5)
    Button(north,text=' - ',command=partial(paratha,0)).grid(row=3,column=4,sticky=N,padx=5,pady=5)
    Button(north,text=' + ',command=partial(paratha,1)).grid(row=3,column=7,sticky=N,padx=5,pady=5)

    counterlabel(0)
    Button(north,text='Back to Cuisines',command=partial(move,2)).place(x=270,y=170,anchor=E)

    north.mainloop()

def south_india():
    cuisines.destroy()
    global south
    south=Tk()
    south.title('Food House')
    south.geometry('300x300')
    Label(south,text='Sl.No').grid(row=0,column=0,sticky=N,padx=5,pady=5)
    Label(south,text='Item Name').grid(row=0,column=1,sticky=N,padx=5,pady=5)
    Label(south,text='Rate (Rupees)').grid(row=0,column=2,sticky=N,padx=5,pady=5)

    Label(south,text='1.').grid(row=1,column=0,sticky=N,padx=5,pady=5)
    Label(south,text='Dosa').grid(row=1,column=1)
    Label(south,text='20').grid(row=1,column=2,sticky=N,padx=5,pady=5)
    Button(south,text=' - ',command=partial(dosa,0)).grid(row=1,column=4,sticky=N,padx=5,pady=5)
    Button(south,text=' + ',command=partial(dosa,1)).grid(row=1,column=7,sticky=N,padx=5,pady=5)


    Label(south,text='2.').grid(row=2,column=0,sticky=N,padx=5,pady=5)
    Label(south,text='Idli').grid(row=2,column=1)
    Label(south,text='15').grid(row=2,column=2,sticky=N,padx=5,pady=5)
    Button(south,text=' - ',command=partial(idli,0)).grid(row=2,column=4,sticky=N,padx=5,pady=5)
    Button(south,text=' + ',command=partial(idli,1)).grid(row=2,column=7,sticky=N,padx=5,pady=5)
    
    Label(south,text='3.').grid(row=3,column=0,sticky=N,padx=5,pady=5)
    Label(south,text='Vada').grid(row=3,column=1)
    Label(south,text='25').grid(row=3,column=2,sticky=N,padx=5,pady=5)
    Button(south,text=' - ',command=partial(vada,0)).grid(row=3,column=4,sticky=N,padx=5,pady=5)
    Button(south,text=' + ',command=partial(vada,1)).grid(row=3,column=7,sticky=N,padx=5,pady=5)

    counterlabel(1)
    Button(south,text='Back to Cuisines',command=partial(move,3)).place(x=270,y=170,anchor=E)	
    south.mainloop()

def snacks_india():
    cuisines.destroy()
    global snacks
    snacks=Tk()
    snacks.title('Food House')
    snacks.geometry('300x300')
    Label(snacks,text='Sl.No').grid(row=0,column=0,sticky=N,padx=5,pady=5)
    Label(snacks,text='Item Name').grid(row=0,column=1,sticky=N,padx=5,pady=5)
    Label(snacks,text='Rate (Rupees)').grid(row=0,column=2,sticky=N,padx=5,pady=5)

    Label(snacks,text='1.').grid(row=1,column=0,sticky=N,padx=5,pady=5)
    Label(snacks,text='Samosa').grid(row=1,column=1)
    Label(snacks,text='10').grid(row=1,column=2,sticky=N,padx=5,pady=5)
    Button(snacks,text=' - ',command=partial(samosa,0)).grid(row=1,column=4,sticky=N,padx=5,pady=5)
    Button(snacks,text=' + ',command=partial(samosa,1)).grid(row=1,column=7,sticky=N,padx=5,pady=5)

    Label(snacks,text='2.').grid(row=2,column=0,sticky=N,padx=5,pady=5)
    Label(snacks,text='Pani Puri').grid(row=2,column=1)
    Label(snacks,text='15').grid(row=2,column=2,sticky=N,padx=5,pady=5)
    Button(snacks,text=' - ',command=partial(pani_puri,0)).grid(row=2,column=4,sticky=N,padx=5,pady=5)
    Button(snacks,text=' + ',command=partial(pani_puri,1)).grid(row=2,column=7,sticky=N,padx=5,pady=5)
            
    Label(snacks,text='3.').grid(row=3,column=0,sticky=N,padx=5,pady=5)
    Label(snacks,text='Aloo Roll').grid(row=3,column=1)
    Label(snacks,text='30').grid(row=3,column=2,sticky=N,padx=5,pady=5)
    Button(snacks,text=' - ',command=partial(aloo_roll,0)).grid(row=3,column=4,sticky=N,padx=5,pady=5)
    Button(snacks,text=' + ',command=partial(aloo_roll,1)).grid(row=3,column=7,sticky=N,padx=5,pady=5)
            
    counterlabel(2)
    Button(snacks,text='Back to Cuisines',command=partial(move,4)).place(x=270,y=170,anchor=E)	
    snacks.mainloop()

def beverages():
    cuisines.destroy()
    global beve
    beve=Tk()
    beve.title('Food House')
    beve.geometry('300x300')
    Label(beve,text='Sl.No').grid(row=0,column=0,sticky=N,padx=5,pady=5)
    Label(beve,text='Item Name').grid(row=0,column=1,sticky=N,padx=5,pady=5)
    Label(beve,text='Rate (Rupees)').grid(row=0,column=2,sticky=N,padx=5,pady=5)

    Label(beve,text='1.').grid(row=1,column=0,sticky=N,padx=5,pady=5)
    Label(beve,text='Coffee').grid(row=1,column=1)
    Label(beve,text='15').grid(row=1,column=2,sticky=N,padx=5,pady=5)
    Button(beve,text=' - ',command=partial(coffee,0)).grid(row=1,column=4,sticky=N,padx=5,pady=5)
    Button(beve,text=' + ',command=partial(coffee,1)).grid(row=1,column=7,sticky=N,padx=5,pady=5)


    Label(beve,text='2.').grid(row=2,column=0,sticky=N,padx=5,pady=5)
    Label(beve,text='Tea').grid(row=2,column=1)
    Label(beve,text='15').grid(row=2,column=2,sticky=N,padx=5,pady=5)
    Button(beve,text=' - ',command=partial(tea,0)).grid(row=2,column=4,sticky=N,padx=5,pady=5)
    Button(beve,text=' + ',command=partial(tea,1)).grid(row=2,column=7,sticky=N,padx=5,pady=5)
    
    Label(beve,text='3.').grid(row=3,column=0,sticky=N,padx=5,pady=5)
    Label(beve,text='Hot Chocolate').grid(row=3,column=1)
    Label(beve,text='25').grid(row=3,column=2,sticky=N,padx=5,pady=5)
    Button(beve,text=' - ',command=partial(hot_chocolate,0)).grid(row=3,column=4,sticky=N,padx=5,pady=5)
    Button(beve,text=' + ',command=partial(hot_chocolate,1)).grid(row=3,column=7,sticky=N,padx=5,pady=5)

    counterlabel(3)
    Button(beve,text='Back to Cuisines',command=partial(move,5)).place(x=270,y=170,anchor=E)
    beve.mainloop()


def chole(k):
    foodcheck(0,k,0)
def pav(k):
    foodcheck(1,k,0)
def paratha(k):
    foodcheck(2,k,0)

def dosa(k):
    foodcheck(0,k,1)
def idli(k):
    foodcheck(1,k,1)
def vada(k):
    foodcheck(2,k,1)

def samosa(k):
    foodcheck(0,k,2)
def pani_puri(k):
    foodcheck(1,k,2)
def aloo_roll(k):
    foodcheck(2,k,2)

def coffee(k):
    foodcheck(0,k,3)
def tea(k):
    foodcheck(1,k,3)
def hot_chocolate(k):
    foodcheck(2,k,3)

def befret(k):##BASICALLY SAVES THE COUNTER 
    tempo[k]=[lab1['text'],lab2['text'],lab3['text']]
    print(tempo)
    
def counterlabel(k):
    global lab1,lab2,lab3
    if k==0:
        a=north
    if k==1:
        a=south
    if k==2:
        a=snacks
    if k==3:
        a=beve
    if (tempo[k]==[]):
        lab1=Label(a,text = '0')
        lab2=Label(a,text='0')
        lab3=Label(a,text='0')
        lab1.grid(row=1,column=5)
        lab2.grid(row=2,column=5)
        lab3.grid(row=3,column=5)
    else:
        lab1=Label(a,text = tempo[k][0])
        lab2=Label(a,text = tempo[k][1])
        lab3=Label(a,text = tempo[k][2])
        lab1.grid(row=1,column=5)
        lab2.grid(row=2,column=5)
        lab3.grid(row=3,column=5)

def foodcheck(index,k,type):
    lab=[lab1,lab2,lab3]
    
    if type==0:
        ml=northmenu[index]
    if type==1:
        ml=southmenu[index]
    if type==2:
        ml=snacksmenu[index]
    if type==3:
        ml=beveragemenu[index]
    if k==1:
        lab[index]['text']=str(int(lab[index]['text'])+1)
        if (cartlist==[]):
            cartlist.append(ml)
        else:
            kk=0
            for i in cartlist:
                if ml[0]==i[0]:
                    kk=1
                    i[1]+=1
                    i[3]=i[1]*i[2]
                    break
            if kk==0:
                cartlist.append(ml)
    else:
        kk,c,d=0,0,0
        for i in cartlist:
            if ml[0]==i[0]:
                d=1
                i[1]-=1
                i[3]=i[1]*i[2]
                
                if cartlist[kk][1]==0:
                    c=1
                break
            kk+=1
        if d==1:## ADDED LINE
            lab[index]['text']=str(int(lab[index]['text'])-1)
        if c==1:
            del cartlist[kk]
    time.sleep(.300)
    print(cartlist)
            
def payment():
	global pay
	pay=Tk()
	pay.title('Food House')
	pay.geometry('300x250')

	l1=Label(pay,text='Payment Method')
	l1.config(font=("Courier", 20))
	l1.grid(row=0,columnspan=5,padx=35,pady=20)

	but1=Button(pay,text="Credit Card",command=partial(money,1),height=1,width=10)
	but1.config(font=('verdana',13))
	but1.place(x=30, y=140, anchor=W)
	
	but2=Button(pay,text="Debit Card",command=partial(money,2),height=1,width=10)
	but2.config(font=('verdana',13))
	but2.place(x=280, y=140, anchor=E)

	but3=Button(pay,text="Paytm",command=partial(money,3),height=1,width=10)
	but3.config(font=('verdana',13))
	but3.place(x=30, y=210, anchor=W)

	but4=Button(pay,text="Cash",command=partial(money,4),height=1,width=10)
	but4.config(font=('verdana',13))
	but4.place(x=280, y=210, anchor=E)

def money(n):
	global mon
	mon=Tk()
	mon.title('Food House')
	mon.geometry('300x180')

	if(n==1):
		l=Label(mon,text='Credit Card')
		l.config(font=("Courier", 20))
		l.grid(row=0,rowspan=2,columnspan=2,padx=60)
		
		Label(mon,text='Name on card: ').grid(row=3,column=0,sticky=E)
		Entry(mon).grid(row=3,column=1)

		Label(mon,text='Card Number: ').grid(row=4,column=0,sticky=E)
		Entry(mon).grid(row=4,column=1)

		Label(mon,text='Date Of Expiry: ').grid(row=5,column=0,sticky=E)
		Entry(mon).grid(row=5,column=1)

		Label(mon,text='CVV Number: ').grid(row=6,column=0,sticky=E)
		Entry(mon).grid(row=6,column=1)

		Button(mon,text='Submit',command=partial(move,8)).grid(row=8,column=1,sticky=E,padx=30)

	if(n==2):
		l=Label(mon,text='Debit Card')
		l.config(font=("Courier", 20))
		l.grid(row=0,rowspan=2,columnspan=2,padx=60)
		
		Label(mon,text='Name on card: ').grid(row=3,column=0,sticky=E)
		Entry(mon).grid(row=3,column=1)

		Label(mon,text='Card Number: ').grid(row=4,column=0,sticky=E)
		Entry(mon).grid(row=4,column=1)

		Label(mon,text='Date Of Expiry: ').grid(row=5,column=0,sticky=E)
		Entry(mon).grid(row=5,column=1)

		Label(mon,text='CVV Number: ').grid(row=6,column=0,sticky=E)
		Entry(mon).grid(row=6,column=1)

		Button(mon,text='Submit',command=partial(move,8)).grid(row=8,column=1,sticky=E,padx=30)
	if(n==3):
		pay.destroy()
		mon.destroy()
		webbrowser.open('https://paytm.com/')
		messagebox.showinfo('Payment','The order will reach you in 30 minutes, Thank you for choosing Food House')

	if(n==4):
		pay.destroy()
		mon.destroy()
		
	mon.mainloop()

def done():
	messagebox.showinfo('Payment','The order will reach you in 30 minutes, Thank you for choosing Food House')

init_glo()	
login()

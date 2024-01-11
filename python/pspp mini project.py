#The following lines are executed once and then are commented to create the binary files
f=open("usernamepass.dat",'wb')
f.close()
f=open("user.dat",'wb')
f.close()
from tkinter import *
from tkinter import messagebox
import pickle
from datetime import date
import os

def tariff():
    try:
        f=open("tariff.dat","wb")
        d3={'bangalore':{"dp":5000,"sdp":8500,"sp":10000},
             'bangkok':{"dp":6500,"sdp":8000,"sp":10000},
             'brazil':{"dp":7500,"sdp":8500,"sp":10000},
             'busan':{"dp":8500,"sdp":9500,"sp":10000},
             'chennai':{"dp":6500,"sdp":9500,"sp":10000},
             'delhi':{"dp":5000,"sdp":6500,"sp":10000},
             'dubai':{"dp":5500,"sdp":6500,"sp":10000},
             'goa':{"dp":6500,"sdp":7500,"sp":10000},
             'hongkong':{"dp":7500,"sdp":8500,"sp":10000},
             'las vegas':{"dp":5500,"sdp":6500,"sp":10000},
             'malaysia':{"dp":5600,"sdp":6500,"sp":10000},
             'maldives':{"dp":5500,"sdp":6500,"sp":10000},
             'mauritius':{"dp":6500,"sdp":7500,"sp":10000},
             'mumbai':{"dp":6500,"sdp":8500,"sp":10000},
             'new york':{"dp":5500,"sdp":6500,"sp":10000},
             'paris':{"dp":6500,"sdp":7500,"sp":10000},
             'seoul':{"dp":5500,"sdp":6500,"sp":10000},
             'singapore':{"dp":5500,"sdp":6500,"sp":10000},
             'switzerland':{"dp":6500,"sdp":7500,"sp":10000},
             'sydney':{"dp":5500,"sdp":6500,"sp":10000},
             'tokyo':{"dp":5500,"sdp":6500,"sp":10000}}
        d4={'bangalore':{"dp":7000,"sdp":8500,"sp":11000},
             'bangkok':{"dp":6500,"sdp":8000,"sp":12000},
             'brazil':{"dp":7500,"sdp":8500,"sp":11000},
             'busan':{"dp":8500,"sdp":9500,"sp":12000},
             'chennai':{"dp":8500,"sdp":9500,"sp":12000},
             'delhi':{"dp":7000,"sdp":8000,"sp":11000},
             'dubai':{"dp":6500,"sdp":7500,"sp":12000},
             'goa':{"dp":6500,"sdp":7500,"sp":12000},
             'hongkong':{"dp":7500,"sdp":8500,"sp":13000},
             'las vegas':{"dp":8500,"sdp":9500,"sp":11000},
             'malaysia':{"dp":5600,"sdp":6500,"sp":10000},
             'maldives':{"dp":7500,"sdp":8500,"sp":12000},
             'mauritius':{"dp":6500,"sdp":7500,"sp":10000},
             'mumbai':{"dp":7500,"sdp":9500,"sp":12000},
             'new york':{"dp":9500,"sdp":1000,"sp":13000},
             'paris':{"dp":8000,"sdp":9000,"sp":12000},
             'seoul':{"dp":7500,"sdp":8500,"sp":13000},
             'singapore':{"dp":6500,"sdp":8500,"sp":12000},
             'switzerland':{"dp":7500,"sdp":8500,"sp":13000},
             'sydney':{"dp":5500,"sdp":6500,"sp":10000},
             'tokyo':{"dp":7500,"sdp":9800,"sp":11000}}
        d5={'bangalore':{"dp":8000,"sdp":9500,"sp":15000},
             'bangkok':{"dp":1000,"sdp":15000,"sp":17000},
             'brazil':{"dp":9500,"sdp":12500,"sp":19000},
             'busan':{"dp":12000,"sdp":13500,"sp":16000},
             'chennai':{"dp":10000,"sdp":12500,"sp":20000},
             'delhi':{"dp":10000,"sdp":18500,"sp":20000},
             'dubai':{"dp":11500,"sdp":16000,"sp":20000},
             'goa':{"dp":9000,"sdp":10000,"sp":15000},
             'hongkong':{"dp":9000,"sdp":10000,"sp":15000},
             'las vegas':{"dp":10500,"sdp":12000,"sp":16000},
             'malaysia':{"dp":9000,"sdp":10500,"sp":13000},
             'maldives':{"dp":13300,"sdp":15500,"sp":20000},
             'mauritius':{"dp":8500,"sdp":10000,"sp":15000},
             'mumbai':{"dp":9500,"sdp":10000,"sp":18000},
             'new york':{"dp":8500,"sdp":12000,"sp":15000},
             'paris':{"dp":10000,"sdp":13000,"sp":19000},
             'seoul':{"dp":10000,"sdp":13500,"sp":17000},
             'singapore':{"dp":10500,"sdp":13500,"sp":18000},
             'switzerland':{"dp":9000,"sdp":16000,"sp":20000},
             'sydney':{"dp":9500,"sdp":15000,"sp":19000},
             'tokyo':{"dp":8500,"sdp":9500,"sp":10000}}
        da={'bangalore':{"bc":19500,"fc":20000,"ec":10000},
             'bangkok':{"bc":20000,"fc":15000,"ec":10000},
             'brazil':{"bc":25000,"fc":15000,"ec":12000},
             'busan':{"bc":23000,"fc":16000,"ec":13000},
             'chennai':{"bc":20000,"fc":18000,"ec":15000},
             'delhi':{"bc":18000,"fc":16000,"ec":12000},
             'dubai':{"bc":25000,"fc":20000,"ec":18000},
             'goa':{"bc":22000,"fc":18000,"ec":15000},
             'hongkong':{"bc":25000,"fc":15000,"ec":12000},
             'las vegas':{"bc":26000,"fc":20000,"ec":17000},
             'malaysia':{"bc":21000,"fc":19000,"ec":17000},
             'maldives':{"bc":22000,"fc":19000,"ec":15000},
             'mauritius':{"bc":23000,"fc":20000,"ec":18000},
             'mumbai':{"bc":20000,"fc":18000,"ec":15000},
             'new york':{"bc":25000,"fc":22000,"ec":19000},
             'paris':{"bc":25000,"fc":23000,"ec":20000},
             'seoul':{"bc":23000,"fc":20000,"ec":19000},
             'singapore':{"bc":25000,"fc":21000,"ec":19000},
             'switzerland':{"bc":23000,"fc":20000,"ec":18000},
             'sydney':{"bc":25000,"fc":20000,"ec":17000},
             'tokyo':{"bc":25000,"fc":20000,"ec":19000}}
        pickle.dump([d3,d4,d5,da],f)
    except EOFError:
        pass
    except IOError:
        print("file not found")
    f.close()
def newpage():
    #SIGN UP/LOGIN IN PAGE
    global username,password,npage
    npage=Toplevel(bg="white")
    npage.title("BON VOYAGE")
    npage.geometry("1800x250")
    space=Label(npage,text=" "*60,bg="white").grid(row=0,column=3)
    intro1=Label(npage,text="BON VOYAGE",fg="black",bg="white",font=("Times New Roman",40,"bold")).grid(row=0,column=5)
    intro2=Label(npage,text="DREAM.EXPLORE.DISCOVER.",fg="black",bg="white",font=("Times New Roman",24)).grid(row=1,column=5)
    space=Label(npage,text=" "*60,bg="white").grid(row=2,column=0)
    usernamelabel=Label(npage,text="USERNAME:",fg="black",bg="white",font=("Times New Roman",15,"bold")).grid(row=3,column=4)
    passwordlabel=Label(npage,text="PASSWORD:",fg="black",bg="white",font=("Times New Roman",15,"bold")).grid(row=4,column=4)
    username=StringVar()
    password=StringVar()
    username_input=Entry(npage,textvariable=username).grid(row=3,column=5)
    password_input=Entry(npage,show="*",textvariable=password).grid(row=4,column=5)
    button=Button(npage,text="SIGN UP",font=("Times New Roman",10,"bold"),command=lambda:signup()).grid(row=5,column=5)
    button=Button(npage,text="LOG IN",font=("Times New Roman",10,"bold"),command=lambda:login()).grid(row=6,column=5)
def signup():
    #SIGN UP
    global page1,u
    u=username.get()
    p=password.get()
    if u=="" and p=="":
        messagebox.showinfo("sign up","Enter username and password")
    elif p=="":
        messagebox.showinfo("sign up","Enter password")
    elif u=="" :
        messagebox.showinfo("sign up","Enter username")
    else:
        f=open("usernamepass.dat","rb")
        try:
            while True:
                d=pickle.load(f)
                if d["username"]==u:
                    messagebox.showinfo("sign up","Username already exists")
                    f.close()
                    return
        except EOFError:
            f.close()
            with open("usernamepass.dat","ab") as f:
                pickle.dump({"username":u,"password":p},f)
                messagebox.showinfo("sign up","Welcome")
            page1=Toplevel(bg="white")
            mainmenu()
        except IOError:
            print("file does not exist")
def login():
    #LOGIN
    global page1,u
    u=username.get()
    p=password.get()
    if u=="" or p=="":
        messagebox.showinfo("login","Enter username and password")
    elif u=="":
        messagebox.showinfo("login","Enter username")
    elif p=="":
        messagebox.showinfo("login","Enter password")
    else:
        f=open("usernamepass.dat","rb")
        try:
            while True:
                d=pickle.load(f)
                if d["username"]==u:
                    if d["password"]==p:
                        messagebox.showinfo("login","Welcome back")
                        f.close()
                        page1=Toplevel(bg="white")
                        mainmenu()
                        return 
                    else:
                        messagebox.showinfo("login","Invalid password")
                        f.close()
                        return 
        except EOFError:
            messagebox.showinfo("login","Invalid username")
            f.close()
            return
def mainmenu():
    #MAIN MENU PAGE
    global city,facility
    page1.geometry("1800x250")
    space=Label(page1,text=" "*100,bg="white").grid(row=0,column=1)
    label=Label(page1,text="MAIN MENU",fg="black",bg="white",font=("Times New Roman",35,"bold")).grid(row=0,column=4)
    space=Label(page1,text=" "*30,bg="white").grid(row=2,column=0)
    label=Label(page1,text="choose city:",fg="black",bg="white",font=("Times New Roman",15,"bold")).grid(row=3,column=3)
    city=StringVar()
    options=['bangalore',
             'bangkok',
             'brazil',
             'busan',
             'chennai',
             'delhi',
             'dubai',
             'goa',
             'hongkong',
             'las vegas',
             'malaysia',
             'maldives',
             'mauritius',
             'mumbai',
             'new york',
             'paris',
             'seoul',
             'singapore',
             'switzerland',
             'sydney',
             'tokyo']
    city.set(options[0])
    drop=OptionMenu(page1,city,*options).grid(row=3,column=4)
    label=Label(page1,text="choose facility:",fg="black",bg="white",font=("Times New Roman",15,"bold")).grid(row=4,column=3)
    facility=StringVar()
    facility.set("complete package")
    drop=OptionMenu(page1,facility,"complete package","airplane only","hotel only","booked ticket","cancel ticket").grid(row=4,column=4)
    submit=Button(page1,text="SUBMIT",command=reservation,font=("Times New Roman",10,"bold")).grid(row=5,column=4)
    exitbutton=Button(page1,text="EXIT",command=exitmenu,font=("Times New Roman",10,"bold")).grid(row=6,column=4)
def reservation():
    #DEPENDING ON THE FACILIY, THE RESPECTIVE FUNCTION IS CALLED
    global dair,dehot,CITY,FACILITY,book
    dair={}
    dehot={}
    CITY=city.get()
    FACILITY=facility.get()
    if FACILITY=="airplane only" :
        dair["city"]=CITY
        dair["facility"]=FACILITY
        book=False
        airplane()
    elif FACILITY=="hotel only":
        book=False
        dehot["city"]=CITY
        dehot["facility"]=FACILITY
        hotel()
    elif FACILITY=="complete package":
        book=False
        dair["city"]=CITY
        dair["facility"]=FACILITY
        dehot["city"]=CITY
        dehot["facility"]=FACILITY
        airplane()
    elif FACILITY=="cancel ticket":
        cancel()
    else:
        booktic()
def airplane():
    #AIRPLANE TICKET
    global page2,var,fclass,dair
    page2=Toplevel(bg="white")
    page2.geometry("1800x550")
    page1.destroy()
    label=Label(page2,text="AIRPLANE RESERVATION",fg="black",bg="white",font=("Times New Roman",30,"bold")).pack()
    p=[("Oneway","one"),("Roundtrip","round")]
    var=StringVar()
    var.set("none")
    for text,journey in p:
        Radiobutton(page2,text=text,variable=var,value=journey,bg="white",font=("Times New Roman",15,"bold")).pack()
    mybutton=Button(page2,text="OK",font=("ariel",10,"bold"),command=check).pack()
def check():
    #DEPENDING ON THE JOURNEY OTHER OPTIONS ARE DISPLAYED
    global j,c,dair,dept,returnd,fclass,dair,returnd,dept
    j=var.get()
    if j=="none":
        messagebox.showinfo("details","choose oneway or roundtrip")
    else:
        dair["journey"]=j
        label=Label(page2,text="DATE OF DEPARTURE",bg="white",font=("Times New Roman",15,"bold")).pack()
        dept=StringVar()
        entry=Entry(page2,textvariable=dept)
        entry.insert(0,"DD/MM/YYYY")
        entry.pack()
        returnd=StringVar()
        if j=="round":
            label=Label(page2,text="DATE OF ARRIVAL:",bg="white",font=("Times New Roman",15,"bold")).pack()
            entry=Entry(page2,textvariable=returnd)
            entry.insert(0,"DD/MM/YYYY")
            entry.pack()
            lab=Label(page2,text="Number of passengers:",fg="black",bg="white",font=("Times New Roman",15,"bold"))
            lab.pack()
            option=[1,2,3,4,5]
            c=IntVar()
            c.set(option[0])
            drop=OptionMenu(page2,c,*option)
            drop.pack()
            label=Label(page2,text="CLASS:",bg="white",font=("Times New Roman",15,"bold")).pack()
            frange=["Business Class","First Class","Economy Class"]
            fclass=StringVar()
            fclass.set("Business Class")
            drop=OptionMenu(page2,fclass,*frange).pack()
            mybutton=Button(page2,text="OK",command=date_validity,font=("Times New Roman",10,"bold")).pack()
        else:
            lab=Label(page2,text="Number of passengers:",fg="black",bg="white",font=("Times New Roman",15,"bold"))
            lab.pack()
            option=[1,2,3,4,5]
            c=IntVar()
            c.set(option[0])
            drop=OptionMenu(page2,c,*option)
            drop.pack()
            label=Label(page2,text="CLASS:",bg="white",font=("Times New Roman",15,"bold")).pack()
            frange=["Business Class","First Class","Economy Class"]
            fclass=StringVar()
            fclass.set("Business Class")
            drop=OptionMenu(page2,fclass,*frange).pack()
            mybutton=Button(page2,text="OK",font=("Times New Roman",10,"bold"),command=date_validity).pack()
def date_validity():
    #CHECKING FOR THE VALIDITY OF THE DATE
    global page2,c,dair,d1,i,num,seat,dair
    seat=fclass.get()
    dair["seat"]=seat
    d1={}
    current=date.today()
    today=current.strftime("%d/%m/%Y")
    num=c.get()
    dair["number"]=num
    if j=="round":
        if returnd.get()=="DD/MM/YYYY" and dept.get()=="DD/MM/YYYY":
            messagebox.showinfo("details","enter date of arrival and date of departure")
        elif dept.get()=="DD/MM/YYYY":
            messagebox.showinfo("details","enter date of departure")
        elif returnd.get()=="DD/MM/YYYY":
            messagebox.showinfo("details","enter date of arrival")
        else:
            if dept.get()[:2].isdigit()!=True or dept.get()[3:5].isdigit()!=True or dept.get()[6:].isdigit()!=True:
                messagebox.showinfo("details","Invalid date format for date of departure")
            elif dept.get()[2]!="/" or dept.get()[5]!="/":
                messagebox.showinfo("details","Invalid date format for date of departure")
            elif len(dept.get())!=10:
                messagebox.showinfo("details","Invalid date format for date of departure")
            elif returnd.get()[:2].isdigit()!=True or returnd.get()[3:5].isdigit()!=True or returnd.get()[6:].isdigit()!=True:
                messagebox.showinfo("details","Invalid date format for date of arrival")
            elif returnd.get()[2]!="/" or returnd.get()[5]!="/":
                messagebox.showinfo("details","Invalid date format for date of arrival")
            elif len(returnd.get())!=10:
                messagebox.showinfo("details","Invalid date format for date of arrival")
            elif int(dept.get()[6:])<int(today[6:]) or (int(dept.get()[3:5])<int(today[3:5]) and int(dept.get()[6:])==int(today[6:])) or (int(dept.get()[:2])<int(today[:2]) and int(dept.get()[3:5])==int(today[3:5]) and int(dept.get()[6:])==int(today[6:])): 
                messagebox.showinfo("details","Invalid date for date of departure")
            elif int(dept.get()[3:5])<0 or int(dept.get()[3:5])>12:
                messagebox.showinfo("details","Invalid date format for date of departure")
            elif int(dept.get()[3:5]) in [1,3,5,7,8,10,12] and (int(dept.get()[:2])<0 or int(dept.get()[:2])>31):
                messagebox.showinfo("details","Invalid date format for date of departure")
            elif int(dept.get()[3:5]) in [2,4,6,9,11] and (int(dept.get()[:2])<0 or int(dept.get()[:2])>30):
                messagebox.showinfo("details","Invalid date for date of departure")         
            elif int(returnd.get()[6:])<int(today[6:]) or (int(returnd.get()[3:5])<int(today[3:5]) and int(returnd.get()[6:])==int(today[6:])) or (int(returnd.get()[:2])<int(today[:2]) and int(returnd.get()[3:5])==int(today[3:5]) and int(returnd.get()[6:])==int(today[6:])): 
                messagebox.showinfo("details","Invalid date for date of arrival")
            elif int(returnd.get()[3:5])<0 or int(returnd.get()[3:5])>12:
                messagebox.showinfo("details","Invalid date format for date of arrival")
            elif int(returnd.get()[3:5]) in [1,3,5,7,8,10,12] and (int(returnd.get()[:2])<0 or int(returnd.get()[:2])>31):
                messagebox.showinfo("details","Invalid date format for date of arrival")
            elif int(returnd.get()[3:5]) in [2,4,6,9,11] and (int(returnd.get()[:2])<0 or int(returnd.get()[:2])>30):
                messagebox.showinfo("details","Invalid date for date of arrival")
            elif int(returnd.get()[6:])<int(dept.get()[6:]) or (int(returnd.get()[3:5])<int(dept.get()[3:5]) and int(returnd.get()[6:])>=int(dept.get()[6:])) or (int(returnd.get()[:2])<int(dept.get()[:2]) and int(returnd.get()[3:5])==int(dept.get()[3:5]) and int(returnd.get()[6:])==int(dept.get()[6:])): 
                messagebox.showinfo("details","Invalid date date for date of arrival")
            elif int(returnd.get()[3:5])<0 or int(returnd.get()[3:5])>12:
                messagebox.showinfo("details","Invalid date format for date of arrival")
            elif int(returnd.get()[3:5]) in [1,3,5,7,8,10,12] and (int(returnd.get()[:2])<0 or int(returnd.get()[:2])>31):
                messagebox.showinfo("details","Invalid date format for date of arrival")
            elif int(returnd.get()[3:5]) in [4,6,9,11] and (int(returnd.get()[:2])<0 or int(returnd.get()[:2])>30):
                messagebox.showinfo("details","Invalid date for date of arrival")
            elif int(dept.get()[3:5])==2 and int(dept.get()[:2])%4==0 and (int(dept.get()[:2])<0 or int(dept.get()[:2])>29):
                messagebox.showinfo("details","Invalid date for date of departure")
            elif int(dept.get()[3:5])==2 and int(dept.get()[:2])%4!=0 and (int(dept.get()[:2])<0 or int(dept.get()[:2])>28):
                messagebox.showinfo("details","Invalid date for date of departure")
            elif int(returnd.get()[3:5])==2 and int(returnd.get()[:2])%4==0 and (int(returnd.get()[:2])<0 or int(returnd.get()[:2])>29):
                messagebox.showinfo("details","Invalid date for date of departure")
            elif int(returnd.get()[3:5])==2 and int(returnd.get()[:2])%4!=0 and (int(returnd.get()[:2])<0 or int(returnd.get()[:2])>28):
                messagebox.showinfo("details","Invalid date for date of departure")
            else:
                dair["arrival"]=returnd.get()
                dair["departure"]=dept.get()
                i=1
                passenger1()
    elif j=="one":
        if dept.get()=="DD/MM/YYYY":
            messagebox.showinfo("details","enter date of departure")
        else:
            if dept.get()[:2].isdigit()!=True or dept.get()[3:5].isdigit()!=True or dept.get()[6:].isdigit()!=True:
                messagebox.showinfo("details","Invalid date format for date of departure")
            elif dept.get()[2]!="/" or dept.get()[5]!="/":
                messagebox.showinfo("details","Invalid date format for date of departure")
            elif len(dept.get())!=10:
                messagebox.showinfo("details","Invalid date format for date of departure")
            elif int(dept.get()[6:])<int(today[6:]) or (int(dept.get()[3:5])<int(today[3:5]) and int(dept.get()[6:])==int(today[6:])) or (int(dept.get()[:2])<int(today[:2]) and (int(dept.get()[3:5])==int(today[3:5]) and int(dept.get()[6:])==int(today[6:]))):
                messagebox.showinfo("details","Invalid date for date of departure")
            elif int(dept.get()[3:5])<0 or int(dept.get()[3:5])>12:
                messagebox.showinfo("details","Invalid date format for date of departure")
            elif int(dept.get()[3:5]) in [1,3,5,7,8,10,12] and (int(dept.get()[:2])<0 or int(dept.get()[:2])>31):
                messagebox.showinfo("details","Invalid date format for date of departure")
            elif int(dept.get()[3:5]) in [4,6,9,11] and (int(dept.get()[:2])<0 or int(dept.get()[:2])>30):
                messagebox.showinfo("details","Invalid date for date of departure")
            elif int(dept.get()[3:5])==2 and int(dept.get()[:2])%4==0 and (int(dept.get()[:2])<0 or int(dept.get()[:2])>29):
                messagebox.showinfo("details","Invalid date for date of departure")
            elif int(dept.get()[3:5])==2 and int(dept.get()[:2])%4!=0 and (int(dept.get()[:2])<0 or int(dept.get()[:2])>28):
                messagebox.showinfo("details","Invalid date for date of departure")
            else:
                dair["departure"]=dept.get()
                i=1
                passenger1()
def passenger1():
    global n,a,i,num,page3
    page2.destroy()
    page3=Toplevel(bg="white")
    if num==1:
        page3.geometry("1800x200")
    elif num==2:
        page3.geometry("1800x300")
    elif num==3:
        page3.geometry("1800x400")
    elif num==4:
        page3.geometry("1800x500")
    else:
        page3.geometry("1800x750")
    label=Label(page3,text="PASSENGER DETAILS:",bg="white",font=("ariel",18,"bold")).pack()
    if i==1:
        label=Label(page3,text="passenger"+str(i),bg="white",font=("ariel",14,"bold")).pack()
        n=Entry(page3)
        n.insert(0,"Enter name")
        n.pack()
        a=Entry(page3)
        a.insert(0,"Enter age")
        a.pack()
        button=Button(page3,text="enter",command=nameage1,font=("ariel",12,"bold")).pack()
def nameage1():
    global n,a,i,d1
    name=n.get()
    age=a.get()
    if name=="Enter name" and age=="Enter age":
        messagebox.showinfo("details","enter all details")
    elif name=="Enter name":
        messagebox.showinfo("details","enter name")
    elif age=="Enter age":
        messagebox.showinfo("details","enter age")
    else:
        if age.isdigit()==False:
            messagebox.showinfo("details","age should be integer only")
        elif int(age)==0:
            messagebox.showinfo("details","invalid age")
        else:
            d1[i]=(name,age)
            i+=1
            passenger2()
def passenger2():
    global n,a,i,num,page3
    if i<=num:
        label=Label(page3,text="passenger"+str(i),bg="white",font=("Times New Roman",14,"bold")).pack()
        n=Entry(page3)
        n.insert(0,"Enter name")
        n.pack()
        a=Entry(page3)
        a.insert(0,"Enter age")
        a.pack()
        button=Button(page3,text="enter",command=nameage2,font=("Times New Roman",12,"bold")).pack()
    else:
       button=Button(page3,text="confirm",command=price,font=("Times New Roman",12,"bold")).pack()
def nameage2():
    global n,a,i,d1
    name=n.get()
    age=a.get()
    if name=="Enter name" and age=="Enter age":
        messagebox.showinfo("details","enter all details")
    elif name=="Enter name":
        messagebox.showinfo("details","enter name")
    elif age=="Enter age":
        messagebox.showinfo("details","enter age")
    else:
        if age.isdigit()==False:
            messagebox.showinfo("details","age should be integer only")
        elif int(age)==0:
            messagebox.showinfo("details","invalid age")
        else:
            d1[i]=(name,age)
            i+=1
            passenger3()
def passenger3():
    global n,a,i,num,page3
    if i<=num:
        label=Label(page3,text="passenger"+str(i),bg="white",font=("Times New Roman",14,"bold")).pack()
        n=Entry(page3)
        n.insert(0,"Enter name")
        n.pack()
        a=Entry(page3)
        a.insert(0,"Enter age")
        a.pack()
        button=Button(page3,text="enter",command=nameage3,font=("Times New Roman",12,"bold")).pack()
    else:
       button=Button(page3,text="confirm",command=price,font=("Times New Roman",12,"bold")).pack() 
def nameage3():
    global n,a,i,d1
    name=n.get()
    age=a.get()
    if name=="Enter name" and age=="Enter age":
        messagebox.showinfo("details","enter all details")
    elif name=="Enter name":
        messagebox.showinfo("details","enter name")
    elif age=="Enter age":
        messagebox.showinfo("details","enter age")
    else:
        if age.isdigit()==False:
            messagebox.showinfo("details","age should be integer only")
        elif int(age)==0:
            messagebox.showinfo("details","invalid age")
        else:
            d1[i]=(name,age)
            i+=1
            passenger4()
def passenger4():
    global n,a,i,num,page3
    if i<=num:
        label=Label(page3,text="passenger"+str(i),bg="white",font=("Times New Roman",14,"bold")).pack()
        n=Entry(page3)
        n.insert(0,"Enter name")
        n.pack()
        a=Entry(page3)
        a.insert(0,"Enter age")
        a.pack()
        button=Button(page3,text="enter",command=nameage4,font=("Times New Roman",12,"bold")).pack()
    else:
       button=Button(page3,text="confirm",command=price,font=("Times New Roman",12,"bold")).pack()
def nameage4():
    global n,a,i,d1
    name=n.get()
    age=a.get()
    if name=="Enter name" and age=="Enter age":
        messagebox.showinfo("details","enter all details")
    elif name=="Enter name":
        messagebox.showinfo("details","enter name")
    elif age=="Enter age":
        messagebox.showinfo("details","enter age")
    else:
        if age.isdigit()==False:
            messagebox.showinfo("details","age should be integer only")
        elif int(age)==0:
            messagebox.showinfo("details","invalid age")
        else:
            d1[i]=(name,age)
            i+=1
            passenger5()
def passenger5():
    global n,a,i,num,page3
    if i<=num:
        label=Label(page3,text="passenger"+str(i),bg="white",font=("Times New Roman",14,"bold")).pack()
        n=Entry(page3)
        n.insert(0,"Enter name")
        n.pack()
        a=Entry(page3)
        a.insert(0,"Enter age")
        a.pack()
        button=Button(page3,text="enter",command=nameage5,font=("Times New Roman",12,"bold")).pack()
    else:
       button=Button(page3,text="confirm",command=price,font=("Times New Roman",12,"bold")).pack()
def nameage5():
    global n,a,i,d1
    name=n.get()
    age=a.get()
    if name=="Enter name" and age=="Enter age":
        messagebox.showinfo("details","enter all details")
    elif name=="Enter name":
        messagebox.showinfo("details","enter name")
    elif age=="Enter age":
        messagebox.showinfo("details","enter age")
    else:
        if age.isdigit()==False:
            messagebox.showinfo("details","age should be integer only")
        elif int(age)==0:
            messagebox.showinfo("details","invalid age")
        else:
            d1[i]=(name,age)
            i+=1
            button=Button(page3,text="confirm",command=price,font=("Times New Roman",12,"bold")).pack()           
def price():
    global page2,page4,mop,FACILITY,finpri,dair,seat,cpack
    dair["passengers"]=d1
    page3.destroy()
    page4=Toplevel(bg="white")
    page4.geometry("1800x650")
    label=Label(page4,text="PRICE:",bg="white",font=("Times New Roman",15,"bold")).pack()
    tariff()
    f=open("tariff.dat","rb")
    down=pickle.load(f)
    f.close()
    if CITY in down[3]:
        if seat=="Business Class":
            finpri=num*down[3][CITY]["bc"]
            dair["final_price"]=finpri
            mylabel=Label(page4,text=finpri,bg="white",font=("Times New Roman",15,"bold")).pack()
        elif seat=="First Class":
            finpri=num*down[3][CITY]["fc"]
            dair["final_price"]=finpri
            mylabel=Label(page4,text=finpri,bg="white",font=("Times New Roman",15,"bold")).pack()
        elif seat=="Economy Class":
            finpri=num*down[3][CITY]["ec"]
            dair["final_price"]=finpri
            mylabel=Label(page4,text=finpri,bg="white",font=("Times New Roman",15,"bold")).pack()
    paymentlabel=Label(page4,text="MODE OF PAYMENT",bg="white",font=("Times New Roman",14,"bold")).pack()
    mop=StringVar()
    mop.set("netbanking")
    options=["netbanking","credit card","debit card"]
    drop=OptionMenu(page4,mop,*options)
    drop.pack()
    cpack="ca"
    button=Button(page4,text="confirm",command=lambda:mode(page4),font=("Times New Roman",12,"bold")).pack()
def mode(paying):
    #MODE OF PAYMENT
    global mode_pay,bankname,IFSC,transactionpass,cardno,page4,page5,amt,FACILITY
    mode_pay=mop.get()
    if mode_pay=="netbanking":
        bankname=StringVar()
        bankname.set("")
        label1=Label(paying,text="enter bank name",bg="white",font=("Times New Roman",14,"bold")).pack()
        entry1=Entry(paying,textvariable=bankname).pack()
        IFSC=StringVar()
        IFSC.set("")
        label2=Label(paying,text="enter IFSC code:",bg="white",font=("Times New Roman",14,"bold")).pack()
        entry2=Entry(paying,textvariable=IFSC).pack()
        amt=StringVar()
        amt.set("")
        label3=Label(paying,text="enter amount:",bg="white",font=("Times New Roman",14,"bold")).pack()
        entry3=Entry(paying,textvariable=amt).pack()
        transactionpass=StringVar()
        transactionpass.set("")
        label4=Label(paying,text="enter transaction password:",bg="white",font=("Times New Roman",14,"bold")).pack()
        entry4=Entry(paying,textvariable=transactionpass,show="*").pack()
        button=Button(paying,text="pay",command=pay,font=("Times New Roman",12,"bold")).pack()
    elif mode_pay=="credit card":
        cardno=StringVar()
        cardno.set("")
        transactionpass=StringVar()
        transactionpass.set("")
        amt=StringVar()
        amt.set("")
        label1=Label(paying,text="enter credit card number:",bg="white",font=("Times New Roman",14,"bold")).pack()
        entry1=Entry(paying,textvariable=cardno).pack()
        label2=Label(paying,text="enter amount:",bg="white",font=("Times New Roman",14,"bold")).pack()
        entry2=Entry(paying,textvariable=amt).pack()
        label3=Label(paying,text="enter transaction password:",bg="white",font=("Times New Roman",14,"bold")).pack()
        entry3=Entry(paying,textvariable=transactionpass,show="*").pack()
        button=Button(paying,text="pay",command=pay,font=("Times New Roman",12,"bold")).pack()
    else:
        cardno=StringVar()
        cardno.set("")
        transactionpass=StringVar()
        transactionpass.set("")
        amt=StringVar()
        amt.set("")
        label1=Label(paying,text="enter debit card number:",bg="white",font=("Times New Roman",14,"bold")).pack()
        entry1=Entry(paying,textvariable=cardno).pack()
        label2=Label(paying,text="enter amount:",bg="white",font=("Times New Roman",14,"bold")).pack()
        entry2=Entry(paying,textvariable=amt).pack()
        label3=Label(paying,text="enter transaction password",bg="white",font=("Times New Roman",14,"bold")).pack()
        entry3=Entry(paying,textvariable=transactionpass,show="*").pack()
        button=Button(paying,text="pay",command=pay,font=("Times New Roman",12,"bold")).pack()
def pay():
    #FINAL TRANSACTION
    global FACILITY,finalprice,finpri,cpack,duser,u
    duser={}
    if mode_pay=="netbanking":
        if bankname.get()!="" and IFSC.get()!="" and transactionpass.get()!="" and amt.get()!="":
            if amt.get().isdigit():
                if FACILITY=="hotel only" or (FACILITY=="complete package" and cpack=="ch"):
                    if int(amt.get())==finalprice:
                        messagebox.showinfo("transaction","transaction complete")
                        if FACILITY=="hotel only":
                            f1=open("user.dat","ab")
                            duser[u]={"hotel":dehot}
                            pickle.dump(duser,f1)
                            f1.close()
                            hotelbill()
                        else:
                            f1=open("user.dat","rb+")
                            f1.seek(0)
                            try:
                                while True:
                                    pos=f1.tell()
                                    duser=pickle.load(f1)
                                    if u in duser:
                                        f1.seek(pos)
                                        duser[u]["hotel"]=dehot
                                        pickle.dump(duser,f1)
                                        f1.close()
                                        hotelbill()
                                        break
                            except EOFError:
                                f1.close()
                                pass
                    elif int(amt.get())<finalprice:
                        messagebox.showinfo("transaction","amount is insufficient")
                    elif int(amt.get())>finalprice:
                        messagebox.showinfo("transaction","Please check the amount you have entered")
                elif FACILITY=="airplane only" or (FACILITY=="complete package" and cpack=="ca"):
                    if int(amt.get())==finpri:
                        messagebox.showinfo("transaction","transaction complete")
                        f1=open("user.dat","ab")
                        duser[u]={"airplane":dair}
                        pickle.dump(duser,f1)
                        f1.close()
                        airplaneticket()
                    elif int(amt.get())<finpri:
                        messagebox.showinfo("transaction","amount is insufficient")
                    elif int(amt.get())>finpri:
                        messagebox.showinfo("transaction","Please check the amount you have entered")
            else:
                messagebox.showinfo("transaction","amount should be an integer")
        else:
            messagebox.showinfo("transaction", "enter all details")
    elif mode_pay=="credit card" or mode_pay=="debit card":
        if cardno.get()!="" and transactionpass.get()!="" and amt.get()!="":
            if cardno.get().isdigit()==True or len(cardno.get())==16:
                if amt.get().isdigit():
                    if FACILITY=="hotel only" or (FACILITY=="complete package" and cpack=="ch"):
                        if int(amt.get())==finalprice:
                            messagebox.showinfo("transaction","transaction complete")
                            if FACILITY=="hotel only":
                                f1=open("user.dat","ab")
                                duser[u]={"hotel":dehot}
                                pickle.dump(duser,f1)
                                f1.close()
                                hotelbill()
                            else:
                                f1=open("user.dat","rb+")
                                f1.seek(0)
                                try:
                                    while True:
                                        pos=f1.tell()
                                        duser=pickle.load(f1)
                                        if u in duser:
                                            f1.seek(pos)
                                            duser[u]["hotel"]=dehot
                                            pickle.dump(duser,f1)
                                            f1.close()
                                            hotelbill()
                                            break
                                except EOFError:
                                    f1.close()
                                    pass
                        elif int(amt.get())<finalprice:
                            messagebox.showinfo("transaction","amount is insufficient")
                        elif int(amt.get())>finalprice:
                            messagebox.showinfo("transaction","Please check the amount you have entered")
                    elif FACILITY=="airplane only" or (FACILITY=="complete package" and cpack=="ca"):
                        if int(amt.get())==finpri:
                            messagebox.showinfo("transaction","transaction complete")
                            f1=open("user.dat","ab")
                            duser[u]={"airplane":dair}
                            pickle.dump(duser,f1)
                            f1.close()
                            airplaneticket()
                        elif int(amt.get())<finpri:
                            messagebox.showinfo("transaction","amount is insufficient")
                        elif int(amt.get())>finpri:
                            messagebox.showinfo("transaction","Please check the amount you have entered")
                else:
                    messagebox.showinfo("transaction","amount should be an integer")
            else:
               messagebox.showinfo("transaction","invalid card number") 
        else:
            messagebox.showinfo("transaction", "enter all details")           
def hotel():
    #HOTEL RESERVATION
    global page5,CITY,number,Star,rms,dehot,nameh,page1
    if FACILITY=="hotel only":
        page1.destroy()
    elif FACILITY=="complete package":
        page.destroy()
    else:
        page1.destroy()
    page5=Toplevel(bg="white")
    page5.geometry("1800x750")
    label=Label(page5,text="HOTEL BOOKING",fg="black",bg="white",font=("Times New Roman",30,"bold")).pack()
    label=Label(page5,text="Enter name:",bg="white",font=("Times New Roman",14,"bold")).pack()
    nameh=StringVar()
    label=Entry(page5,textvariable=nameh).pack()
    acc=Label(page5,text="Enter number of accomodations:",bg="white",font=("Times New Roman",14,"bold")).pack()
    number=Entry(page5)
    number.pack()
    v=Label(page5,text="Select Star rating:",bg="white",font=("Times New Roman",14,"bold")).pack()
    s=["3 star","4 star","5 Star"]
    Star=StringVar()
    Star.set(s[0])
    drop=OptionMenu(page5,Star,*s).pack()
    rm=Label(page5,text="Select type of room:",bg="white",font=("Times New Roman",14,"bold")).pack()
    r=["DELUXE","SUPER DELUXE","SUITE"]
    rms=StringVar()
    rms.set(r[0])
    drop=OptionMenu(page5,rms,*r).pack()
    mybutton=Button(page5,text="Confirm",command=pricecalc,font=("Times New Roman",10,"bold")).pack()
def pricecalc():
    #FINAL PRICE CALCULATIONS
    global page5,mop,finalprice,FACILITY,dehot,cpack,nameh
    tariff()
    cpack="ch"
    if number.get()=="":
        messagebox.showinfo("details","Enter number of accomodations")
    elif number.get().isdigit()!=True:
        messagebox.showinfo("details","Enter a integral number")
    elif number.get()=='0':
        messagebox.showinfo("details","Enter a non-zero number")
    else:
        accnum=int(number.get())
        dehot["accnum"]=int(number.get())
        star=Star.get()
        dehot["star"]=star
        room=rms.get()
        dehot["room"]=room
        name_h=nameh.get()
        dehot["name_h"]=name_h
        with open("tariff.dat","rb") as f:
            l=pickle.load(f)
            f.close()
            if star=="3 star":
                d=l[0]
                if CITY in d:
                    if room=="DELUXE":
                        roomrate=d[CITY]["dp"]
                        finalprice=accnum*roomrate
                        dehot["final_price"]=finalprice
                        pricelabel=Label(page5,text="PRICE:",bg="white",font=("Times New Roman",20,"bold")).pack()
                        price=Label(page5,text=finalprice,font=("Times New Roman",12,"bold"),bg="white").pack()
                        paymentlabel=Label(page5,text="MODE OF PAYMENT",bg="white",font=("Times New Roman",14,"bold")).pack()
                        mop=StringVar()
                        mop.set("netbanking")
                        options=["netbanking","credit card","debit card"]
                        drop=OptionMenu(page5,mop,*options)
                        drop.pack()
                        button=Button(page5,text="confirm",command=lambda:mode(page5),font=("Times New Roman",10,"bold")).pack()
                    elif room=="SUPER DELUXE":
                        roomrate=d[CITY]["sdp"]
                        finalprice=accnum*roomrate
                        dehot["final_price"]=finalprice
                        pricelabel=Label(page5,text="PRICE:",bg="white",font=("Times New Roman",20,"bold")).pack()
                        price=Label(page5,text=finalprice,font=("Times New Roman",12,"bold"),bg="white").pack()
                        paymentlabel=Label(page5,text="MODE OF PAYMENT",bg="white",font=("Times New Roman",14,"bold")).pack()
                        mop=StringVar()
                        mop.set("netbanking")
                        options=["netbanking","credit card","debit card"]
                        drop=OptionMenu(page5,mop,*options)
                        drop.pack()
                        button=Button(page5,text="confirm",command=lambda:mode(page5),font=("Times New Roman",10,"bold")).pack()
                    else:
                        roomrate=d[CITY]["sp"]
                        finalprice=accnum*roomrate
                        dehot["final_price"]=finalprice
                        pricelabel=Label(page5,text="PRICE:",bg="white",font=("ariel",20,"bold")).pack()
                        price=Label(page5,text=finalprice,font=("ariel",12,"bold"),bg="white").pack()
                        paymentlabel=Label(page5,text="MODE OF PAYMENT",bg="white",font=("Times New Roman",14,"bold")).pack()
                        mop=StringVar()
                        mop.set("netbanking")
                        options=["netbanking","credit card","debit card"]
                        drop=OptionMenu(page5,mop,*options)
                        drop.pack()
                        button=Button(page5,text="confirm",command=lambda:mode(page5),font=("Times New Roman",10,"bold")).pack()
            elif star=="4 star":
                d=l[1]
                if CITY in d:
                    if room=="DELUXE":
                        roomrate=d[CITY]["dp"]
                        finalprice=accnum*roomrate
                        dehot["final_price"]=finalprice
                        pricelabel=Label(page5,text="PRICE:",bg="white",font=("Times New Roman",20,"bold")).pack()
                        price=Label(page5,text=finalprice,font=("Times New Roman",12,"bold"),bg="white").pack()
                        paymentlabel=Label(page5,text="MODE OF PAYMENT",bg="white",font=("Times New Roman",14,"bold")).pack()
                        mop=StringVar()
                        mop.set("netbanking")
                        options=["netbanking","credit card","debit card"]
                        drop=OptionMenu(page5,mop,*options)
                        drop.pack()
                        button=Button(page5,text="confirm",command=lambda:mode(page5),font=("Times New Roman",10,"bold")).pack()
                    elif room=="SUPER DELUXE":
                        roomrate=d[CITY]["sdp"]
                        finalprice=accnum*roomrate
                        dehot["final_price"]=finalprice
                        pricelabel=Label(page5,text="PRICE:",bg="white",font=("Times New Roman",20,"bold")).pack()
                        price=Label(page5,text=finalprice,font=("Times New Roman",12,"bold"),bg="white").pack()
                        paymentlabel=Label(page5,text="MODE OF PAYMENT",bg="white",font=("Times New Roman",14,"bold")).pack()
                        mop=StringVar()
                        mop.set("netbanking")
                        options=["netbanking","credit card","debit card"]
                        drop=OptionMenu(page5,mop,*options)
                        drop.pack()
                        button=Button(page5,text="confirm",command=lambda:mode(page5,font=("Times New Roman",10,"bold"))).pack()
                    else:
                        roomrate=d[CITY]["sp"]
                        finalprice=accnum*roomrate
                        dehot["final_price"]=finalprice
                        pricelabel=Label(page5,text="PRICE:",bg="white",font=("Times New Roman",20,"bold")).pack()
                        price=Label(page5,text=finalprice,font=("Times New Roman",12,"bold"),bg="white").pack()
                        paymentlabel=Label(page5,text="MODE OF PAYMENT",bg="white",font=("Times New Roman",14,"bold")).pack()
                        mop=StringVar()
                        mop.set("netbanking")
                        options=["netbanking","credit card","debit card"]
                        drop=OptionMenu(page5,mop,*options)
                        drop.pack()
                        button=Button(page5,text="confirm",command=lambda:mode(page5),font=("Times New Roman",10,"bold")).pack()
            else:
                d=l[2]
                if CITY in d:
                    if room=="DELUXE":
                        roomrate=d[CITY]["dp"]
                        finalprice=accnum*roomrate
                        dehot["final_price"]=finalprice
                        pricelabel=Label(page5,text="PRICE:",bg="white",font=("Times New Roman",20,"bold")).pack()
                        price=Label(page5,text=finalprice,font=("Times New Roman",12,"bold"),bg="white").pack()
                        paymentlabel=Label(page5,text="MODE OF PAYMENT",bg="white",font=("Times New Roman",14,"bold")).pack()
                        mop=StringVar()
                        mop.set("netbanking")
                        options=["netbanking","credit card","debit card"]
                        drop=OptionMenu(page5,mop,*options)
                        drop.pack()
                        button=Button(page5,text="confirm",command=lambda:mode(page5),font=("Times New Roman",10,"bold")).pack()
                    elif room=="SUPER DELUXE":
                        roomrate=d[CITY]["sdp"]
                        finalprice=accnum*roomrate
                        dehot["final_price"]=finalprice
                        pricelabel=Label(page5,text="PRICE:",bg="white",font=("Times New Roman",20,"bold")).pack()
                        price=Label(page5,text=finalprice,font=("Times New Roman",12,"bold"),bg="white").pack()
                        paymentlabel=Label(page5,text="MODE OF PAYMENT",bg="white",font=("Times New Roman",14,"bold")).pack()
                        mop=StringVar()
                        mop.set("netbanking")
                        options=["netbanking","credit card","debit card"]
                        drop=OptionMenu(page5,mop,*options)
                        drop.pack()
                        button=Button(page5,text="confirm",command=lambda:mode(page5),font=("Times New Roman",10,"bold")).pack()
                    else:
                        roomrate=d[CITY]["sp"]
                        finalprice=accnum*roomrate
                        dehot["final_price"]=finalprice
                        pricelabel=Label(page5,text="PRICE:",bg="white",font=("Times New Roman",20,"bold")).pack()
                        price=Label(page5,text=finalprice,font=("Times New Roman",12,"bold"),bg="white").pack()
                        paymentlabel=Label(page5,text="MODE OF PAYMENT",bg="white",font=("Times New Roman",14,"bold")).pack()
                        mop=StringVar()
                        mop.set("netbanking")
                        options=["netbanking","credit card","debit card"]
                        drop=OptionMenu(page5,mop,*options)
                        drop.pack()
                        button=Button(page5,text="confirm",command=lambda:mode(page5),font=("Times New Roman",10,"bold")).pack()
def airplaneticket():
    #AIRPLANE TICKET GENERATION
    global page,page4,CITY,seat,FACILITY,u
    if FACILITY=="airplane only" or FACILITY=="complete package":
        page4.destroy()
    page=Toplevel(bg="white")
    f=open("user.dat","rb")
    flag=True
    try:
        while flag:
            d=pickle.load(f)
            if u in d:
                flag=False
                if ("airplane" in d[u] and "hotel" in d[u]) or ("airplane" in d[u] and "hotel" not in d[u]):
                    d1=d[u]["airplane"]
                    page.geometry("1800x750")
                    label=Label(page,text="AIR TICKET",bg="white",font=("Times New Roman",40,"bold")).pack()
                    label=Label(page,text=" "*10,bg="white").pack()
                    label=Label(page,text="DESTINATION",bg="white",font=("Times New Roman",15,"bold")).pack()
                    label=Label(page,text=CITY,bg="white",font=("Times New Roman",15)).pack()
                    if d1["journey"]=="one":       
                        label=Label(page,text="DATE OF DEPARTURE",bg="white",font=("Times New Roman",15,"bold")).pack()
                        label=Label(page,text=d1["departure"],bg="white",font=("Times New Roman",15)).pack()
                    else:
                        label=Label(page,text="DATE OF DEPARTURE",bg="white",font=("Times New Roman",15,"bold")).pack()
                        label=Label(page,text=d1["departure"],bg="white",font=("Times New Roman",15)).pack()
                        label=Label(page,text="DATE OF ARRIVAL",bg="white",font=("Times New Roman",15,"bold")).pack()
                        label=Label(page,text=d1["arrival"],bg="white",font=("Times New Roman",15)).pack()
                    label=Label(page,text="CLASS:",bg="white",font=("Times New Roman",15,"bold")).pack()
                    label=Label(page,text=d1["seat"],bg="white",font=("Times New Roman",15)).pack()
                    label=Label(page,text="PASSENGER DETAILS:",bg="white",font=("Times New Roman",15,"bold")).pack()
                    for i in range(1,d1["number"]+1):
                        label=Label(page,text=d1["passengers"][i][0],bg="white",font=("Times New Roman",12,"bold")).pack()
                        label=Label(page,text=d1["passengers"][i][1],bg="white",font=("Times New Roman",12,"bold")).pack()
                    if FACILITY!="airplane only" and FACILITY!="booked ticket" and FACILITY!="cancel ticket":
                        label=Label(page,text="Click ok to proceed to hotel booking",bg="white",font=("Times New Roman",12,"bold")).pack()
                        f.close()
                        button=Button(page,text="OK",command=hotel).pack()
                    elif FACILITY=="booked ticket":
                        f.close()
                        if book=="airplane ticket only":
                            button=Button(page,text="OK",command=thankyou).pack()
                        elif book=="complete package":
                            button=Button(page,text="OK",command=hotelbill).pack()
                    else:
                        f.close()
                        button=Button(page,text="OK",command=thankyou).pack()
    except EOFError:
        f.close()
        pass
def hotelbill():
    #HOTEL BILL GNERATION
    global page6,name,page5,book,cl,u
    if FACILITY=="hotel only" or FACILITY=="complete package":
        page5.destroy()
    page6=Toplevel(bg="white")
    page6.geometry("1800x750")
    f=open("user.dat","rb")
    flag=True
    try:
        while flag:
            d=pickle.load(f)
            if u in d:
                flag=False
                if ("airplane" in d[u] and "hotel" in d[u]) or ("airplane" not in d[u] and "hotel" in d[u]):
                        d2=d[u]["hotel"]
                        label=Label(page6,text="HOTEL BILL",bg="white",font=("ariel",40,"bold")).pack()
                        label=Label(page6,text=" "*10,bg="white").pack()
                        label=Label(page6,text="NAME:",bg="white",font=("ariel",15,"bold")).pack()
                        label=Label(page6,text=d2["name_h"],bg="white",font=("ariel",15)).pack() 
                        label=Label(page6,text="CATEGORY:",bg="white",font=("ariel",15,"bold")).pack()
                        label=Label(page6,text=d2["star"],bg="white",font=("ariel",15)).pack()
                        label=Label(page6,text="ROOM:",bg="white",font=("ariel",15,"bold")).pack()
                        label=Label(page6,text=d2["room"],bg="white",font=("ariel",15)).pack()
                        label=Label(page6,text="NUMBER OF ACCOMODATIONS",bg="white",font=("ariel",15,"bold")).pack()
                        label=Label(page6,text=d2["accnum"],bg="white",font=("ariel",15)).pack()
                        label=Label(page6,text="AMOUNT PAID:",bg="white",font=("ariel",15,"bold")).pack()
                        label=Label(page6,text=d2["final_price"],bg="white",font=("ariel",15)).pack()
                        button=Button(page6,text="OK",command=thankyou).pack()
                        cl="hot"
                        f.close()
    except EOFError:
        f.close()
        pass   
def thankyou():
    #DISPLAYING THANK YOU MESSAGE ONCE THEY BOOK
    global FACILITY,page,page6,book,cpack,cl
    if FACILITY=="hotel only" or book=="hotel bill only"  or (FACILITY=="complete package" and cpack=="ch"):
        page6.destroy()
    elif book=="complete package" and cl=="hot":
        page6.destroy()
        page.destroy()
    elif FACILITY=="airplane only" or book=="airplane ticket only"  or (FACILITY=="complete package" and cpack=="ca"):
        page.destroy()
    messagebox.showinfo("BON VOYAGE","THANK YOU FOR CHOOSING US! BON VOYAGE!!!")
def booktic():
    #DISPLAYING BOOKED TICKET
    global u,book
    f=open("user.dat","rb")
    try:
        while True:
            d=pickle.load(f)
            if u in d:
                if "airplane" in d[u] and "hotel" not in d[u]:
                    book="airplane ticket only"
                    airplaneticket()
                    f.close()
                    break
                elif "airplane" in d[u] and "hotel" in d[u]:
                    book="complete package"
                    airplaneticket()
                    f.close()
                    break
                else:
                    book="hotel bill only"
                    f.close()
                    hotelbill()
                    break
    except EOFError:
        messagebox.showinfo("booked ticket","No tickets booked")
        f.close()
def cancel():
    #CANCELLATION OF BOOKED TICKET
    global u
    a=messagebox.askyesno("cancellation","Are you sure you want to cancel?")
    if a==True:
        cancellation=False
        x=os.path.getsize("user.dat")
        if x==0:
            messagebox.showinfo("cancellation","no ticket booked to cancel")
        else:
            f=open("user.dat",'rb')
            f1=open("temp.dat",'wb')
            try:
                while True:
                    d=pickle.load(f)
                    if u in d:
                        cancellation=True
                        continue
                    else:
                        pickle.dump(d,f1)
            except EOFError:
                if cancellation:
                    f.close()
                    f1.close()
                    messagebox.showinfo("cancellation","Successfully cancelled your ticket")
                else:
                    messagebox.showinfo("cancellation","no ticket booked to cancel")
                os.remove("user.dat")
                os.rename("temp.dat","user.dat")
def exitmenu():
    #EXITING MAIN MENU
    a=messagebox.askyesno("MAIN MENU","Are you sure you want to exit?")
    if a==True:
        page1.destroy()
        messagebox.showinfo("BON VOYAGE","HOPE YOU HAD A GOOD EXPERIENCE!SEE YOU NEXT TIME!")
root=Tk()
root.config(bg="white")
root.title("BON VOYAGE")
root.geometry("2000x1333")

projectname=Label(root,text ="TRAVEL AGENCY",fg="white",bg="black",font=("Times New Roman",70,"bold","italic")).pack()

button=Button(root,text="Continue",fg="black",font=("Times New Roman",14,"bold"),command=newpage).pack()
root.mainloop()

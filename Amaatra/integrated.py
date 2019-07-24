from tkinter import *
from PIL import Image
from PIL import ImageTk
from tkinter import ttk
import pandas as pd
import os
import tkinter.messagebox
import pyrebase
from datetime import date
import sys
from fpdf import FPDF
import time
import matplotlib.pyplot as plt


config = {
    "apiKey": "AIzaSyATuQBI1JJ9sI4jyLjvKbLQX6pzPeGfOMA",
    "authDomain": "amaatraid.firebaseapp.com",
    "databaseURL": "https://amaatraid.firebaseio.com",
    "projectId": "amaatraid",
    "storageBucket": "amaatraid.appspot.com",
    "messagingSenderId": "829220285103"
  }

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
database = firebase.database()
path = ""
today = str(date.today())

ReturnName = ""
Age = 0
Choice =-1


RPMresult = BSTresult = GDTresult = VLresult = 0
pathdir = ""

Name = ""
Age = 0
test_number = 0


class Plot:
    def __init__(self,master):
        
        print('Starting the plot function')
        self.master=master
        frame1 = Frame(master,width=500,height=50)
        frame1.pack(side=TOP)
        maxlabel = Label(frame1, text = "BST min: 90| GDT min: 21| RPM min: 26| Vineland min: 90",wraplength=500,justify="left") #search
        maxlabel.pack()

    def plot(self,bst,rpm,gdt,vi):
        self.z = 0
        print(bst)
        fig, axs = plt.subplots(2, 2)
        i = 1
        y1 = []
        print(f'bst {bst} gdt {gdt} rpm {rpm} vi {vi}')
        for x1 in bst :
            y1.append(i)
            i = i+1
        axs[0, 0].bar(y1, bst, label='Binet Simon Test', color='tab:blue')
        axs[0, 0].set_title('BST')
        i = 1
        y1 = []
        
        for x1 in gdt :
            y1.append(i)
            i = i+1
        axs[0, 1].bar(y1, gdt, label='Gessel\'s Drawing Test', color='tab:orange')
        axs[0, 1].set_title('GDT')
        i = 1
        y1 = []
        
        for x1 in rpm :
            y1.append(i)
            i = i+1
        axs[1, 0].bar(y1, rpm, label='Raven\'s Progressive Matrix', color='tab:green')
        axs[1, 0].set_title('RPM')
        y1 = []
        i = 1
        y1 = []
        
        for x1 in vi :
            y1.append(i)
            i = i+1
        axs[1, 1].bar(y1, vi, label='Vineland Social Maturity Scale', color='tab:red')
        axs[1, 1].set_title('Vinelands')
        fig.suptitle('Test results comparison')
        plt.tight_layout()

        filepath=os.path.dirname(os.path.abspath(__file__))
        plt.savefig(filepath+'/Images/Report.png')
        frame2 = Frame(self.master,width=500,height=400)
        frame2.pack(side=TOP)
        photo = Image.open(filepath+'/Images/Report.png')
        photo = photo.resize((500, 400), Image.ANTIALIAS)
        self.render = ImageTk.PhotoImage(photo)
        photolabel = Label(frame2,image=self.render)
        photolabel.image = self.render
        photolabel.pack()
        endb = Button(self.master,text="Finish",command = self.quitb)
        endb.pack(side=BOTTOM)
        print('Plot successful')
    
    def quitb(self):
        self.master.destroy()
        self.master.quit()     

class LoginTeacher:
    def __init__(self,f,master,numb):
        self.f=f
        self.master = master
        self.Password=StringVar()
        self.Email = StringVar()
        self.label_0 = Label(f, text="Staff Login Verification",width=20,font=("bold", 20))
        self.label_0.place(x=90,y=53)

        self.label_1 = Label(f, text="Email",width=20,font=("bold", 10))
        self.label_1.place(x=80,y=130)

        self.entry_1 = Entry(f, textvar=self.Email)
        self.entry_1.place(x=240,y=130)

        self.label_2 = Label(f, text="Password",width=20,font=("bold", 10))
        self.label_2.place(x=79,y=180)

        self.entry_2 = Entry(f, textvar=self.Password)
        self.entry_2.place(x=240,y=180)

        self.btn = Button(f, text='Submit',width=20, anchor="center", command=self.insertlogin)
        self.btn.place(x=180,y=300)


    def insertlogin(self):
        email=self.Email.get()
        password=self.Password.get()

        #Check entered details with existing details on firebase to verify staff or not
        print(self.Email.get())
        #to check if primary key aready EXISTS
        try:
            user = auth.sign_in_with_email_and_password(email,password)
            info=auth.get_account_info(user['idToken'])
            print(info)
            self.f.destroy()

            #global root
            f1 = Frame(self.master,width=500,height=500)
            f1.configure(background='peach puff')
            f1.pack()
            page1 = Page1(f1,self.master)
        except:
            tkinter.messagebox.showinfo("No access", "Invalid email or password")

    def returnnametocalling(self):
        global ReturnName,path
        return ReturnName,path

    def returnagetocalling(self):
        global Age
        return Age

    def returnchoice(self):
        global Choice
        return Choice

class Page1: #Intermediate window to choose new student, previous student or retake of test
    def __init__(self, f,master):
        self.f=f
        self.master=master
        self.label_0 = Label(f, text="Choose Activity",width=20,font=("bold", 20))
        self.label_0.place(x=90,y=53)
        self.btn1 = Button(self.f, text='New Student',width=20, anchor="center",command=self.newstudent)
        self.btn1.place(x=160,y=310)
        self.btn2 = Button(self.f, text='Todays report',width=20, anchor="center", command=self.report)
        self.btn2.place(x=160,y=410)

    def newstudent(self):
        global Choice
        Choice = 1
        self.f.destroy()
        f1 = Frame(self.master,width=500,height=500)
        f1.configure(background='peach puff')
        f1.pack()
        page2 = NewStudent(f1,self.master)

    def report(self):
        global Choice
        Choice = 2
        self.f.destroy()
        f2 = Frame(self.master,width=500,height=500)
        f2.configure(background='peach puff')
        f2.pack()
        page3 = Reports(f2,self.master)

class NewStudent:
    def __init__(self, f,master):
        self.f=f
        self.master=master
        self.Fname=StringVar()
        self.Lname = StringVar()
        self.Gender=StringVar()
        self.Age = IntVar()
        self.Dob = StringVar()

        self.label_0 = Label(f, text="Enter Student Details",width=20,font=("bold", 20))
        self.label_0.place(x=90,y=53)

        self.label_1 = Label(f, text="First Name",width=20,font=("bold", 10))
        self.label_1.place(x=80,y=130)

        self.entry_1 = Entry(f, textvar=self.Fname)
        self.entry_1.place(x=240,y=130)

        self.label_2 = Label(f, text="Last Name",width=20,font=("bold", 10))
        self.label_2.place(x=79,y=180)

        self.entry_2 = Entry(f, textvar=self.Lname)
        self.entry_2.place(x=240,y=180)

        self.label_3 = Label(f, text="Age",width=20,font=("bold", 10))
        self.label_3.place(x=79,y=230)

        self.entry_3 = Entry(f, textvar=self.Age)
        self.entry_3.place(x=240,y=230)

        self.label_4 = Label(f, text="Gender",width=20,font=("bold", 10))
        self.label_4.place(x=79,y=280)

        self.entry_4 = Entry(f, textvar=self.Gender)
        self.entry_4.place(x=240,y=280)

        self.label_5 = Label(f, text="DOB",width=20,font=("bold", 10))
        self.label_5.place(x=79,y=320)

        self.entry_5 = Entry(f, textvar=self.Dob)
        self.entry_5.place(x=240,y=320)

        self.btn = Button(f, text='Submit',width=20, anchor="center", command=self.insertnew)
        self.btn.place(x=180,y=370)

    def insertnew(self):
        global ReturnName,Age,path
        fname=self.Fname.get()
        lname=self.Lname.get()
        age=self.Age.get()
        gender=self.Gender.get()
        dob=self.Dob.get()
        #if(age<6 or age>9):
        #    tkinter.messagebox.showinfo("Error", "Age out of bounds, only 6 to 9")
        #    exit()
        dob=dob.replace("/","-")
        self.fullname = fname + " " + lname + " " + str(dob)
        self.fullname = self.fullname.lower()
        path = self.fullname
        ReturnName = self.fullname
        Age = age
        #Check entered details with existing details on firebase to verify staff or not
        print(self.Fname.get())
        db = firebase.database()
        data = {"fname": fname, "lname": lname, "age": age, "gender": gender}
        today = date.today()
        results = db.child("Student").child(self.fullname).set(data)
        db.child(str(today)).child(self.fullname).set(data)
        print(results)
        #to check if primary key aready EXISTS
        self.f.destroy()
        #global root
        self.f.quit()
        self.master.destroy()
        self.master.quit()

class Reports:
    def __init__(self, f,master):
        filepath=os.path.dirname(os.path.abspath(__file__))
        self.master=master
        self.f=f
        today = str(date.today())
        try:
            nameswithdob = database.child(today).get().val()
        except:
            pass
        print(nameswithdob)
        print('*'*10)
        lineslist = []
        try:
            for items in nameswithdob.keys():
                try:
                    resdict = database.child(today).child(items).get().val()
                    lineslist.append(str(resdict['fname'])+','+str(resdict['lname'])+','+str(resdict['age'])+','+str(resdict['RPM'])+','+str(round(resdict['BST'],3))+','+str(resdict['GDT'])+','+str(round(resdict['VL'],3)))
                except:
                    pass
        except:
            tkinter.messagebox.showinfo("Error", "No tests were taken today!")
            exit()
        print(lineslist)  
        with open(filepath+'/dailytest/'+today+'_IDreport.csv','w') as file:
            file.write('First Name,Last Name,Age,RPM,BST,GDT,Vineland')
            file.write('\n')
            for line in lineslist:
                file.write(line)
                file.write('\n')
        self.master.destroy()
       # dt = Details(self.master)
        #dt.details(fname,lname,dob)
       
'''
self.count keeps track of the age of the test that is currently being conducted
basal age is one  less than the count.
'''
class BST:
    def __init__(self,master,cage):
        self.cage = cage
        filepath=os.path.dirname(os.path.abspath(__file__))+"/tests"
        self.df = pd.read_csv(filepath+'/BST/bst.csv')
        self.master=master
        self.images = [filepath+"/BST/age3.png",filepath+"/BST/age4.png","",filepath+"/BST/age6.png",filepath+"/BST/age7.png",filepath+"/BST/age8.png","",""]
        self.count = 3
        self.basalage = 2.0
        self.additive_age = 0.0
        self.questioncount = 0
        self.i=0
        self.q = 0
        self.frame1 = Frame(self.master, width=500, height=50)
        self.frame1.pack(side=TOP)
        self.frame2 = Frame(self.master, width=500, height=75)
        self.frame2.pack(side=TOP)
        self.frame3 = Frame(self.master, width=500, height=75)
        self.frame3.pack(side=TOP)
        self.frame4 = Frame(self.master, width=500, height=75)
        self.frame4.pack(side=TOP)
        self.frame5 = Frame(self.master, width=500, height=75)
        self.frame5.pack(side=TOP)
        self.frame6 = Frame(self.master, width=500, height=75)
        self.frame6.pack(side=TOP)
        self.frame7 = Frame(self.master, width=500, height=75)
        self.frame7.pack(side=BOTTOM)
        self.frame = [self.frame1,self.frame2,self.frame3,self.frame4,self.frame5,self.frame6]
        self.agelabel = Label(self.frame1,text="Age test: "+str(self.count),bg='black',fg='white')
        self.agelabel.place(x=250,y=25,anchor="center")
        self.nextb = Button(self.frame7,text="next",command=self.next_btn)
        self.nextb.place(x=250, y =25, anchor="center")
        self.opt_selected1 = IntVar()
        self.opt_selected2 = IntVar()
        self.opt_selected3 = IntVar()
        self.opt_selected4 = IntVar()
        self.opt_selected5 = IntVar()
        self.opt_selected = [self.opt_selected1,self.opt_selected2,self.opt_selected3,self.opt_selected4,self.opt_selected5]
        self.opts1 = self.create_options(self.frame2,0)
        self.opts2 = self.create_options(self.frame3,1)
        self.opts3 = self.create_options(self.frame4,2)
        self.opts4 = self.create_options(self.frame5,3)
        self.opts5 = self.create_options(self.frame6,4)
        self.ques = self.create_q()

    def create_q(self):
        for i in range(0,5):
            self.opt_selected[i].set(0)
        self.displayquestion1= Label(self.frame2,text="",wraplength=450,justify="left")
        self.displayquestion1.place(x=2,y=25)
        self.displayquestion2= Label(self.frame3,text="",wraplength=450,justify="left")
        self.displayquestion2.place(x=2,y=25)
        self.displayquestion3= Label(self.frame4,text="",wraplength=450,justify="left")
        self.displayquestion3.place(x=2,y=25)
        self.displayquestion4= Label(self.frame5,text="",wraplength=450,justify="left")
        self.displayquestion4.place(x=2,y=25)
        self.displayquestion5= Label(self.frame6,text="",wraplength=450,justify="left")
        self.displayquestion5.place(x=2,y=25)
        self.question = [self.displayquestion1,self.displayquestion2,self.displayquestion3,self.displayquestion4,self.displayquestion5]
        agecase = {3:self.bs,4:self.bs4,5:self.bs,6:self.bs,7:self.bs,8:self.bs,9:self.bs,10:self.bs,11:self.finish}
        self.agelabel['text'] = "Age test: "+str(self.count)
        if self.count==5:
            self.frame6.pack(side=TOP)
        agecase[self.count](self.q)

    def bs(self,i):
        X = self.df.iloc[:,i]
        for i in range(0,5):
            q=self.question[i]
            q['text'] = X[i]
        if self.images[self.q]!="":
            self.root1 = Toplevel()
            photo = Image.open(self.images[self.q])
            photo = photo.resize((500, 500), Image.ANTIALIAS)
            self.render1 = ImageTk.PhotoImage(photo)
            photolabel = Label(self.root1,image=self.render1)
            photolabel.image = self.render1
            photolabel.pack()
        self.q+=1

    def bs4(self,i):
        X = self.df.iloc[:,i]
        self.frame6.pack_forget()
        for i in range(0,4):
            q=self.question[i]
            q['text'] = X[i]
        self.root1 = Toplevel()
        photo = Image.open(self.images[1])
        photo = photo.resize((500, 300), Image.ANTIALIAS)
        self.render = ImageTk.PhotoImage(photo)
        photolabel = Label(self.root1,image=self.render)
        photolabel.image = self.render
        photolabel.pack()
        self.q+=1

    def finish(self,i):
        while self.additive_age >= 12:
            self.basalage+=1
            self.additive_age-=12
        print("Additive age is "+str(self.additive_age))
        print("Cage is "+str(self.cage))
        self.basalage*=12
        self.basalage+=self.additive_age
        print("Basal age is "+str(self.basalage))
        self.iq = ((self.basalage)/(self.cage*12))*100
        print("IQ is "+str(self.iq))
        for i in range (1,6):
            self.frame[i].destroy()
        self.agelabel['text'] = "IQ is: "+str(self.iq)
        strid = ""
        if self.iq <24:
            strid = "Profound Intellectual Disability"
        elif self.iq <40:
            strid = "Severe Intellectual Disability"
        elif self.iq <55:
            strid = "Moderate Intellectual Disability"
        elif self.iq < 70:
            strid = "Mild Intellectual Disability"
        else:
            strid = "Not Intellectual Disability"
        if self.basalage//12 < 3:
            self.iq = 0
        frame = Frame(self.master,width = 500, height = 300)
        frame.pack(side=TOP)
        frame.configure(background='peach puff')
        label = Label(frame,text=strid)
        label.place(x=250,y=150,anchor='center')
        self.returnval = self.iq 
        self.frame7.destroy()
        self.frame8 = Frame(self.master, width=500, height=75)
        self.frame8.pack(side=BOTTOM)
        self.qui = Button(self.frame8,text="next",command=self.des)
        self.qui.place(x=250, y =25, anchor="center")

    def des(self):
        self.master.destroy()
        self.master.quit()

    def create_options(self,frame,n):
        b_val = 0
        b = []
        btn = Radiobutton(frame, text="Yes",variable=self.opt_selected[n],value=b_val+1)
        b.append(btn)
        btn.place(x=490,y=30,anchor="e")
        return b

    def next_btn(self):
        for i in range(0,5):
            if self.opt_selected[i].get() == 1:
                self.questioncount+=1
                print(str(self.questioncount))
        if self.questioncount == 0:
            self.count = 11
        else:
            if self.count != 4:
                if self.questioncount == 5:
                    self.basalage+=1
                else:
                    self.additive_age+=2.4*self.questioncount
                self.root1.destroy()

            if self.count == 4:
                if self.questioncount == 4:
                    self.basalage+=1
                else:
                    self.additive_age+=3*self.questioncount
                self.root1.destroy()
            self.count+=1
            self.questioncount = 0
        self.root1.destroy()
        for i in range(0,5):
            q=self.question[i]
            q.destroy()
        self.create_q()
    
    def getresult(self):
        return self.returnval

class GDT:
    def __init__(self,master,cage):
        filepath=os.path.dirname(os.path.abspath(__file__))+"/tests"
        self.cage = cage
        self.master=master
        self.count = 0
        self.frame1 = Frame(self.master,width=500,height=475)
        self.frame1.pack(side=TOP)
        self.frame2 = Frame(self.master,height=25,width=500)
        self.frame2.pack(side=BOTTOM)
        self.nextbtn = Button(self.frame2, text= "Next", command = self.next)
        self.nextbtn.place(x= 250, y= 12.5, anchor= "center")
        self.opt_selected1 = IntVar()
        self.opt_selected2 = IntVar()
        self.opt_selected3 = IntVar()
        self.opt_selected4 = IntVar()
        self.opt_selected5 = IntVar()
        self.opt_selected6 = IntVar()
        self.opt_selected7 = IntVar()
        self.opt_selected8 = IntVar()
        self.opt_selected9 = IntVar()
        self.opt_selected10 = IntVar()
        self.opt_selected11 = IntVar()
        self.opt_selected = [self.opt_selected1,self.opt_selected2, self.opt_selected3, self.opt_selected4,self.opt_selected5, self.opt_selected6, self.opt_selected7, self.opt_selected8, self.opt_selected9, self.opt_selected10]
        self.opts1 = self.create_options(self.frame1,0)
        self.opts2 = self.create_options(self.frame1,1)
        self.opts3 = self.create_options(self.frame1,2)
        self.opts4 = self.create_options(self.frame1,3)
        self.opts5 = self.create_options(self.frame1,4)
        self.opts6 = self.create_options(self.frame1,5)
        self.opts7 = self.create_options(self.frame1,6)
        self.opts8 = self.create_options(self.frame1,7)
        self.opts9 = self.create_options(self.frame1,8)
        self.opts10 = self.create_options(self.frame1,9)
        self.createq()
        self.q = [filepath+"/GDT/GDT1.png", filepath+"/GDT/GDT2.png", filepath+"/GDT/GDT3.png", filepath+"/GDT/GDT4.png", filepath+"/GDT/GDT5.png", filepath+"/GDT/GDT6.png", filepath+"/GDT/GDT7.png", filepath+"/GDT/GDT8.png", filepath+"/GDT/GDT9.png", filepath+"/GDT/GDT10.png", filepath+"/GDT/GDT11.png", filepath+"/GDT/GDT12.png", filepath+"/GDT/GDT13.png", filepath+"/GDT/GDT14.png", filepath+"/GDT/GDT15.png", filepath+"/GDT/GDT16.png", filepath+"/GDT/GDT17.png", filepath+"/GDT/GDT18.png", filepath+"/GDT/GDT19.png", filepath+"/GDT/GDT20.png", filepath+"/GDT/GDT21.png", filepath+"/GDT/GDT22.png", filepath+"/GDT/GDT23.png", filepath+"/GDT/GDT24.png"  ]
        self.qn =0
        self.age = cage
        self.agegroup = [3,6,8,11,13,17,20,24]




    def create_q(self,frame1,qn):
       photo = Image.open(self.q[qn])
       photo = photo.resize((500, 300), Image.ANTIALIAS)
       self.render = ImageTk.PhotoImage(photo)
       photolabel = Label(frame1,image=self.render)
       photolabel.image = self.render
       photolabel.pack()
       return photolabel

    def checkans(self):
        self.qn+=1
        if self.opt_selected11.get() == 1:
            self.count+=1
        if self.qn>= self.agegroup[self.age-3]:
            self.result()
        else:
            self.opt_selected11.set(0)
            self.dispq(self.qn)

    def dispq(self,n):
        photo = Image.open(self.q[n])
        photo = photo.resize((500, 300), Image.ANTIALIAS)
        self.render = ImageTk.PhotoImage(photo)
        self.ques['image'] = self.render

    def result(self):
        filepath=os.path.dirname(os.path.abspath(__file__))+"/tests"
        df = pd.read_csv(filepath+"/GDT/GDT.csv")
        X =df.iloc[:, 0:8]
        result = X.iloc[self.count, self.age-3]
        print(str(result)) #printing percentile
        self.frame3.pack_forget()
        if result<=10:
            strid = "Definitely below required: Intellectual Disability"
            ID = True
        elif result<=20:
            strid = "Below required: Intellectual Disability"
            ID = True
        else:
            strid = "Normal"
            ID =False
        self.frame1.destroy()
        self.frame1 = Frame(self.master,width=500,height=450)
        self.frame1.pack(side=TOP)
        self.frame1.configure(background='peach puff')  
        labelid = Label(self.frame1, text = strid)
        labelid.place(x= 250, y =225, anchor = "center" )
        self.nextbtn['command'] = self.nexttest
        
        self.returnval = int(result) 


    def nexttest(self):
        self.master.destroy()
        self.master.quit()

    def createq(self):
        n = 0
        q1 = Label(self.frame1,text="Palmer hold on writing instruments:")
        q1.place(x=0,y=23.5+23.5*2*n,anchor="w")
        n+=1
        q2 = Label(self.frame1,text="Spontaneous scribble:")
        q2.place(x=0,y=23.5+23.5*2*n,anchor="w")
        n+=1
        q3 = Label(self.frame1,text="Purposive horizontal scribble:")
        q3.place(x=0,y=23.5+23.5*2*n,anchor="w")
        n+=1
        q1 = Label(self.frame1,text="Makes dots:")
        q1.place(x=0,y=23.5+23.5*2*n,anchor="w")
        n+=1
        q1 = Label(self.frame1,text="Tripod hold on writing instruments:")
        q1.place(x=0,y=23.5+23.5*2*n,anchor="w")
        n+=1
        q1 = Label(self.frame1,text="Purposive vertical scribble:")
        q1.place(x=0,y=23.5+23.5*2*n,anchor="w")
        n+=1
        q1 = Label(self.frame1,text="Imitates vertical strokes:")
        q1.place(x=0,y=23.5+23.5*2*n,anchor="w")
        n+=1
        q1 = Label(self.frame1,text="Extends tail to dots in different directions:")
        q1.place(x=0,y=23.5+23.5*2*n,anchor="w")
        n+=1
        q1 = Label(self.frame1,text="Imitates horizontal strokes:")
        q1.place(x=0,y=23.5+23.5*2*n,anchor="w")
        n+=1
        q1 = Label(self.frame1,text="Traces outline of objects/ palm on paper:")
        q1.place(x=0,y=23.5+23.5*2*n,anchor="w")


    def create_options(self,frame,n):
        b_val = 0
        b = []
        btn = Radiobutton(frame, text="Yes",variable=self.opt_selected[n],value=b_val+1)
        b.append(btn)
        btn.place(x=490,y=(23.5+23.5*2*n),anchor="e")
        return b

    def next(self):
        for i in range(0,9):
            if self.opt_selected[i].get() == 1:
                self.count+=1
        self.frame1.destroy()
        self.frame3 = Frame(self.master, width =500, height=25 )
        self.frame3.pack(side = BOTTOM)
        self.frame1 = Frame(self.master,width=500,height=450)
        self.frame1.pack(side=TOP)
        self.nextbtn['command'] = self.checkans
        btn = Radiobutton(self.frame3, text="Yes",variable=self.opt_selected11,value=1)
        btn.place(y= 10, x =250, anchor = "center")
        self.ques = self.create_q(self.frame1, self.qn)

    def getresult(self):
        return self.returnval

q= ["A1.png", "A2.png", "A3.png", "A4.png", "A5.png", "A6.png", "A7.png", "A8.png", "A9.png", "A10.png", "A11.png", "A12.png", "A13.png", "A14.png", "A15.png", "A16.png", "A17.png", "A18.png", "A19.png", "A20.png", "A21.png", "A22.png", "A23.png", "A24.png", "A25.png", "A26.png", "A27.png", "A28.png", "A29.png", "A30.png", "A31.png", "A32.png", "A33.png", "A34.png", "A35.png", "A36.png", "A37.png", "A38.png", "A39.png", "A40.png", "A41.png", "A42.png", "A43.png", "A44.png", "A45.png", "A46.png", "A47.png", "A48.png", "A49.png", "A50.png", "A51.png", "A52.png", "A53.png", "A54.png", "A55.png", "A56.png", "A57.png", "A58.png", "A59.png", "A60.png"]
options = [["1","2","3","4","5","6"], ["1","2","3","4","5","6","7","8"]]
a = [4,5,1,2,6,3,6,2,1,3,5,4,2,6,1,2,1,3,5,6,4,3,4,5,8,2,3,8,7,4,5,1,7,6,1,2,3,4,3,7,8,6,5,4,1,2,5,6,7,6,8,2,1,5,2,4,1,6,3,5]

class RPM:
    def __init__(self,master,cage):
        self.cage = cage 
        self.master=master
        self.result = 0
        self.result_wrong_counter = 0
        self.frame1= Frame(master,width=500, height=400)
        self.frame1.pack(side=TOP)
        self.frame2= Frame(master,width=500, height=100)
        self.frame2.pack(side=BOTTOM)
        self.opt_selected = IntVar()
        self.qn = 0
        self.ques = self.create_q(self.frame1,self.qn)
        self.opts = self.create_options(self.frame2,6)
        self.display_q(self.qn)
        self.returnval=0

    def next_btn(self, value):
        print(value)
        self.opt_selected = value
        if self.check_q(self.qn):
            self.result+=1
            print("correct "+str(self.qn+1))
        else:
            print('wrong '+str(self.qn+1))
        if self.result_wrong_counter == 3:
            self.nextsection()
        self.qn+=1
        if self.qn >= len(q):
            self.print_result()

        else:
            self.display_q(self.qn)

    def nextsection(self):
        if self.qn < 12:
            self.qn = 11
        elif self.qn < 24:
            self.qn = 23
        elif self.qn < 36:
            self.qn = 35
        elif self.qn < 48:
            self.qn = 47
        else:
            self.qn = 59
        self.result_wrong_counter = 0

    def mapvalue(self):
        if self.cage>=6 and self.cage<7:
            self.map=0
        elif self.cage>=7 and self.cage<8:
            self.map=1
        elif self.cage>=8 and self.cage<9:
            self.map=2
        elif self.cage>=9 and self.cage<10:
            self.map=3
        elif self.cage>=10 and self.cage<11:
            self.map = 4
        
    def print_result(self):
        filepath=os.path.dirname(os.path.abspath(__file__))+"/tests"
        df = pd.read_csv(filepath+'/RPM/rpmresult.csv')
        X = df.iloc[:,1:6]
        self.mapvalue()
        result = X.iloc[self.result,self.map] 
        print(result)
        self.frame1.destroy()
        self.frame2.destroy()
        self.frame1 = Frame(self.master, width=500, height=500)
        self.frame1.pack()
        printresult = Label(self.frame1, text="Score is "+str(result))
        printresult.place(x=250,y=240,anchor="center")
        if(result<26):
            self.frame1.configure(background='peach puff')  
            printid = Label(self.frame1, text="Test FAILED: Intellectual Disability")
            printid.place(x=250,y=260,anchor="center")
        else:
            self.frame1.configure(background='peach puff')   
            printid = Label(self.frame1, text="Test PASSED: Normal")
            printid.place(x=250,y=260,anchor="center")
        self.nexttest = Button(self.frame1,text="Next Test",command=self.next)
        self.nexttest.place(x=250,y=490,anchor="center")
        self.returnval = int(result) #return to calling function 

    def next(self):
        self.master.destroy()
        self.master.quit()

    def check_q(self,qn):
        print(self.opt_selected)
        if self.opt_selected == a[qn] :
            self.result_wrong_counter = 0
            return True
        self.result_wrong_counter+=1
        return False

    def display_q(self,qn):
        filepath=os.path.dirname(os.path.abspath(__file__))+"/tests"
        b_val = 0
        num = 0
        photo = Image.open(filepath+"/RPM/"+q[qn])
        photo = photo.resize((500, 400), Image.ANTIALIAS)
        self.render = ImageTk.PhotoImage(photo)
        self.opt_selected = 0 
        self.ques['image'] = self.render
        if (qn>=24):
            num = 1
        if (qn==24):
            self.frame2.destroy()
            self.frame2= Frame(self.master,width=500, height=100)
            self.frame2.pack(side=BOTTOM)
            self.opts = self.create_options(self.frame2,8)
        for op in options[num]:
            self.opts[b_val]['text'] = op
            b_val = b_val + 1

    def create_q(self,frame1,qn):
       filepath=os.path.dirname(os.path.abspath(__file__))+"/tests"
       photo = Image.open(filepath+"/RPM/"+q[qn])
       photo = photo.resize((500, 300), Image.ANTIALIAS)
       self.render = ImageTk.PhotoImage(photo)
       photolabel = Label(frame1,image=self.render)
       photolabel.image = self.render
       photolabel.pack()
       return photolabel

    def create_options(self,frame2,n):
        b_val = 0
        b = []
        while b_val<n:
            print(b_val)
            btn = Button(frame2, text= str(b_val+1), command = lambda i = b_val+ 1 :self.next_btn(i), width = 5, height = 3)
            b.append(btn)
            btn.pack(side=LEFT,anchor="w")
            b_val=b_val+1
        return b

    def getresult(self):
        return self.returnval

yes =0
no=0
might=0
basal_age=0
vli=0
index_arr = [0] * 90
agetoadd = 0
age_range = {0:[1,17],1:[18,34],2:[35,44],3:[45,50],4:[51,56],5:[57,61],6:[45,65],7:[51,70],8:[57,74],9:[62,77]}
cage = 6
vlf = age_range[cage][1]

class Question:
    def __init__(self, question, answers):
        self.question = question
        self.answers = answers
        global vli
        vli = 0

    def check(self, letter, view):
        global yes
        global no
        global might
        global basal_age
        global index_arr
        global vli
        global vlf
        global agetoadd
        agemap = {0:0.7, 34:1.2, 44:2, 56:2.4, 61:3, 65:2.4, 70:3, 74:4, 77:3}
        for (k, v) in agemap.items():
            if vli == k:
                agetoadd = v

        if(letter == "A"):
            label = Label(view, text="Yes")
            yes += 1
            if(vli==15 or vli==32):
                basal_age=round(basal_age+0.1,2)
            basal_age=round(basal_age+agetoadd,2)
            vli += 1
            index_arr[vli] = 1
        elif(letter == "B"):
            label = Label(view, text="No")
            no +=1
            vli += 1
            index_arr[vli] = 0
        else:
            label = Label(view, text="Could have passed")
            might +=1
            basal_age += agetoadd/2.0
            vli += 1
            index_arr[vli] = 2

        if (index_arr[vli]==1 and index_arr[(vli)-2]==1 and index_arr[(vli)-1]==2):
            current=self.mapmaybeage(vli)
            previous=self.mapmaybeage(vli-1)
            if current == previous:
                basal_age += agetoadd/2.0
            else:
                basal_age+= agemap[previous]/2.0
        print("current basal age is ")
        print(basal_age, " months")

        label.pack()
        view.after(1, lambda *args: self.unpackView(view))

    def mapmaybeage(self,vli):
        if vli < 34:
            return 0
        elif vli<44:
            return 34
        elif vli<56:
            return 44
        elif vli<61:
            return 56
        elif vli<65:
            return 61
        elif vli<70:
            return 65
        elif vli<74:
            return 70
        elif vli<77:
            return 74
        elif vli<81:
            return 77

    def getView(self, window,REF):
        view = Frame(window)
        Label(view, text=self.question).pack()
        self.REF = REF
        Button(view, text=self.answers[0], command=lambda *args: self.check("A", view),width=50).pack()
        Button(view, text=self.answers[1], command=lambda *args: self.check("B", view),width=50).pack()
        Button(view, text=self.answers[2], command=lambda *args: self.check("C", view),width=50).pack()

        return view

    def unpackView(self, view):
        view.pack_forget()
        self.REF.askQuestion()

questions = []
filepath=os.path.dirname(os.path.abspath(__file__))+"/tests"
file = open(filepath+"/VL/vineland2questions.txt", "r",encoding='windows-1252')
line = file.readline()
while(line != ""):
    questionString = line
    answers = []
    for vli in range (3):
        answers.append(file.readline())
    questions.append(Question(questionString, answers))
    line = file.readline()
file.close()

number_of_questions = len(questions)

class Report:
    def __init__(self):
        self.pdf = FPDF() 
    def genrep(self,name,age,sch,rpm,gdt,bst,vi):
        self.pdf.add_page()
        self.text = 'Final report'
        self.name = name
        self.rpm  = rpm
        self.gdt = gdt
        self.bst = bst
        self.vi = vi
        self.age = age
        self.sch = sch

        #Setting the threshold values for each test
        self.rpmv =26
        self.gdtv =20
        self.bstv =70
        self.viv =70
        #Final report text
        self.pdf.set_font("Arial",size=24)
        self.pdf.cell(60, 10,txt=self.text,ln = 50,align="L")
        #First Sep line
        self.pdf.set_draw_color(0, 0, 0)
        self.pdf.set_line_width(0.5)
        self.pdf.line(0, 20, 500, 20)
        #Vertical line
        self.pdf.set_draw_color(0, 0, 0)
        self.pdf.set_line_width(0.5)
        self.pdf.line(10, 0, 10, 1000)
        
        #Displaying student details
        #Name
        self.pdf.set_font("Arial",size=14)
        self.pdf.cell(60,7,txt="Name:"+self.name,ln = 1,align="L")
        #Age
        self.pdf.set_font("Arial",size=14)
        self.pdf.cell(60, 7,txt="Age:"+str(self.age),ln = 1,align="L")
        #School
        self.pdf.set_font("Arial",size=14)
        self.pdf.cell(60, 7,txt="School:"+self.sch,ln = 1,align="L")
        #Bottom Line for the report 
        self.pdf.set_draw_color(0, 0, 0)
        self.pdf.set_line_width(0.5)
        self.pdf.line(0, 40, 500, 40)
        #Report Image
        filepath=os.path.dirname(os.path.abspath(__file__))
        self.path = filepath+'/Images/Report.png'
        self.pdf.image(self.path, x = 15, y = 150, w = 200, h =100)

        #Data list to plot the data
        self.data = [['Name of the test','Expected Score','Score Obtained','Remark']]

        #Adding the scores to data lsit
        #RPM
        self.temp = []
        self.temp.append("RPM")
        self.temp.append(str(self.rpmv))
        self.temp.append(str(self.rpm))
        if self.rpm < 6:
            self.temp.append("Severe Intellectual Disability")
        elif self.rpm < 11:
            self.temp.append("Moderate Intellectual Disability")
        elif self.rpm < 26:
            self.temp.append("Mild Intellectual Disability")
        else:
            self.temp.append("Normal Score")
        self.data.append(self.temp)
        
        #GDT
        self.temp = []
        self.temp.append("GDT")
        self.temp.append(str(self.gdtv))
        self.temp.append(str(self.gdt))
        if self.gdt < 6:
            self.temp.append("Severe Intellectual Disability")
        elif self.gdt < 11:
            self.temp.append("Moderate Intellectual Disability")
        elif self.gdt < 26:
            self.temp.append("Mild Intellectual Disability")
        else:
            self.temp.append("Normal Score")
        self.data.append(self.temp)

        #BST
        self.temp = []        
        self.temp.append("BST")
        self.temp.append(str(self.bstv))
        self.temp.append(str(round(self.bst,3)))
        if self.bst == 0:
            self.temp.append("N/A")
        elif self.bst < 20:
            self.temp.append("Profound Intellectual Disability")
        elif self.bst < 36:
            self.temp.append("Severe Intellectual Disability")
        elif self.bst < 52:
            self.temp.append("Moderate Intellectual Disability")
        elif self.bst < 70:
            self.temp.append("Mild Intellectual Disability")
        else:
            self.temp.append("Normal Score")
        self.data.append(self.temp)

        #VI
        self.temp = []        
        self.temp.append("VI")
        self.temp.append(str(self.viv))
        self.temp.append(str(round(self.vi,3)))
        if self.vi < 20:
            self.temp.append("Profound Intellectual Disability")
        elif self.vi < 36:
            self.temp.append("Severe Intellectual Disability")
        elif self.vi < 52:
            self.temp.append("Moderate Intellectual Disability")
        elif self.vi < 70:
            self.temp.append("Mild Intellectual Disability")
        else:
            self.temp.append("Normal Score")
        self.data.append(self.temp)
        
        #Setting table parameters
        self.col_width = self.pdf.w / 4.5
        self.row_height = self.pdf.font_size+2
        self.spacing = 2
        #Drawing the table
        for row in self.data:
            for item in row:
                self.pdf.cell(self.col_width, self.row_height*self.spacing,txt=item, border=1)
            self.pdf.ln(self.row_height*self.spacing)
        self.pdf.output(filepath+"/Reports/"+self.name+".pdf")
        
class Caller:
    def __init__(self,age):
        global cage,vlf
        cage = age
        vlf = age_range[cage][1]
        self.window = Tk()
        w = 600
        h = 500
            # get screen width and height
        ws = self.window.winfo_screenwidth() # width of the screen
        hs = self.window.winfo_screenheight() # height of the screen
            # calculate x and y coordinates for the Tk root window
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
            # set the dimensions of the screen
            # and where it is placed
        self.window.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.window.title("Vineland Social Maturity Test")
        label_heading = Label(self.window, text="VINELAND SOCIAL MATURITY TEST",bg="black",fg="white",font=('Helvetica', '20'))
        label_heading.pack()
        self.label_des = Label(self.window, text="\n\nThe Vineland Social Maturity Scale (VSMS) measures the differential social\ncapacities of an individual. It provides an estimate of Social Age (SA) and Social\nQuotient (SQ), and shows high correlation (0.80) with intelligence. It is designed to\nmeasure social maturation in eight social areas: Self-help General (SHG), Self-help\nEating (SHE), Self-help Dressing (SHD), Self direction (SD), Occupation (OCC),\nCommunication (COM), Locomotion (LOM), and Socialization (SOC).",fg="blue",font=('15'))
        self.label_des.pack()
        self.button = Button(self.window, text="Start", command=self.askQuestion)
        self.button.pack()
        self.window.mainloop()

    def askQuestion(self):
        global questions, button, yes, no,might, number_of_questions,social_quotient,index_arr,vlf,vli
        window = self.window
        if(vli == vlf):
            Label(window,text="Thank you for answering the questions.\n basal age = " + str(basal_age)).pack()
            global cage
            social_quotient=(basal_age/(cage*12))*100#chrono age taken as 10 as all question included are till 9-10 yearsold
            Label(window, text="social quotient = " + str(social_quotient)).pack()
            if(social_quotient<25):
                ID = True
                Label(window, text="Profound Intelletual disability").pack()
            elif((social_quotient>=25) and(social_quotient<40)):
                ID = True
                Label(window, text="Severe Intelletual disability").pack()
            elif((social_quotient>=40) and (social_quotient<55)):
                ID = True
                Label(window, text="Moderate Intelletual disability").pack()
            elif((social_quotient>=55) and (social_quotient<70)):
                ID = True
                Label(window, text="Mild Intelletual disability").pack()
            else:
                ID = False
                Label(window, text="Normal IQ").pack()
            window.configure(background='peach puff')
            buttonn = Button(window,text="Next",command=self.quitf)
            buttonn.pack(side=BOTTOM)
            self.returnval = float(social_quotient) 
            return
        self.button.pack_forget()
        self.label_des.pack_forget()
        questions[vli].getView(window,self).pack() 
        
    def quitf(self):
        self.window.destroy()
        self.window.quit()

    def getresult(self):
        return self.returnval   

def RPMCALL():
    global Age
    root = Tk()
    w = 500 # width for the Tk root
    h = 500 # height for the Tk root
    # get screen width and height
    ws = root.winfo_screenwidth() # width of the screen
    hs = root.winfo_screenheight() # height of the screen
    # calculate x and y coordinates for the Tk root window
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    # set the dimensions of the screen
    # and where it is placed
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    root.title("Ravens Progressive Matrix")
    RPMcall = RPM(root,Age)
    root.mainloop()
    global RPMresult
    RPMresult=RPMcall.getresult()

def BSTCALL():
    global Age
    root = Tk()
    w = 500 # width for the Tk root
    h = 500 # height for the Tk root
    # get screen width and height
    ws = root.winfo_screenwidth() # width of the screen
    hs = root.winfo_screenheight() # height of the screen
    # calculate x and y coordinates for the Tk root window
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    # set the dimensions of the screen
    # and where it is placed
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    root.title("Binet Simon Test")
    BSTcall = BST(root,Age)
    root.mainloop()
    global BSTresult
    BSTresult=BSTcall.getresult()

def GDTCALL():
    global Age
    root = Tk()
    w = 500 # width for the Tk root
    h = 500 # height for the Tk root
    # get screen width and height
    ws = root.winfo_screenwidth() # width of the screen
    hs = root.winfo_screenheight() # height of the screen
    # calculate x and y coordinates for the Tk root window
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    # set the dimensions of the screen
    # and where it is placed
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    root.title("Gessel's Drawing Test")
    GDTcall = GDT(root,Age)
    root.mainloop() 
    global GDTresult
    GDTresult=GDTcall.getresult()

def VLCALL():
    global Age
    c = Caller(Age)
    global VLresult
    VLresult = c.getresult()

def gph():
    global RPMresult,BSTresult,GDTresult,VLresult,RPMresultl,BSTresultl,GDTresultl,VLresultl
    root = Tk()
    w = 500 # width for the Tk root
    h = 500 # height for the Tk root
    # get screen width and height
    ws = root.winfo_screenwidth() # width of the screen
    hs = root.winfo_screenheight() # height of the screen
    # calculate x and y coordinates for the Tk root window
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    # set the dimensions of the screen
    # and where it is placed
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    frame = Frame(root,width=750,height=750)
    frame.pack()
    plt = Plot(frame)
    BSTresultl.append(BSTresult)
    RPMresultl.append(RPMresult)
    VLresultl.append(VLresult)
    GDTresultl.append(GDTresult)
    plt.plot(BSTresultl,RPMresultl,GDTresultl,VLresultl)
    root.mainloop() 

def TAKETEST():
    global test_number,BSTresult,GDTresult,VLresult,RPMresult,pathdir
    global RPMresultl,BSTresultl,GDTresultl,VLresultl 
    global Name,Age
    RPMresultl = []
    BSTresultl = []
    GDTresultl = []
    VLresultl = []
    test_number+=1
    #RPMCALL()
    #BSTCALL()
    #GDTCALL()
    VLCALL()
    resulttodb = {"RPM":RPMresult, "BST":BSTresult,"VL":VLresult,"GDT":GDTresult}
    database.child("Student").child(pathdir).update(resulttodb)
    database.child(today).child(pathdir).update(resulttodb)
    gph()
    r = Report()
    r.genrep(Name,Age,"SSRVM BANGALORE EAST",RPMresult,GDTresult,BSTresult,VLresult)

def FIREBASECALL():
    root = Tk()
    w=500
    h=500
    # get screen width and height
    ws = root.winfo_screenwidth() # width of the screen
    hs = root.winfo_screenheight() # height of the screen
    # calculate x and y coordinates for the Tk root window
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    # set the dimensions of the screen
    # and where it is placed
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    root.title("Login")
    root.configure(background='peach puff')
    f = Frame(root,width=750,height=750)
    f.configure(background='peach puff')
    f.pack()
    login = LoginTeacher(f,root,test_number)
    root.mainloop()
    global Name,Age,pathdir
    choice = login.returnchoice()
    if choice == 1:
        Name,pathdir = login.returnnametocalling()
        Age = login.returnagetocalling()
        TAKETEST()

FIREBASECALL()

from tkinter import *
from PIL import ImageTk, Image
import os
import tkinter.messagebox
import pyrebase
from datetime import date

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
        page3 = Report(f2,self.master)


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
        if(age<6 or age>9):
            tkinter.messagebox.showinfo("Error", "Age out of bounds")
            exit()
        gender=self.Gender.get()
        dob=self.Dob.get()
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

class Report:
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
       

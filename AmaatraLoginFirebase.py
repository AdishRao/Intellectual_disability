from tkinter import *
from PIL import ImageTk, Image
import os
import tkinter.messagebox
import pyrebase
import datetime

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

class LoginTeacher:
    def __init__(self, f):
        self.f=f
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
            global user1
            user = auth.sign_in_with_email_and_password(email,password)
            user1 = user
            global info1
            info=auth.get_account_info(user['idToken'])
            info1 = info
            print(info)
            self.f.destroy()
            #global root#self.f1.title("RESTAURANT DETAILS AND CUISINE")
            f1 = Frame(root,width=500,height=500)
            f1.pack()
            page1 = Page1(f1)
        except:
            tkinter.messagebox.showinfo("No access", "Invalid email or password")

class Page1: #Intermediate window to choose new student, previous student or retake of test
    def __init__(self, f):
        self.f=f
        self.label_0 = Label(f, text="Choose Activity",width=20,font=("bold", 20))
        self.label_0.place(x=90,y=53)
        self.btn1 = Button(self.f, text='New Student',width=20, anchor="center",command=self.newstudent)
        self.btn1.place(x=160,y=310)
        self.btn2 = Button(self.f, text='Student Details',width=20, anchor="center", command=self.prevstudent)
        self.btn2.place(x=160,y=410)

    def newstudent(self):
        self.f.destroy()
        f1 = Frame(root,width=500,height=500)
        f1.pack()
        page2 = NewStudent(f1)

    def prevstudent(self):
        self.f.destroy()
        f2 = Frame(root,width=500,height=500)
        f2.pack()
        page3 = PrevStudent(f2)


class NewStudent:
    def __init__(self, f):
        self.f=f
        self.Fname=StringVar()
        self.Lname = StringVar()
        self.Gender=StringVar()
        self.Age = IntVar()

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

        self.btn = Button(f, text='Submit',width=20, anchor="center", command=self.insertnew)
        self.btn.place(x=180,y=320)

    def insertnew(self):
        fname=self.Fname.get()
        lname=self.Lname.get()
        age=self.Age.get()
        gender=self.Gender.get()
        global user1
        global info1
        fullname = fname + " " + lname
        fullname = fullname.lower()
        #Check entered details with existing details on firebase to verify staff or not
        print(self.Fname.get())
        db = firebase.database()
        data = {"fname": fname, "lname": lname, "age": age, "gender": gender}
        results = db.child("Student").child(fullname).set(data)
        print(results)
        #to check if primary key aready EXISTS

        self.f.destroy()
        #global root#self.f1.title("RESTAURANT DETAILS AND CUISINE")
        f1 = Frame(root,width=500,height=500)
        f1.pack()
        page10 = Page1(f1) #TODO

class PrevStudent:
    def __init__(self, f):
        self.f=f
        self.Fname=StringVar()
        self.Lname = StringVar()

        self.label_0 = Label(f, text="Previous Student Details",width=20,font=("bold", 15))
        self.label_0.place(x=140,y=53)

        self.label_1 = Label(f, text="First Name",width=20,font=("bold", 10))
        self.label_1.place(x=80,y=130)

        self.entry_1 = Entry(f, textvar=self.Fname)
        self.entry_1.place(x=240,y=130)

        self.label_2 = Label(f, text="Last Name",width=20,font=("bold", 10))
        self.label_2.place(x=79,y=180)

        self.entry_2 = Entry(f, textvar=self.Lname)
        self.entry_2.place(x=240,y=180)


        self.btn = Button(f, text='Submit',width=20, anchor="center", command=self.checkprev)
        self.btn.place(x=180,y=320)

    def checkprev(self):
        fname=self.Fname.get()
        lname=self.Lname.get()
        fullname = fname + " " + lname
        fullname=fullname.lower()
        db = firebase.database()
        results = db.child("Student").child(fullname).get()
        print("\n")
        #Display stats or move to the statistics page created earlier for tests taken by a student
        print(results.val())
        str = results.val()
        if(str==None):
            tkinter.messagebox.showinfo("Invalid", "No such student")
        else:
            self.f.destroy()
            #global root#self.f1.title("RESTAURANT DETAILS AND CUISINE")
            f1 = Frame(root,width=500,height=500)
            f1.pack()
            page11 = Page1(f1) #TODO


root = Tk()
root.geometry('500x500')
root.title("Amaatra-Login")
f = Frame(root,width=750,height=750)
f.pack()
login = LoginTeacher(f)
root.mainloop()

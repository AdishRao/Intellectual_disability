import sys
from tkinter import *
import random
from tkinter import ttk
import pandas as pd
from random import randint
import numpy as np
import pyrebase
import tkinter.messagebox

#firebase config
config = {
    "apiKey": "AIzaSyDc3JTW47RqgD1oAtbar5n4HZ6nDEVBXt4",
    "authDomain": "intellectualdisability-a9894.firebaseapp.com",
    "databaseURL": "https://intellectualdisability-a9894.firebaseio.com",
    "projectId": "intellectualdisability-a9894",
    "storageBucket": "intellectualdisability-a9894.appspot.com",
    "messagingSenderId": "255261471519"
}

firebase = pyrebase.initialize_app(config)
auth =firebase.auth()
uid = 0
rid = 0
ID = True
Sclass = ''
cage = 0
cname =""
gender=""

class login:
    def __init__(self,master,root):
        self.master = master
        self.root=root
        self.email = Label(master,text="Enter Email:")
        self.email.place(x=200,y=195,anchor="center")
        self.password = Label(master,text="Enter Password:")
        self.password.place(x=135,y=225)
        self.emailid= Entry(self.master)
        self.psswd= Entry(self.master)
        self.emailid.place(x=250,y=180)
        self.psswd.place(x=250,y=220)
        self.login = Button(master,text="Login",command=self.loginb)
        self.login.place(x=250,y=450,anchor="center")


    def loginb(self):
        try:
            email = self.emailid.get()
            password = self.psswd.get()
            #email = "user2@gmail.com"
            #password = "admin123"
            print(email)
            print(password)
            user = auth.sign_in_with_email_and_password(email,password)
            global uid, i, rid, mycursor
            #mycursor.execute("SELECT COUNT(*) FROM CHILD")
            #result = mycursor.fetchone()
            info=auth.get_account_info(user['idToken'])
            #uid=result[0]
            rid=str(info['users'][0]['localId'])
            #i=-5
            #global st
            #st =  2
            
            self.analysismain()
            
        except:
            tkinter.messagebox.showinfo("Error", "Invalid Email")
            self.emailid.destroy()
            self.psswd.destroy()
            self.emailid= Entry(self.master)
            self.psswd= Entry(self.master)
            self.emailid.place(x=250,y=180)
            self.psswd.place(x=250,y=220)

    def analysismain(self):
        global rid
        self.email.destroy()
        self.password.destroy()
        self.login.destroy()
        self.emailid.destroy()
        self.psswd.destroy()
        db = firebase.database()
        #sashwat@gmail.com
        #admin123
        scores = []
        friends = []
        myscore = child = db.child("Child").child(str(rid)).get().val()
        for uids in myscore:
            currscore = []
            for vals in myscore[uids]:
               currscore.append(myscore[uids][vals])
            scores.append(currscore)
        print(scores)
        i = len(scores) #This is for the user
        ins = scores.pop()
        scores.insert(0,ins)
        child = db.child("Child").get().val()
        for rids in child:
            compare = []
            if rids!= rid :
                for uids in child[rids]:
                    compareind = []
                    for rids1 in child[rids][uids]:
                        compareind.append(child[rids][uids][rids1])
                    compare.append(compareind)
                print("Compare",compare)
                print("scores",scores)
                passscore = scores
                if self.find_friend(compare,passscore):
                    friends.append(rids)
        print(friends)
        self.master.destroy()
        rowcount=3
        frame1 = Frame(self.root,width=500,height=50)
        frame1.pack()
        frame2 = Frame(self.root,width=500,height=450)
        frame2.pack()
        Label(frame1,text="SIMILAR PERFORMANCES").place(x=250,y=25,anchor="center")
        for i in friends:
            lab = Label(frame2,text=i)
            lab.grid(row=rowcount,column=0)
            Button(frame2,text="Contact", fg="Red").grid(row=rowcount,column=1)

    def find_friend(self,compare,scores):
        print("-------")
        i = len(compare) #this is for overall
        ins = compare.pop() #FB stores first test last and rest normally
        compare.insert(0,ins)
        varintest = []
        for testlist in range(i-1):
            indvar = []
            for tests in range (5):
                indvar.append(compare[testlist+1][tests]-compare[testlist][tests])
            varintest.append(indvar)
        print("var for all",varintest)
        i = len(scores) #This is for the user
        varintestforuser = []
        for testlist in range(i-1):
            indvar = []
            for tests in range (5):
                indvar.append(scores[testlist+1][tests]-scores[testlist][tests])
            varintestforuser.append(indvar)
            print("Var for user",varintestforuser)
        truth = []    
        for x,y in zip(varintest,varintestforuser):
            print("________________")
            count = 0
            for i in range(5):
                if abs(x[i]-y[i])<=5:
                    count+=1
            if count>=1:
                truth.append(True)
            else:
                return False
        return True
            
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
frame1 = Frame(root,width=500,height=500)
frame1.pack()
login = login(frame1,root)
root.mainloop()

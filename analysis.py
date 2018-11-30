#import mysql.connector
import sys
from tkinter import *
#from PIL import Image
#from PIL import ImageTk
import random
from tkinter import ttk
import pandas as pd
from random import randint
#import keras
#from keras import backend as K
#from keras.models import load_model
import numpy as np
#import datetime
import pyrebase
#from plotly.offline import iplot, init_notebook_mode
#import plotly.graph_objs as go
#import plotly.io as pio

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

mydb = mysql.connector.connect(host="localhost",user="sidd",passwd="123",database="ID",auth_plugin='mysql_native_password') #TODO change before pushing
mycursor = mydb.cursor()
uid = 0
rid = 0
ID = True
Sclass = ''
cage = 0
cname =""
gender=""

class login:
    def __init__(self,master):
        self.master = master
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
            self.master.destroy()
            analysismain(self)
            self.master.quit()
        except:
            self.errorlabel = Label(self.master, text = "Wrong email or password, try again!")
            self.errorlabel.pack(side=BOTTOM)
            self.emailid.destroy()
            self.psswd.destroy()
            self.emailid= Entry(self.master)
            self.psswd= Entry(self.master)
            self.emailid.place(x=250,y=180)
            self.psswd.place(x=250,y=220)

    def analysismain(self):
        self.master= master





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
login = login(root)
root.mainloop()

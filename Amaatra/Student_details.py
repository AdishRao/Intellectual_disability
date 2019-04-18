#This file os fpr students who login to take the tests for their nth time 
#Importing the req. libraries
from tkinter import *
from PIL import Image
from PIL import ImageTk
import os
import tkinter.messagebox
import pyrebase
import datetime
from firebase import firebase


#import all test classes classes
from tests.rpm import *
from tests.bst import *
from tests.gdt import *
from tests.vl import *
from graph import *
from AmaatraLoginFirebase import *

config = {
    "apiKey": "AIzaSyATuQBI1JJ9sI4jyLjvKbLQX6pzPeGfOMA",
    "authDomain": "amaatraid.firebaseapp.com",
    "databaseURL": "https://amaatraid.firebaseio.com",
    "projectId": "amaatraid",
    "storageBucket": "amaatraid.appspot.com",
    "messagingSenderId": "829220285103"
  }

firebase = firebase.FirebaseApplication("https://amaatraid.firebaseio.com")
res = firebase.put('/Student/Ag16-05-1998','BST','30/40')
print(res)
res = firebase.get('/StudentDetails/Ag16-05-1998',None)
print(res)
class Details:
    def __init__(self,master):
        self.master = master
        print("init")

    def details(self,fname,lname,dob):
        key = fname+lname+dob
        res = firebase.get('/StudentDetails/'+key,None)
        if res != 'None':
            tBST = res["BST"]
            tGDT = res["GDT"]
            tRPM = res["RPM"]
            tVI =  res["VI"]
            tBST = tBST.split("/")
            tRPM = tRPM.split("/")
            tGDT = tGDT.split("/")
            tVI = tVI.split("/")
            print(res)
            plt = Plot(self.master)
            plt.plot(tBST,tRPM,tGDT,tVI)
        else:
            Page1(self.master)


    def updatemarks(fname,lname,dob,BST,GDT,RPM,VI):
        key = fname+lname+dob
        res = firebase.get('/StudentDetails/'+key,None)
        tBST = res["BST"]
        tGDT = res["GDT"]
        tRPM = res["RPM"]
        tVI =  res["VI"]
        tBST = t+BST+"/"
        tRPM = t+RPM+"/"
        tGDT = t+GDT+"/"
        tVI = t+VI+"/"
        firebase.put('/StudentDetails/Ag16-05-1998','BST',tBST)
        firebase.put('/StudentDetails/Ag16-05-1998','GDT',tGDT)
        firebase.put('/StudentDetails/Ag16-05-1998','RPM',tRPM)
        firebase.put('/StudentDetails/Ag16-05-1998','VI',tVI)
        res = firebase.get('/StudentDetails/'+key,None)
        print("Updated",res)
        



    




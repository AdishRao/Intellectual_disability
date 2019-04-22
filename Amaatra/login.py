from tkinter import *
from PIL import ImageTk, Image
import os
import tkinter.messagebox
import pyrebase
from datetime import date
from firebase import firebase

config = {
    "apiKey": "AIzaSyATuQBI1JJ9sI4jyLjvKbLQX6pzPeGfOMA",
    "authDomain": "amaatraid.firebaseapp.com",
    "databaseURL": "https://amaatraid.firebaseio.com",
    "projectId": "amaatraid",
    "storageBucket": "amaatraid.appspot.com",
    "messagingSenderId": "829220285103"
}

class control:
    def __init__(self):
        self.firebase = firebase.FirebaseApplication("https://amaatraid.firebaseio.com")
        print(self.firebase.get('/NoOfAccount/Value',None))
    
    def check(self):
        if self.firebase.get('/NoOfAccount/Value',None) > 0:
            return True
        else:
            return False
    def dec(self):
        self.firebase.put('NoOfAccount','Value',self.firebase.get('/NoOfAccount/Value',None)-1)
        print(self.firebase.get('/NoOfAccount/Value',None))
    def inc(self):
        self.firebase.put('NoOfAccount','Value',self.firebase.get('/NoOfAccount/Value',None)+1)
        print(self.firebase.get('/NoOfAccount/Value',None))

    

        
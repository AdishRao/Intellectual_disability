import mysql.connector
import sys
from tkinter import *
from PIL import Image
from PIL import ImageTk
import random
from tkinter import ttk
import pandas as pd
from random import randint
import keras
from keras import backend as K
from keras.models import load_model
import numpy as np
import datetime
import pyrebase
from plotly.offline import iplot, init_notebook_mode
import plotly.graph_objs as go
import plotly.io as pio

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

loaded_model = load_model("final.h5")
#network and graph
NetworkValues=[]
plotres = []
dataplot = []
#TODO change database name and password accordingly

mydb = mysql.connector.connect(host="localhost",user="root",passwd="Amazing96",database="ID",auth_plugin='mysql_native_password') #TODO change before pushing
mycursor = mydb.cursor()
uid = 0
rid = 0
ID = True
Sclass = ''
cage = 0
cname =""
gender=""
#variable to choose test to run
i = -4
st = 0

bscore = 0
fscore = 0

#global variables for RPM
q= ["A1.png", "A2.png", "A3.png", "A4.png", "A5.png", "A6.png", "A7.png", "A8.png", "A9.png", "A10.png", "A11.png", "A12.png", "A13.png", "A14.png", "A15.png", "A16.png", "A17.png", "A18.png", "A19.png", "A20.png", "A21.png", "A22.png", "A23.png", "A24.png", "A25.png", "A26.png", "A27.png", "A28.png", "A29.png", "A30.png", "A31.png", "A32.png", "A33.png", "A34.png", "A35.png", "A36.png", "A37.png", "A38.png", "A39.png", "A40.png", "A41.png", "A42.png", "A43.png", "A44.png", "A45.png", "A46.png", "A47.png", "A48.png", "A49.png", "A50.png", "A51.png", "A52.png", "A53.png", "A54.png", "A55.png", "A56.png", "A57.png", "A58.png", "A59.png", "A60.png"]
options = [["1","2","3","4","5","6"], ["1","2","3","4","5","6","7","8"]]
a = [4,5,1,2,6,3,6,2,1,3,5,4,2,6,1,2,1,3,5,6,4,3,4,5,8,2,3,8,7,4,5,1,7,6,1,2,3,4,3,7,8,6,5,4,1,2,5,6,7,6,8,2,1,5,2,4,1,6,3,5]
result = 0

#global for vinelad
index = -1
yes =0
no=0
might=0
basal_age=0
vli=0
vlf=0
index_arr = [0] * 90
agetoadd = 0
age_range = {6:[45,65],7:[51,70],8:[57,74],9:[62,77]}

class STR:
    def __init__(self,master):
        self.master=master
        frame1 = Frame(master,width=500,height=50)
        frame1.pack(side=TOP)
        maxlabel = Label(frame1, text = "RPM min: 26| DST min: 26| BST min: 91| GDT min: 21| Vineland min: 91",wraplength=500,justify="left") #search
        maxlabel.pack()
        frame2 = Frame(master,width=500,height=400)
        frame2.pack(side=TOP)
        photo = Image.open('Report/'+str(rid)+'.png')
        photo = photo.resize((500, 400), Image.ANTIALIAS)
        self.render = ImageTk.PhotoImage(photo)
        photolabel = Label(frame2,image=self.render)
        photolabel.image = self.render
        photolabel.pack()
        endb = Button(master,text="Finish",command = self.quitb)
        endb.pack(side=BOTTOM)

    def quitb(self):
        global i
        i = 8
        self.master.destroy()
        self.master.quit()

class testorstat:
    def __init__(self,master):
        self.master = master
        self.displabel = Label(master,text="Take the test or view statistics")
        self.displabel.place(x=250,y=250,anchor="center")
        self.signup = Button(master,text="Test", command=self.test)
        self.login = Button(master,text="Statistics", command=self.stat)
        self.signup.place(x=180,y=290)
        self.login.place(x=280,y=290)

    def stat(self):
        global i
        i = -6
        self.master.destroy()
        self.master.quit()

    def test(self):
        global i
        i = -1
        self.master.destroy()
        self.master.quit()

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
            mycursor.execute("SELECT COUNT(*) FROM CHILD")
            result = mycursor.fetchone()
            info=auth.get_account_info(user['idToken'])
            uid=result[0]
            rid=str(info['users'][0]['localId'])
            i=-5
            global st
            st =  2
            self.master.destroy()
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

class signup:
    def __init__(self,master):
        self.master = master
        self.email = Label(master,text="Enter Email:")
        self.email.place(x=200,y=195,anchor="center")
        self.password = Label(master,text="Enter Password:")
        self.password.place(x=135,y=225)
        self.password = Label(master,text="Enter class:")
        self.password.place(x=165,y=265)
        self.emailid= Entry(self.master)
        self.psswd= Entry(self.master)
        self.emailid.place(x=250,y=180)
        self.psswd.place(x=250,y=220)
        self.classid= Entry(self.master)
        self.classid.place(x=250,y=260)
        self.login = Button(master,text="Sign Up",command=self.signupb)
        self.login.place(x=250,y=450,anchor="center")


    def signupb(self):
        try:
            global Sclass
            email = self.emailid.get()
            password = self.psswd.get()
            Sclass = self.classid.get()
            print(email)
            print(password)
            user = auth.create_user_with_email_and_password(email,password)
            global uid,rid,i,st
            info=auth.get_account_info(user['idToken'])
            rid=str(info['users'][0]['localId'])
            uid=str(info['users'][0]['localId'])
            i=-5
            st = 1
            self.master.destroy()
            self.master.quit()
        except:
            self.errorlabel = Label(self.master, text = "Email or password invalid, try again")
            self.errorlabel.pack(side=BOTTOM)
            self.emailid.destroy()
            self.psswd.destroy()
            self.emailid= Entry(self.master)
            self.psswd= Entry(self.master)
            self.emailid.place(x=250,y=180)
            self.psswd.place(x=250,y=220)

class logorsign:
    def __init__(self,master):
        self.master = master
        self.displabel = Label(master,text="Please select Sign Up or Login")
        self.displabel.place(x=250,y=250,anchor="center")
        self.signup = Button(master,text="Sign Up", command=self.signupb)
        self.login = Button(master,text="Log In", command=self.loginb)
        self.signup.place(x=180,y=290)
        self.login.place(x=280,y=290)
        self.userno = Button(master,text="Number of Users", command=self.dispno)
        self.userno.place(x=250,y=450,anchor="center")

    def dispno(self):
        global mydb,mycursor
        self.displabel.destroy()
        self.signup.destroy()
        self.login.destroy()
        mycursor.callproc('fetch_no_users')
        for result in mycursor.stored_results():
            Label(self.master,text=result.fetchone()).pack()

    def signupb(self):
        global i
        i = -2
        self.master.destroy()
        self.master.quit()

    def loginb(self):
        global i
        i = -3
        self.master.destroy()
        self.master.quit()

class AN: #Finished
    def __init__(self,master):
        self.master=master
        self.agelabel = Label(master,text="Enter Age:")
        self.agelabel.place(x=180,y=235,anchor="center")
        self.namelabel = Label(master,text="Enter Name:")
        self.namelabel.place(x=144,y=180)
        self.eage= Entry(master)
        self.ename= Entry(master)
        self.eage.place(x=230,y=220)
        self.ename.place(x=230,y=180)
        self.buttonget = Button(master,text="Begin Tests",command=self.getdetails)
        self.buttonget.place(x=250,y=450,anchor="center")
        self.gend = Label(master,text="Enter Gender:")
        self.gend.place(x=181,y=275,anchor="center")
        self.gender = Entry(master)
        self.gender.place(x=230,y=260)

    def getdetails(self):
        global cname,cage,basal_age,gender,NetworkValues,st
        cname = self.ename.get()
        cage = int(self.eage.get())
        gender = self.gender.get()
        NetworkValues.append(cage)
        if gender == 'M':
            NetworkValues.append(1)
        else:
            NetworkValues.append(0)
        print("Age:"+str(cage))
        print("Name:"+cname)
        global i
        global vli
        global vlf
        global age_range
        global index_arr
        if cage>5 and cage<10:
            vli = age_range[cage][0]
            vlf = age_range[cage][1]
            vli-=1
            basal_age = (cage-3)*12.0
        i = 0
        self.master.destroy()
        self.master.quit()

#RPM test class
class RPM:
    def __init__(self,master):
        self.master=master
        self.result = 0
        self.frame1= Frame(master,width=500, height=300)
        self.frame1.pack(side=TOP)
        self.frame3= Frame(master, width=500,height=100)
        self.frame3.pack(side=BOTTOM)
        self.frame2= Frame(master,width=500, height=100)
        self.frame2.pack(side=BOTTOM)
        self.opt_selected = IntVar()
        self.qn = 0
        self.ques = self.create_q(self.frame1,self.qn)
        self.opts = self.create_options(self.frame2,6)
        self.display_q(self.qn)
        labelempty= Label(self.frame3,text="")
        labelempty.pack(side=TOP)
        self.button1 = Button(self.frame3,text="Skip", command=self.print_result)
        self.button1.pack(side=BOTTOM)
        self.button = Button(self.frame3,text="Next", command=self.next_btn)
        self.button.pack(side=LEFT)

    def next_btn(self):
        if self.check_q(self.qn):
            self.result+=1
            print("correct "+str(self.qn+1))
        else:
            print('wrong '+str(self.qn+1))
        self.qn+=1
        if self.qn >= len(q):
            self.print_result()

        else:
            self.display_q(self.qn)

    def mapvalue(self):
        global cage
        if cage>=6 and cage<7:
            self.map=0
        elif cage>=7 and cage<8:
            self.map=1
        elif cage>=8 and cage<9:
            self.map=2
        elif cage>=9 and cage<10:
            self.map=3
        elif cage>=10 and cage<11:
            self.map = 4


    def print_result(self):
        df = pd.read_csv('RPM1.csv')
        X = df.iloc[:,1:6]
        self.mapvalue()
        result = X.iloc[self.result,self.map] #TODO map, with the input age
        print(result)
        self.frame1.destroy()
        self.frame2.destroy()
        self.frame3.destroy()
        self.frame1 = Frame(self.master, width=500, height=500)
        self.frame1.pack()
        printresult = Label(self.frame1, text="Score is "+str(self.result))
        printresult.place(x=250,y=240,anchor="center")
        if(result<26):
            ID = True
            printid = Label(self.frame1, text="Intellectual Disability")
            printid.place(x=250,y=260,anchor="center")
        else:
            ID = False
            printid = Label(self.frame1, text="Normal")
            printid.place(x=250,y=260,anchor="center")
        self.nexttest = Button(self.frame1,text="Next Test",command=self.next)
        self.nexttest.place(x=250,y=490,anchor="center")
        global uid,mydb,mycursor
        rpmq = "insert into RPM(UID,Score,IDR) values (%s,%s,%s)"
        rpmv = (uid,int(result),ID)
        mycursor.execute(rpmq,rpmv)
        mydb.commit()
        global NetworkValues, plotres
        plotres.append(int(result))
        NetworkValues.append(int(result))

    def next(self):
        global i
        i = 1
        self.master.destroy()
        self.master.quit()

    def check_q(self,qn):
        if self.opt_selected.get() == a[qn] :
            return True
        return False

    def display_q(self,qn):
        b_val = 0
        num = 0
        photo = Image.open("RPM/"+q[qn])
        photo = photo.resize((500, 300), Image.ANTIALIAS)
        self.render = ImageTk.PhotoImage(photo)
        self.opt_selected.set(0)
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
       photo = Image.open("RPM/"+q[qn])
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
            btn = Radiobutton(frame2, text="",variable=self.opt_selected,value=b_val+1)
            b.append(btn)
            btn.pack(side=LEFT,anchor="w")
            b_val=b_val+1
        return b

class DST:
    def __init__(self,ar, root, string_var):
        self.ar = ar
        #variables
        self.root = root
        self.items = 1
        self.span = 2
        self.total = 0
        self.clicked1 = IntVar()
        self.clicked2 = IntVar()
        self.test_type = string_var
        self.final_score = 0

        #WIDGET CREATION
        #labels
        self.span_field = self.create_label(root, "Span", self.span, 0, 0, 0, 1, 10, 2, "flat")
        self.trial_1 = self.create_label(root, "Trial 1", self.rand_int_gen(self.span), 1, 0, 1, 1, 10, 2, "groove")
        self.trial_2 = self.create_label(root, "Trial 2", self.rand_int_gen(self.span), 2, 0, 2, 1, 10, 2, "groove")
        self.score_label, self.score_val = self.create_label(root, "", "" , 4, 0, 4, 1, 10, 0, "flat")
        #check-buttons
        self.check_btn_1 = self.create_check_btn(root, self.clicked1, NORMAL, 1, 2)
        self.check_btn_2 = self.create_check_btn(root, self.clicked2, NORMAL, 2, 2)
        #buttons
        self.btn = self.create_btn(root, "NEXT", 5, self.on_btn_click, NORMAL, 3, 1)

    def create_label(self, root, label_txt, value_txt, label_row, label_col, val_row, val_col, w, bw, r):
        label = Label(root, text = label_txt, width = w)
        label.grid(row = label_row, column = label_col, sticky = 'E')
        value = Label(root, text = value_txt, width = w, borderwidth = bw, relief = r)
        value.grid(row = val_row, column = val_col)
        if(label_txt == ""):
            return label, value
        else:
            return value

    def create_check_btn(self, root, var, st, cbtn_row, cbtn_col):
        chk_btn = Checkbutton(root, variable = var, state = st)
        chk_btn.grid(row = cbtn_row, column = cbtn_col)
        return chk_btn

    def create_btn(self, root, btn_text, w, cmd, st, btn_row,  btn_col):
        btn = ttk.Button(root, text = btn_text, command = cmd, state = st)
        btn.grid(row = btn_row, column = btn_col)
        return btn

    def rand_int_gen(self, n):
        l = 10**(n-1)
        b = (10**n)-1
        num = random.randint(l,b)
        return num

    def disable_func(self):
        #self.btn['state'] = DISABLED
        self.btn['command'] = self.next
        self.clicked1.set(0)
        self.clicked2.set(0)
        self.check_btn_2['state'] = DISABLED
        self.check_btn_1['state'] = DISABLED
        self.span_field['text'] = ""
        self.trial_1['text'] = "DONE!"
        self.trial_2['text'] = "DONE!"
        self.score_label['text'] = self.test_type
        self.score_val['text'] = self.total
        self.score_val['relief'] = "groove"
        print(self.test_type , " = " , self.total)
        self.final_score = self.total

    def next(self):
        global i
        if i==1:
            global fscore
            fscore = self.total
            i=2
        else:
            i=3
            global bscore
            bscore = self.total
        self.ar.destroy()
        self.ar.quit()

    def on_btn_click(self):
        global items
        global span
        global total

        if(self.items < 7):
            if( self.clicked1.get() | self.clicked2.get() ):
                self.total = self.total + (self.clicked1.get() + self.clicked2.get())
                self.span += 1
                self.items += 1

                self.clicked1.set(0)
                self.clicked2.set(0)

                self.span_field['text'] = self.span
                self.trial_1['text'] = self.rand_int_gen(self.span)
                self.trial_2['text'] = self.rand_int_gen(self.span)

            else:
                self.disable_func()

        else:
            self.disable_func()

class BST:
    def __init__(self,master):
        self.df = pd.read_csv('bst1.csv')
        self.master=master
        self.images = ["age3.png","age4.png","","age6.png","age7.png","age8.png","",""]
        self.count = 3
        self.basalage = 3.0
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
        global cage,uid,mydb,mycursor
        self.cage = cage
        self.uid = uid
        self.mydb = mydb
        self.mycursor = mycursor
        qbst = "insert into BST(UID,BID) values (%s,%s)"
        vbst = (uid,uid)
        self.mycursor.execute(qbst,vbst)
        self.bid=uid
        self.queries = ["insert into BST3(BID,q1,q2,q3,q4,q5) values(%s,%s,%s,%s,%s,%s)", "insert into BST4(BID,q1,q2,q3,q4) values(%s,%s,%s,%s,%s)","insert into BST5(BID,q1,q2,q3,q4,q5) values(%s,%s,%s,%s,%s,%s)","insert into BST6(BID,q1,q2,q3,q4,q5) values(%s,%s,%s,%s,%s,%s)","insert into BST7(BID,q1,q2,q3,q4,q5) values(%s,%s,%s,%s,%s,%s)","insert into BST8(BID,q1,q2,q3,q4,q5) values(%s,%s,%s,%s,%s,%s)","insert into BST9(BID,q1,q2,q3,q4,q5) values(%s,%s,%s,%s,%s,%s)","insert into BST10(BID,q1,q2,q3,q4,q5) values(%s,%s,%s,%s,%s,%s)"]

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
        self.basalage+=(self.additive_age/100.0)
        self.iq = ((self.basalage)/(self.cage))*100
        print(self.iq)
        for i in range (1,6):
            self.frame[i].destroy()
        self.agelabel['text'] = "IQ is: "+str(self.iq)
        strid = ""
        if self.iq <20:
            strid = "Profound ID"
        elif self.iq <34:
            strid = "Severe ID"
        elif self.iq <49:
            strid = "Moderate ID"
        elif self.iq < 69:
            strid = "Mild ID"
        elif self.iq <90:
            strid = "Boderline ID"
        else:
            strid = "NOT ID"
        if self.iq<90:
            ID = True
        else:
            ID = False
        global uid
        bstcmd = "update BST SET IDB=%s, IQ=%s,ID_Type=%s where UID='"+str(uid)+"'"
        bstval =(ID,self.iq,strid)
        self.mycursor.execute(bstcmd,bstval)
        self.mydb.commit()
        frame = Frame(self.master,width = 500, height = 300)
        frame.pack(side=TOP)
        label = Label(frame,text=strid)
        label.place(x=250,y=150,anchor='center')
        self.frame7.destroy()
        self.frame8 = Frame(self.master, width=500, height=75)
        self.frame8.pack(side=BOTTOM)
        self.qui = Button(self.frame8,text="quit",command=self.des)
        self.qui.place(x=250, y =25, anchor="center")
        global NetworkValues, plotres
        NetworkValues.append(self.iq)
        plotres.append(self.iq)

    def des(self):
        global i
        i = 5
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
        ans = []
        for i in range(0,5):
            if self.opt_selected[i].get() == 1:
                self.questioncount+=1
                print(str(self.questioncount))
                ans.append(1)
            else:
                ans.append(0)
        if self.questioncount == 0:
            self.count = 11
        else:
            if self.count != 4:
                cmd = self.queries[self.q-1]
                val = (self.bid,ans[0],ans[1],ans[2],ans[3],ans[4])
                if self.questioncount == 5:
                    self.basalage+=1
                else:
                    self.additive_age+=2.4*self.questioncount
                self.root1.destroy()

            if self.count == 4:
                cmd = self.queries[self.q-1]
                val = (self.bid,ans[0],ans[1],ans[2],ans[3])
                if self.questioncount == 4:
                    self.basalage+=1
                else:
                    self.additive_age+=3*self.questioncount
                self.root1.destroy()
            self.mycursor.execute(cmd,val)
            self.mydb.commit()
            self.count+=1
            self.questioncount = 0
        self.root1.destroy()
        for i in range(0,5):
            q=self.question[i]
            q.destroy()
        self.create_q()

class dispdst:

    def __init__(self,master):
        global cage,uid,mydb,mycursor
        self.master=master
        global rawscore,fscore,bscore
        rawscore = fscore + bscore
        stdscore = 0
        dstper = 0
        if rawscore <= 3:
            ID=True
            dstlabel = Label(master,text="ID")
        else:
            df = pd.read_csv('DST.csv')
            stdscore=df[str(cage)][rawscore-4]
            df = pd.read_csv('P_Score.csv')
            dstper=df.loc[df['SS']==stdscore]['PE'].iloc[0]
            if dstper < 26:
                ID=True
                dstlabel = Label(master,text="ID")
            else:
                ID=False
                dstlabel = Label(master,text="Not ID")
        dstlabel.place(x=250,y=250,anchor="center")
        dstbutton = Button(master,text="Next Test",command=self.nexttest)
        dstbutton.pack(side=BOTTOM)
        dstq = "insert into DST(UID,Forward_Score,Backward_Score,Raw_score,IDD,Std_score,Per_score) values (%s,%s,%s,%s,%s,%s,%s)"
        dstv = (uid,int(fscore),int(bscore),int(rawscore),ID,float(stdscore),float(dstper))
        mycursor.execute(dstq,dstv)
        mydb.commit()
        global NetworkValues, plotres
        plotres.append(dstper)
        NetworkValues.append(float(stdscore))
        NetworkValues.append(float(dstper))

    def nexttest(self):
        global i
        i=4
        self.master.destroy()
        self.master.quit()

class GDT:
    def __init__(self,master):
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
        self.q = [ "GDT/GDT1.png", "GDT/GDT2.png", "GDT/GDT3.png", "GDT/GDT4.png", "GDT/GDT5.png", "GDT/GDT6.png", "GDT/GDT7.png", "GDT/GDT8.png", "GDT/GDT9.png", "GDT/GDT10.png", "GDT/GDT11.png", "GDT/GDT12.png", "GDT/GDT13.png", "GDT/GDT14.png", "GDT/GDT15.png", "GDT/GDT16.png", "GDT/GDT17.png", "GDT/GDT18.png", "GDT/GDT19.png", "GDT/GDT20.png", "GDT/GDT21.png", "GDT/GDT22.png", "GDT/GDT23.png", "GDT/GDT24.png"  ]
        self.qn =0
        global cage
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
        df = pd.read_csv("GDT.csv")
        X =df.iloc[:, 0:8]
        result = X.iloc[self.count, self.age-3]
        print(str(result)) #printing percentile
        if result<=10:
            strid = "Definitely below"
            ID = True
        elif result<=20:
            strid = "below"
            ID = True
        else:
            strid = "Normal"
            ID =False
        self.frame1.destroy()
        self.frame1 = Frame(self.master,width=500,height=450)
        self.frame1.pack(side=TOP)
        labelid = Label(self.frame1, text = strid)
        labelid.place(x= 250, y =225, anchor = "center" )
        self.nextbtn['command'] = self.nexttest
        global mydb,mycursor,uid
        GDTq = "insert into GDT values (%s,%s,%s,%s)"
        GDTv= (uid,uid,int(result),int(ID))
        mycursor.execute(GDTq,GDTv)
        mydb.commit()
        global NetworkValues, plotres
        NetworkValues.append(result)
        plotres.append(result)

    def nexttest(self):
        self.master.destroy()
        self.master.quit()
        global i
        i = 6

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

class Question:
    def __init__(self, question, answers):
        self.question = question
        self.answers = answers
        global vli
        global vlf
        global age_range



 #       self.c_age=0
 #    def onok(self):
 #       self.c_age= entry.get()

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
            label = Label(view, text="yes")
            yes += 1
            basal_age+=agetoadd
            vli += 1
            index_arr[vli] = 1
        elif(letter == "B"):
            label = Label(view, text="no")
            no +=1
            vli += 1
            index_arr[vli] = 0
        else:
            label = Label(view, text="could have passed")
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



    def getView(self, window):
        view = Frame(window)
        Label(view, text=self.question).pack()
        Button(view, text=self.answers[0], command=lambda *args: self.check("A", view),width=50).pack()
        Button(view, text=self.answers[1], command=lambda *args: self.check("B", view),width=50).pack()
        Button(view, text=self.answers[2], command=lambda *args: self.check("C", view),width=50).pack()

        return view

    def unpackView(self, view):
        view.pack_forget()
        askQuestion()

def askQuestion():
    global questions, window, index, button, yes, no,might, number_of_questions,social_quotient,index_arr,vlf,vli
    if(vli == vlf):
        #Label(window, text="Thank you for answering the questions. 1. yes " + str(yes) +" 2. no " +str(no) + " 3.might"+str(might) + " of " + str(number_of_questions) + " questions answered right||basal_age =  "+str(basal_age),font=('15')).pack()
        Label(window,text="Thank you for answering the questions.\n basal_age = " + str(basal_age)).pack()
        global cage
        social_quotient=(basal_age/(cage*12))*100#chrono age taken as 10 as all question included are till 9-10 yearsold
        Label(window, text="social quotient = " + str(social_quotient)).pack()
        if(social_quotient<20):
            ID = True
            Label(window, text="Profound Intelletual disability").pack()
        elif((social_quotient>=20) and(social_quotient<35)):
            ID = True
            Label(window, text="Severe Intelletual disability").pack()
        elif((social_quotient>=35) and (social_quotient<50)):
            ID = True
            Label(window, text="Moderate Intelletual disability").pack()
        elif((social_quotient>=50) and (social_quotient<70)):
            ID = True
            Label(window, text="Mild Intelletual disability").pack()
        else:
            ID = False
            Label(window, text="Normal IQ").pack()
        buttonn = Button(window,text="Next",command=quitf)
        buttonn.pack(side=BOTTOM)
        global mydb,mycursor,uid
        vlq = "insert into Vineland values (%s,%s,%s,%s)"
        vlv = (uid,uid,ID,social_quotient)
        mycursor.execute(vlq,vlv)
        mydb.commit()
        vlq = "insert into VL0 values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        vlv = (uid,index_arr[1],index_arr[2],index_arr[3],index_arr[4],index_arr[5],index_arr[6],index_arr[7],index_arr[8],index_arr[9],index_arr[10],index_arr[11],index_arr[12],index_arr[13],index_arr[14],index_arr[15],index_arr[16],index_arr[17])
        mycursor.execute(vlq,vlv)
        mydb.commit()
        vlq = "insert into VL1 values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        vlv = (uid,index_arr[18],index_arr[19],index_arr[20],index_arr[21],index_arr[22],index_arr[23],index_arr[24],index_arr[25],index_arr[26],index_arr[27],index_arr[28],index_arr[29],index_arr[30],index_arr[31],index_arr[32],index_arr[33],index_arr[34])
        mycursor.execute(vlq,vlv)
        mydb.commit()
        vlq = "insert into VL2 values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        vlv = (uid,index_arr[35],index_arr[36],index_arr[37],index_arr[38],index_arr[39],index_arr[40],index_arr[41],index_arr[42],index_arr[43],index_arr[44])
        vlq = "insert into VL3 values (%s,%s,%s,%s,%s,%s,%s)"
        vlv = (uid,index_arr[45],index_arr[46],index_arr[47],index_arr[48],index_arr[49],index_arr[50])
        mycursor.execute(vlq,vlv)
        mydb.commit()
        vlq = "insert into VL4 values (%s,%s,%s,%s,%s,%s,%s)"
        vlv = (uid,index_arr[51],index_arr[52],index_arr[53],index_arr[54],index_arr[55],index_arr[56])
        mycursor.execute(vlq,vlv)
        mydb.commit()
        vlq = "insert into VL5 values (%s,%s,%s,%s,%s,%s)"
        vlv = (uid,index_arr[57],index_arr[58],index_arr[59],index_arr[60],index_arr[61])
        mycursor.execute(vlq,vlv)
        mydb.commit()
        vlq = "insert into VL6 values (%s,%s,%s,%s,%s)"
        vlv = (uid,index_arr[62],index_arr[63],index_arr[64],index_arr[65])
        mycursor.execute(vlq,vlv)
        mydb.commit()
        vlq = "insert into VL7 values (%s,%s,%s,%s,%s,%s)"
        vlv = (uid,index_arr[66],index_arr[67],index_arr[68],index_arr[69],index_arr[70])
        mycursor.execute(vlq,vlv)
        mydb.commit()
        vlq = "insert into VL8 values (%s,%s,%s,%s,%s)"
        vlv = (uid,index_arr[71],index_arr[72],index_arr[73],index_arr[74])
        mycursor.execute(vlq,vlv)
        mydb.commit()
        vlq = "insert into VL9 values (%s,%s,%s,%s)"
        vlv = (uid,index_arr[75],index_arr[76],index_arr[77])
        mycursor.execute(vlq,vlv)
        mydb.commit()
        vlq = "insert into VL10 values (%s,%s,%s,%s,%s)"
        vlv = (uid,index_arr[78],index_arr[79],index_arr[80],index_arr[81])
        mycursor.execute(vlq,vlv)
        mydb.commit()
        global plotres #search
        plotres.append(social_quotient)
        global NetworkValues
        NetworkValues.append(social_quotient)
        return
    button.pack_forget()
    label_des.pack_forget()
    questions[vli].getView(window).pack()

def quitf():
    global i
    i = 7
    window.quit()
    window.destroy()
questions = []
file = open("vineland2questions.txt", "r",encoding='windows-1252')
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

while i==-4:
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
    an = logorsign(root)
    root.mainloop()

while i == -2:
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
    an = signup(root)
    root.mainloop()

while i == -3:
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
    an = login(root)
    root.mainloop()

while i==-5:
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
    tos = testorstat(root)
    root.mainloop()

while i==-1:
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
    an = AN(root)
    root.mainloop()

if i!=-6:
    try:
        childquery = "insert into Child(UID,Name,Age,ID,DateOfTest,RID,Gender,Class) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
        dateoftest = datetime.datetime.today().strftime('%Y-%m-%d')
        childvalues = (uid,cname,cage,ID,dateoftest,rid,gender,Sclass)
        mycursor.execute(childquery,childvalues)
        mydb.commit()
    except mysql.connector.Error as error:
        print("Age out of bounds")
    if cage<6 or cage>9:
        sys.exit()

while i==0:
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
    Rpm = RPM(root)
    root.mainloop()

while i==1:
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
    frame1 = Frame(root,width=500,height=100)
    frame1.pack(side=TOP)
    title = Label(frame1,text='Digit Span Test')
    title.place(x=250,y=50, anchor='center')
    frame2 = Frame(root,width=500,height=400)
    frame2.pack(side=TOP)
    ft = DST(root,frame2, "Forward Score")
    root.mainloop()

while i==2:
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
    frame1 = Frame(root,width=500,height=100)
    frame1.pack(side=TOP)
    title = Label(frame1,text='Digit Span Test')
    title.place(x=250,y=50, anchor='center')
    frame2 = Frame(root,width=500,height=400)
    frame2.pack(side=TOP)
    ft = DST(root,frame2, "Backward Score")
    root.mainloop()

while i==3:
    rootdst = Tk()
    w = 500 # width for the Tk root
    h = 500 # height for the Tk root

    # get screen width and height
    ws = rootdst.winfo_screenwidth() # width of the screen
    hs = rootdst.winfo_screenheight() # height of the screen

    # calculate x and y coordinates for the Tk root window
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)

    # set the dimensions of the screen
    # and where it is placed
    rootdst.geometry('%dx%d+%d+%d' % (w, h, x, y))
    Dispdst= dispdst(rootdst)
    rootdst.mainloop()

while i==4:
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
    Bst = BST(root)
    root.mainloop()

while i==5:
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
    Gdt = GDT(root)
    root.mainloop()

while i==6:
    window = Tk()
    w = 600
    h = 300
      # get screen width and height
    ws = window.winfo_screenwidth() # width of the screen
    hs = window.winfo_screenheight() # height of the screen

        # calculate x and y coordinates for the Tk root window
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)

        # set the dimensions of the screen
        # and where it is placed
    window.geometry('%dx%d+%d+%d' % (w, h, x, y))
    label_heading = Label(window, text="VINELAND SOCIAL MATURITY TEST",bg="black",fg="white",font=('Helvetica', '20'))
    label_heading.pack()
    label_des = Label(window, text="\n\nThe Vineland Social Maturity Scale (VSMS) measures the differential social\ncapacities of an individual. It provides an estimate of Social Age (SA) and Social\nQuotient (SQ), and shows high correlation (0.80) with intelligence. It is designed to\nmeasure social maturation in eight social areas: Self-help General (SHG), Self-help\nEating (SHE), Self-help Dressing (SHD), Self direction (SD), Occupation (OCC),\nCommunication (COM), Locomotion (LOM), and Socialization (SOC).",fg="blue",font=('15'))
    label_des.pack()
    button = Button(window, text="Start", command=askQuestion)
    button.pack()
    window.mainloop()

if i==7:
    NetworkValues=np.array(NetworkValues)
    NetworkValues=NetworkValues.reshape(1,8)
    NetAns=loaded_model.predict(NetworkValues, verbose=0)
    print(NetAns)

    if st == 1:
        dateoftest = datetime.datetime.today().strftime('%Y-%m-%d')
        trace1 = go.Bar(
        x=['Ravens','DST','BST','Drawing test','Vineland'], #search
        y=plotres,
        name='Test on '+str(dateoftest)
        )
        data = [trace1]
        layout = go.Layout(
            barmode='group'
        )
        fig = go.Figure(data=data, layout=layout)
        pio.write_image(fig, 'Report/'+str(rid)+'.png')
        storage = firebase.storage()
        storage.child("report/"+str(rid)+".jpg").put('Report/'+str(rid)+'.png')
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
        singletestres = STR(root)
        root.mainloop()

if st==2 or i==-6:
    q = "SELECT UID FROM CHILD WHERE RID ='"+str(rid)+"' order by DateOfTest"
    mycursor.execute(q)
    result = mycursor.fetchall() #TODO input RPM percentile not score. Change all current scores to percentile,
    for x in result:
        p= "select score,Per_score,IQ,Percentile,IQV from child C NATURAL JOIN (RPM R NATURAL JOIN (DST D NATURAL JOIN (BST B NATURAL JOIN (GDT NATURAL JOIN Vineland)))) WHERE UID = '"+str(x[0])+"'"  #search
        mycursor.execute(p)
        result1 = mycursor.fetchone()
        print(result1)
        trace = go.Bar(
        x=['Ravens','DST','BST','Drawing test','Vineland'], #search
        y=list(result1),
        )
        dataplot.append(trace)

    layout = go.Layout(
        barmode='group'
    )
    fig = go.Figure(data=dataplot, layout=layout)
    pio.write_image(fig, 'Report/'+str(rid)+'.png')
    storage = firebase.storage()
    storage.child("report/"+str(rid)+".jpg").put('Report/'+str(rid)+'.png')
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
    singletestres = STR(root)
    root.mainloop()

from tkinter import *
from PIL import ImageTk,Image  
import pandas as pd
import mysql.connector
cage = 6.5
mydb = mysql.connector.connect(host="localhost",user="root",passwd="Amazing96",database="test")
mycursor = mydb.cursor()
uid = 2
name = "xyz"
ID = False
sqlt1 = "INSERT into t1 (uid,name,ID,age) values (%s,%s,%s,%s)"
valt1 = (uid,name,ID,cage)
mycursor.execute(sqlt1, valt1)
mydb.commit()

class BST:
    def __init__(self,master):
        self.df = pd.read_csv('bst1.csv')
        self.master=master
        self.images = ["age3.png","age4.png","","age6.png","age7.png"]
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
        global cage,uid,mydb,mycursor
        self.mydb = mydb
        self.mycursor = mycursor
        self.age=cage
        qbst = "insert into BST(UID,BID) values (%s,%s)"
        vbst = (uid,uid)
        self.mycursor.execute(qbst,vbst)
        self.bid=uid
        self.queries = ["insert into BST3(BID,q1,q2,q3,q4,q5) values(%s,%s,%s,%s,%s,%s)", "insert into BST4(BID,q1,q2,q3,q4) values(%s,%s,%s,%s,%s)","insert into BST5(BID,q1,q2,q3,q4,q5) values(%s,%s,%s,%s,%s,%s)","insert into BST6(BID,q1,q2,q3,q4,q5) values(%s,%s,%s,%s,%s,%s)","insert into BST7(BID,q1,q2,q3,q4,q5) values(%s,%s,%s,%s,%s,%s)"]

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
        agecase = {3:self.bs,4:self.bs4,5:self.bs,6:self.bs,7:self.bs,8:self.finish}
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
        global cage
        self.iq = ((self.basalage)/(cage))*100
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
        bstcmd = "update BST SET ID=%s, IQ=%s,ID_Type=%s where UID=%s"
        bstval =(ID,self.iq,strid,self.bid)
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
        ans = []
        for i in range(0,5):
            if self.opt_selected[i].get() == 1:
                self.questioncount+=1
                print(str(self.questioncount))
                ans.append(1)
            else:
                ans.append(0)
        if self.questioncount == 0:
            self.count = 8
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

root = Tk()
root.geometry("500x500")
root.title("Binet Simon Test")
Bst = BST(root)
root.mainloop()



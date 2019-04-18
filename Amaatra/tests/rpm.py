from tkinter import *
from PIL import Image
from PIL import ImageTk
from tkinter import ttk
import pandas as pd
import os
'''
c age is the chronological age.
self.result is the number of patterns matched right
result is the mapping of cage and self.result, it is this value that is to be stored in firebase and used to generate the graph
'''

q= ["A1.png", "A2.png", "A3.png", "A4.png", "A5.png", "A6.png", "A7.png", "A8.png", "A9.png", "A10.png", "A11.png", "A12.png", "A13.png", "A14.png", "A15.png", "A16.png", "A17.png", "A18.png", "A19.png", "A20.png", "A21.png", "A22.png", "A23.png", "A24.png", "A25.png", "A26.png", "A27.png", "A28.png", "A29.png", "A30.png", "A31.png", "A32.png", "A33.png", "A34.png", "A35.png", "A36.png", "A37.png", "A38.png", "A39.png", "A40.png", "A41.png", "A42.png", "A43.png", "A44.png", "A45.png", "A46.png", "A47.png", "A48.png", "A49.png", "A50.png", "A51.png", "A52.png", "A53.png", "A54.png", "A55.png", "A56.png", "A57.png", "A58.png", "A59.png", "A60.png"]
options = [["1","2","3","4","5","6"], ["1","2","3","4","5","6","7","8"]]
a = [4,5,1,2,6,3,6,2,1,3,5,4,2,6,1,2,1,3,5,6,4,3,4,5,8,2,3,8,7,4,5,1,7,6,1,2,3,4,3,7,8,6,5,4,1,2,5,6,7,6,8,2,1,5,2,4,1,6,3,5]

class RPM:
    def __init__(self,master,cage):
        self.cage = cage 
        self.master=master
        self.result = 0
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
        self.qn+=1
        if self.qn >= len(q):
            self.print_result()

        else:
            self.display_q(self.qn)

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
        filepath=os.path.dirname(os.path.abspath(__file__))
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
            self.frame1.configure(background='firebrick2') 
            printid = Label(self.frame1, text="Test FAILED: Intellectual Disability")
            printid.place(x=250,y=260,anchor="center")
        else:
            self.frame1.configure(background='spring green') 
            printid = Label(self.frame1, text="Test PASSED: Normal")
            printid.place(x=250,y=260,anchor="center")
        self.nexttest = Button(self.frame1,text="Next Test",command=self.next)
        self.nexttest.place(x=250,y=490,anchor="center")
        self.returnval = int(result) #return to calling function #TODO:create a function to return value

    def next(self):
        self.master.destroy()
        self.master.quit()

    def check_q(self,qn):
        print(self.opt_selected)
        if self.opt_selected == a[qn] :
            return True
        return False

    def display_q(self,qn):
        filepath=os.path.dirname(os.path.abspath(__file__))
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
       filepath=os.path.dirname(os.path.abspath(__file__))
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


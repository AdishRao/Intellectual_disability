from tkinter import *
from PIL import ImageTk,Image  
import pandas as pd

class BST:
    def __init__(self,master):
        self.df = pd.read_csv('bst.csv')
        self.master=master
        self.count = 3
        self.basalage = 2
        self.additive_age = 0
        self.questioncount = 0
        self.i=0
        self.frame1 = Frame(self.master, width=500, height=100)
        self.frame1.pack(side=TOP)
        self.frame2 = Frame(self.master, width=500, height=300)
        self.frame2.pack(side=TOP)
        self.frame3 = Frame(self.master, width=500, height=100)
        self.frame3.pack(side=BOTTOM)
        self.opt_selected = IntVar()
        self.opts = self.create_options(self.frame3,2)
        self.agelabel = Label(self.frame1,text="Age test: "+str(self.count),bg='black',fg='white')
        self.agelabel.place(x=250,y=50,anchor="center")
        self.ques = self.create_q(self.frame2)

    def nextq(self):
            print("basal "+str(self.basalage))
            print("add "+str(self.additive_age))

    def create_q(self,frame2):
        self.displayquestion= Label(frame2,text="")
        self.displayquestion.place(x=250,y=150,anchor="center")
        self.nextb = Button(frame2,text="next",command=self.next_btn)
        self.nextb.place(x=250, y =200, anchor="center")
        self.opt_selected.set(0)
        agecase = {5:self.nextq ,3:self.bs3, 4:self.bs4}
        agecase[self.count]()
    
    def bs3(self):
        X = self.df.iloc[:,0]
        if(self.i < 5):
            self.displayquestion['text'] = X[self.i]
            self.i+=1
        if self.i == 5:
            if self.questioncount == 4:
                self.basalage+=1
            else:
                self.additive_age+=2.4*self.questioncount
            self.count+=1
            self.i = 0
            self.questioncount = -1



    def bs4(self):
        self.agelabel['text'] = "Age test: "+str(self.count)
        X = self.df.iloc[:,1]
        if(self.i<4):
            self.displayquestion['text'] = X[self.i]
            self.i+=1
        if self.i == 4:
            if self.questioncount == 3:
                self.basalage+=1
            else:
                self.additive_age+=3*self.questioncount
            self.count+=1
            self.i = 0
            self.questioncount = -1


    def next_btn(self):
        if self.opt_selected.get() == 1:
            self.questioncount+=1
            print(str(self.questioncount))
        if self.opt_selected.get() != 0:
            self.displayquestion.destroy()
            self.create_q(self.frame2)

        




        
        

    def create_options(self,frame3,n):
        b_val = 0
        b = []
        btn = Radiobutton(frame3, text="Yes",variable=self.opt_selected,value=b_val+1)
        b.append(btn)
        btn.place(x=210,y=50,anchor="center")
        b_val=b_val+1
        btn = Radiobutton(frame3, text="No",variable=self.opt_selected,value=b_val+1)
        b.append(btn)
        btn.place(x=310,y=50,anchor="center")
        return b





root = Tk()
root.geometry("500x500")
Bst = BST(root)
root.mainloop()
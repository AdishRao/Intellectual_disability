from tkinter import *
from PIL import ImageTk,Image  
import pandas as pd

class BST:
    def __init__(self,master):
        df = pd.read_csv('bst.csv')
        self.master=master
        self.age = 3
        self.count = 3
        self.frame1 = Frame(self.master, width=500, height=100)
        self.frame1.pack(side=TOP)
        self.frame2 = Frame(self.master, width=500, height=300)
        self.frame2.pack(side=TOP)
        self.frame3 = Frame(self.master, width=500, height=100)
        self.frame3.pack(side=BOTTOM)
        self.opt_selected = IntVar()
        self.opts = self.create_options(self.frame3,2)
        self.agelabel = Label(self.frame1,text="Age test: "+str(self.age),bg='black',fg='white')
        self.agelabel.place(x=250,y=50,anchor="center")
        self.ques = self.create_q(self.frame2)

    def nextq(self):
            print('done')

    def create_q(self,frame2):
        displayquestion= Label(frame2,text="")
        displayquestion.place(x=250,y=150,anchor="center")
        agecase = {0:self.nextq ,3:self.bs3, 4:self.bs4, 5:self.bs5, 6:self.bs6, 7:self.bs7}
        agecase[self.count]()
        
        


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
from tkinter import *
from PIL import Image
from PIL import ImageTk
from tkinter import ttk
import pandas as pd
import os

class GDT:
    def __init__(self,master,cage):
        filepath=os.path.dirname(os.path.abspath(__file__))
        self.cage = cage
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
        self.q = [filepath+"/GDT/GDT1.png", filepath+"/GDT/GDT2.png", filepath+"/GDT/GDT3.png", filepath+"/GDT/GDT4.png", filepath+"/GDT/GDT5.png", filepath+"/GDT/GDT6.png", filepath+"/GDT/GDT7.png", filepath+"/GDT/GDT8.png", filepath+"/GDT/GDT9.png", filepath+"/GDT/GDT10.png", filepath+"/GDT/GDT11.png", filepath+"/GDT/GDT12.png", filepath+"/GDT/GDT13.png", filepath+"/GDT/GDT14.png", filepath+"/GDT/GDT15.png", filepath+"/GDT/GDT16.png", filepath+"/GDT/GDT17.png", filepath+"/GDT/GDT18.png", filepath+"/GDT/GDT19.png", filepath+"/GDT/GDT20.png", filepath+"/GDT/GDT21.png", filepath+"/GDT/GDT22.png", filepath+"/GDT/GDT23.png", filepath+"/GDT/GDT24.png"  ]
        self.qn =0
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
        filepath=os.path.dirname(os.path.abspath(__file__))
        df = pd.read_csv(filepath+"/GDT/GDT.csv")
        X =df.iloc[:, 0:8]
        result = X.iloc[self.count, self.age-3]
        print(str(result)) #printing percentile
        self.frame3.pack_forget()
        if result<=10:
            strid = "Definitely below required: Intellectual Disability"
            ID = True
        elif result<=20:
            strid = "Below required: Intellectual Disability"
            ID = True
        else:
            strid = "Normal"
            ID =False
        self.frame1.destroy()
        self.frame1 = Frame(self.master,width=500,height=450)
        self.frame1.pack(side=TOP)
        if ID == True:
            self.frame1.configure(background='firebrick2') 
        else:
            self.frame1.configure(background='spring green') 
        labelid = Label(self.frame1, text = strid)
        labelid.place(x= 250, y =225, anchor = "center" )
        self.nextbtn['command'] = self.nexttest
        
        self.returnval = int(result) 


    def nexttest(self):
        self.master.destroy()
        self.master.quit()

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

    def getresult(self):
        return self.returnval

'''
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
GDTcall = GDT(root,6)
root.mainloop()
'''
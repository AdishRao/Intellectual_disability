from tkinter import *
from PIL import ImageTk,Image  
import pandas as pd

#global variables for RPM
q= ["A1.png", "A2.png", "A3.png", "A4.png", "A5.png", "A6.png", "A7.png", "A8.png", "A9.png", "A10.png", "A11.png", "A12.png", "A13.png", "A14.png", "A15.png", "A16.png", "A17.png", "A18.png", "A19.png", "A20.png", "A21.png", "A22.png", "A23.png", "A24.png", "A25.png", "A26.png", "A27.png", "A28.png", "A29.png", "A30.png", "A31.png", "A32.png", "A33.png", "A34.png", "A35.png", "A36.png", "A37.png", "A38.png", "A39.png", "A40.png", "A41.png", "A42.png", "A43.png", "A44.png", "A45.png", "A46.png", "A47.png", "A48.png", "A49.png", "A50.png", "A51.png", "A52.png", "A53.png", "A54.png", "A55.png", "A56.png", "A57.png", "A58.png", "A59.png", "A60.png"]
options = [["1","2","3","4","5","6"], ["1","2","3","4","5","6","7","8"]]
a = [4,5,1,2,6,3,6,2,1,3,5,4,2,6,1,2,1,3,5,6,4,3,4,5,8,2,3,8,7,4,5,1,7,6,1,2,3,4,3,7,8,6,5,4,1,2,5,6,7,6,8,2,1,5,2,4,1,6,3,5]
result = 0

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
        self.button = Button(self.frame3,text="Next", command=self.next_btn)
        self.button.pack(side=BOTTOM)

    def next_btn(self):
        if self.check_q(self.qn):
            self.result+=1
            print("correct")
        else:
            print('wrong')
        self.qn+=1
        if self.qn >= len(q):
            self.print_result()
            
        else:
            self.display_q(self.qn)

    def print_result(self):
        df = pd.read_csv('RPM1.csv')
        X = df.iloc[:,1:2]
        result = X.iloc[self.result,0]
        print(result)
        self.frame1.destroy()
        self.frame2.destroy()
        self.frame3.destroy()
        self.frame1 = Frame(self.master, width=500, height=500)
        self.frame1.pack()
        printresult = Label(self.frame1, text="Score is "+str(self.result))
        printresult.place(x=250,y=240,anchor="center")
        if(result<26):
            printid = Label(self.frame1, text="Intellectual Disability")
            printid.place(x=250,y=260,anchor="center")
        else:
            printid = Label(self.frame1, text="Normal")
            printid.place(x=250,y=260,anchor="center")
        
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
    
#creating root and creating objects to classes    
root = Tk()
root.geometry("500x500")
Rpm = RPM(root)
root.mainloop()

from tkinter import *
from PIL import ImageTk,Image  
import pandas as pd
import random
from tkinter import ttk
cage = 6.5
i = 0
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
        self.qn = 58
        self.ques = self.create_q(self.frame1,self.qn)
        self.opts = self.create_options(self.frame2,8)
        self.display_q(self.qn)
        labelempty= Label(self.frame3,text="")
        labelempty.pack(side=TOP)
        self.button = Button(self.frame3,text="Next", command=self.next_btn)
        self.button.pack(side=BOTTOM)

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
        self.btn['state'] = DISABLED
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
        global i
        if i == 1:
            i = 2
        else:
            i = 3
        self.ar.quit()
        self.ar.destroy()
        

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
        global i
        i = 4
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
        for i in range(0,5):
            if self.opt_selected[i].get() == 1:
                self.questioncount+=1
                print(str(self.questioncount))
        if self.questioncount == 0:
            self.count = 8
        else:
            if self.count != 4:
                if self.questioncount == 5:
                    self.basalage+=1
                else:
                    self.additive_age+=2.4*self.questioncount
                self.root1.destroy()

            if self.count == 4:
                if self.questioncount == 4:
                    self.basalage+=1
                else:
                    self.additive_age+=3*self.questioncount
                self.root1.destroy()
            self.count+=1
            self.questioncount = 0
        self.root1.destroy()
        for i in range(0,5):
            q=self.question[i]
            q.destroy()
        self.create_q()


    
#creating root and creating objects to classes 
while i==0:   
    root = Tk()
    root.geometry("500x500")
    Rpm = RPM(root)
    root.mainloop()

while i==1:
    root = Tk()
    root.geometry("500x500")
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
    root.geometry("500x500")
    frame1 = Frame(root,width=500,height=100)
    frame1.pack(side=TOP)
    title = Label(frame1,text='Digit Span Test')
    title.place(x=250,y=50, anchor='center')
    frame2 = Frame(root,width=500,height=400)
    frame2.pack(side=TOP)
    ft = DST(root,frame2, "Backward Score")
    root.mainloop()

while i==3:
    root = Tk()
    root.geometry("500x500")
    root.title("Binet Simon Test")
    Bst = BST(root)
    root.mainloop()

#TODO
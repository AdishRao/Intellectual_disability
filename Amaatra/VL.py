from tkinter import *
from PIL import Image
from PIL import ImageTk
from tkinter import ttk
#import pandas as pd
import os
import tkinter.messagebox
#import pyrebase
from datetime import date

import sys
from fpdf import FPDF
import time
import matplotlib.pyplot as plt

path = ""
today = str(date.today())

ReturnName = ""
Age = 0
Choice =-1
VLresult = 0
pathdir = ""

Name = ""
Age = 0
test_number = 0

def f(string):
    return string.format(**globals())

class Plot:
    def __init__(self,master):
        
        print('Starting the plot function')
        self.master=master
        frame1 = Frame(master,width=500,height=50)
        frame1.pack(side=TOP)
        maxlabel = Label(frame1, text = "BST min: 90| GDT min: 21| RPM min: 26| Vineland min: 90",wraplength=500,justify="left") #search
        maxlabel.pack()

    def plot(self,vi):
        self.z = 0
        fig, axs = plt.subplots(2, 2)
        i = 1
        y1 = []
        for x1 in vi :
            y1.append(i)
            i = i+1
        axs[0, 0].bar(y1, vi, label='Vineland Social Maturity Scale', color='tab:red')
        axs[0, 0].set_title('Vinelands')
        fig.suptitle('Test results comparison')
        plt.tight_layout()

        filepath=os.path.dirname(os.path.abspath(__file__))
        plt.savefig(filepath+'/Images/Report.png')
        frame2 = Frame(self.master,width=500,height=400)
        frame2.pack(side=TOP)
        photo = Image.open(filepath+'/Images/Report.png')
        photo = photo.resize((500, 400), Image.ANTIALIAS)
        self.render = ImageTk.PhotoImage(photo)
        photolabel = Label(frame2,image=self.render)
        photolabel.image = self.render
        photolabel.pack()
        endb = Button(self.master,text="Finish",command = self.quitb)
        endb.pack(side=BOTTOM)
        print('Plot successful')
    
    def quitb(self):
        self.master.destroy()
        self.master.quit()     

class LoginTeacher:
    def __init__(self,f,master,numb):
        self.f=f
        self.master = master
        self.Password=StringVar()
        self.Email = StringVar()
        self.label_0 = Label(f, text="Staff Login Verification",width=20,font=("bold", 20))
        self.label_0.place(x=90,y=53)

        self.label_1 = Label(f, text="Email",width=20,font=("bold", 10))
        self.label_1.place(x=80,y=130)

        self.entry_1 = Entry(f, textvar=self.Email)
        self.entry_1.place(x=240,y=130)

        self.label_2 = Label(f, text="Password",width=20,font=("bold", 10))
        self.label_2.place(x=79,y=180)

        self.entry_2 = Entry(f, textvar=self.Password)
        self.entry_2.place(x=240,y=180)

        self.btn = Button(f, text='Submit',width=20, anchor="center", command=self.insertlogin)
        self.btn.place(x=180,y=300)


    def insertlogin(self):
        email=self.Email.get()
        password=self.Password.get()

        #Check entered details with existing details on firebase to verify staff or not
        print(self.Email.get())
        #to check if primary key aready EXISTS
        self.f.destroy()
        #global root
        f1 = Frame(self.master,width=500,height=500)
        f1.configure(background='peach puff')
        f1.pack()
        page1 = Page1(f1,self.master)

    def returnnametocalling(self):
        global ReturnName,path
        return ReturnName,path

    def returnagetocalling(self):
        global Age
        return Age

    def returnchoice(self):
        global Choice
        return Choice

class Page1: #Intermediate window to choose new student, previous student or retake of test
    def __init__(self, f,master):
        self.f=f
        self.master=master
        self.label_0 = Label(f, text="Choose Activity",width=20,font=("bold", 20))
        self.label_0.place(x=90,y=53)
        self.btn1 = Button(self.f, text='New Student',width=20, anchor="center",command=self.newstudent)
        self.btn1.place(x=160,y=310)
        self.btn2 = Button(self.f, text='Todays report',width=20, anchor="center", command=self.report)
        self.btn2.place(x=160,y=410)

    def newstudent(self):
        global Choice
        Choice = 1
        self.f.destroy()
        f1 = Frame(self.master,width=500,height=500)
        f1.configure(background='peach puff')
        f1.pack()
        page2 = NewStudent(f1,self.master)

    def report(self):
        global Choice
        Choice = 2
        self.f.destroy()
        f2 = Frame(self.master,width=500,height=500)
        f2.configure(background='peach puff')
        f2.pack()
        #page3 = Reports(f2,self.master)

class NewStudent:
    def __init__(self, f,master):
        self.f=f
        self.master=master
        self.Fname=StringVar()
        self.Lname = StringVar()
        self.Gender=StringVar()
        self.Age = IntVar()
        self.Dob = StringVar()

        self.label_0 = Label(f, text="Enter Student Details",width=20,font=("bold", 20))
        self.label_0.place(x=90,y=53)

        self.label_1 = Label(f, text="First Name",width=20,font=("bold", 10))
        self.label_1.place(x=80,y=130)

        self.entry_1 = Entry(f, textvar=self.Fname)
        self.entry_1.place(x=240,y=130)

        self.label_2 = Label(f, text="Last Name",width=20,font=("bold", 10))
        self.label_2.place(x=79,y=180)

        self.entry_2 = Entry(f, textvar=self.Lname)
        self.entry_2.place(x=240,y=180)

        self.label_3 = Label(f, text="Age",width=20,font=("bold", 10))
        self.label_3.place(x=79,y=230)

        self.entry_3 = Entry(f, textvar=self.Age)
        self.entry_3.place(x=240,y=230)

        self.label_4 = Label(f, text="Gender",width=20,font=("bold", 10))
        self.label_4.place(x=79,y=280)

        self.entry_4 = Entry(f, textvar=self.Gender)
        self.entry_4.place(x=240,y=280)

        self.label_5 = Label(f, text="DOB",width=20,font=("bold", 10))
        self.label_5.place(x=79,y=320)

        self.entry_5 = Entry(f, textvar=self.Dob)
        self.entry_5.place(x=240,y=320)

        self.btn = Button(f, text='Submit',width=20, anchor="center", command=self.insertnew)
        self.btn.place(x=180,y=370)

    def insertnew(self):
        global ReturnName,Age,path
        fname=self.Fname.get()
        lname=self.Lname.get()
        age=self.Age.get()
        gender=self.Gender.get()
        dob=self.Dob.get()
        if(age<0 or age>15):
            tkinter.messagebox.showinfo("Error", "Age out of bounds, only up to 15")
            exit()
        dob=dob.replace("/","-")
        self.fullname = fname + " " + lname + " " + str(dob)
        self.fullname = self.fullname.lower()
        path = self.fullname
        ReturnName = self.fullname
        Age = age
        #Check entered details with existing details on firebase to verify staff or not
        print(self.Fname.get())
        today = date.today()
        #to check if primary key aready EXISTS
        self.f.destroy()
        #global root
        self.f.quit()
        self.master.destroy()
        self.master.quit()

yes =0
no=0
might=0
basal_age=0
vli=0
index_arr = [0] * 90
agetoadd = 0
age_range = {0:[3,17],1:[10,34],2:[17,44],3:[24,50],4:[31,56],5:[38,61],6:[45,65],7:[51,70],8:[57,74],9:[62,77],10:[67,81],11:[71,84],12:[75,89],13:[78,89],14:[81,89],15:[83,89]}
age_range_list = [17,34,44,50,56,61,65,70,74,77,81,84,89,89,89,89]
curr_index = 0
cage = 0
vlf = age_range[cage][1]
SA_mapping = [0,0.06,0.12,0.18,0.24,0.30,0.35,0.41,0.47,0.53,0.59,0.65,0.71,0.77,0.83,0.89,0.94,1.0,1.06,1.12,1.18,1.24,1.30,1.35,1.41,1.47,1.53,1.59,1.65,1.71,1.77,1.83,1.89,1.94,2.00,2.1,2.2,2.3,2.4,2.5,2.6,2.7,2.8,2.9,3.0,3.2,3.3,3.5,3.7,3.8,4.0,4.2,4.3,4.5,4.7,4.8,5.0,5.2,5.4,5.6,5.8,6.0,6.3,6.5,6.8,7.0,7.2,7.4,7.6,7.8,8.0,8.3,8.5,8.8,9.0,9.3,9.7,10.0,10.3,10.5,10.8,11.0,11.3,11.7,12.0,12.6,13.2,13.8,14.4,15.0] #TODO
correct_counter = 0
wrong_counter = 0
correct_ques = 0

class Question:
    def __init__(self, question, answers):
        self.question = question
        self.answers = answers
        global vli
        vli = 0

    def check(self, letter, view):
        global yes
        global no
        global might
        global basal_age
        global index_arr
        global vli
        global vlf
        global agetoadd
        global correct_counter
        global wrong_counter
        global correct_ques
        agemap = {0:0.7, 34:1.2, 44:2, 56:2.4, 61:3, 65:2.4, 70:3, 74:4, 77:3, 81:4, 84:7.2}
        for (k, v) in agemap.items():
            if vli == k:
                agetoadd = v

        if(letter == "A"):
            label = Label(view, text="Yes")
            yes += 1
            if(vli==15 or vli==32):
                basal_age=round(basal_age+0.1,2)
            basal_age=round(basal_age+agetoadd,2)
            vli += 1
            index_arr[vli] = 1
            correct_ques = vli
            correct_counter +=1 #TODO
        elif(letter == "B"):
            label = Label(view, text="No")
            no +=1
            vli += 1
            index_arr[vli] = 0
            wrong_counter+=1 #TODO
        else:
            label = Label(view, text="Could have passed")
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
        elif vli< 84:
            return 81
        elif vli< 89:
            return 84

    def getView(self, window,REF):
        view = Frame(window)
        Label(view, text=self.question).pack()
        self.REF = REF
        Button(view, text=self.answers[0], command=lambda *args: self.check("A", view),width=50).pack()
        Button(view, text=self.answers[1], command=lambda *args: self.check("B", view),width=50).pack()
        Button(view, text=self.answers[2], command=lambda *args: self.check("C", view),width=50).pack()

        return view

    def unpackView(self, view):
        view.pack_forget()
        self.REF.askQuestion()

questions = []
filepath=os.path.dirname(os.path.abspath(__file__))+"/tests"
file = open(filepath+"/VL/vineland2questions.txt", "r",encoding='windows-1252')
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
  
class Caller:
    def __init__(self,age):
        global cage,vlf
        cage = age
        vlf = age_range[cage][1]
        self.window = Tk()
        w = 600
        h = 500
            # get screen width and height
        ws = self.window.winfo_screenwidth() # width of the screen
        hs = self.window.winfo_screenheight() # height of the screen
            # calculate x and y coordinates for the Tk root window
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
            # set the dimensions of the screen
            # and where it is placed
        self.window.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.window.title("Vineland Social Maturity Test")
        label_heading = Label(self.window, text="VINELAND SOCIAL MATURITY TEST",bg="black",fg="white",font=('Helvetica', '20'))
        label_heading.pack()
        self.label_des = Label(self.window, text="",fg="blue",font=('15'))
        self.label_des.pack()
        self.button = Button(self.window, text="Start", command=self.askQuestion)
        self.button.pack()
        self.window.mainloop()

    def askQuestion(self):
        global questions, button, yes, no,might, number_of_questions,social_quotient,index_arr,vlf,vli,correct_counter,correct_ques,wrong_counter,age_range_list, curr_index, SA_mapping,basal_age,cage
        window = self.window
        if vli == age_range_list[curr_index]:
            if correct_counter!=0:
                correct_counter = 0
                curr_index+=1
            else: 
                wrong_counter = wrong_counter - (vli-correct_ques)
                basal_age = (correct_ques-wrong_counter)
                basal_age = SA_mapping[basal_age]
                social_quotient = (basal_age/cage)*100
                print("wrong",wrong_counter)
                print("last correct",correct_ques)
                print("basal age",basal_age)
                Label(window,text="Thank you for answering the questions.\n basal age = " + str(basal_age)).pack()
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
                elif ((social_quotient>=70) and (social_quotient<90)):
                    ID = True
                    Label(window, text="Boderline Intellectual Disability").pack()
                else:
                    ID = False
                    Label(window, text="Normal IQ").pack()
                window.configure(background='peach puff')
                buttonn = Button(window,text="Next",command=self.quitf)
                buttonn.pack(side=BOTTOM)
                self.returnval = float(social_quotient) 
                return
            if vli == 89:
                wrong_counter = wrong_counter - (vli-correct_ques)
                basal_age = (correct_ques-wrong_counter)
                basal_age = SA_mapping[basal_age]
                social_quotient = (basal_age/cage)*100
                print("wrong",wrong_counter)
                print("last correct",correct_ques)
                print("basal age",basal_age)
                Label(window,text="Thank you for answering the questions.\n basal age = " + str(basal_age)).pack()
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
                elif ((social_quotient>=70) and (social_quotient<90)):
                    ID = True
                    Label(window, text="Boderline Intellectual Disability").pack()
                else:
                    ID = False
                    Label(window, text="Normal IQ").pack()
                window.configure(background='peach puff')
                buttonn = Button(window,text="Next",command=self.quitf)
                buttonn.pack(side=BOTTOM)
                self.returnval = float(social_quotient) 
                return
        self.button.pack_forget()
        self.label_des.pack_forget()
        questions[vli].getView(window,self).pack() 
        
    def quitf(self):
        self.window.destroy()
        self.window.quit()

    def getresult(self):
        return self.returnval   

class Report:
    def __init__(self):
        self.pdf = FPDF() 
    def genrep(self,name,age,sch,vi):
        self.pdf.add_page()
        self.text = 'Final report'
        self.name = name
        self.vi = vi
        self.age = age
        self.sch = sch

        #Setting the threshold values for each test
        self.viv =90
        #Final report text
        self.pdf.set_font("Arial",size=24)
        self.pdf.cell(60, 10,txt=self.text,ln = 50,align="L")
        #First Sep line
        self.pdf.set_draw_color(0, 0, 0)
        self.pdf.set_line_width(0.5)
        self.pdf.line(0, 20, 500, 20)
        #Vertical line
        self.pdf.set_draw_color(0, 0, 0)
        self.pdf.set_line_width(0.5)
        self.pdf.line(10, 0, 10, 1000)
        
        #Displaying student details
        #Name
        self.pdf.set_font("Arial",size=14)
        self.pdf.cell(60,7,txt="Name:"+self.name,ln = 1,align="L")
        #Age
        self.pdf.set_font("Arial",size=14)
        self.pdf.cell(60, 7,txt="Age:"+str(self.age),ln = 1,align="L")
        #School
        self.pdf.set_font("Arial",size=14)
        self.pdf.cell(60, 7,txt="School:"+self.sch,ln = 1,align="L")
        #Bottom Line for the report 
        self.pdf.set_draw_color(0, 0, 0)
        self.pdf.set_line_width(0.5)
        self.pdf.line(0, 40, 500, 40)
        #Report Image
        filepath=os.path.dirname(os.path.abspath(__file__))
        self.path = filepath+'/Images/Report.png'
        self.pdf.image(self.path, x = 15, y = 150, w = 200, h =100)

        #Data list to plot the data
        self.data = [['Name of the test','Expected Score','Score Obtained','Remark']]

        #Adding the scores to data lsit
        #VI
        self.temp = []        
        self.temp.append("VI")
        self.temp.append(str(self.viv))
        self.temp.append(str(round(self.vi,3)))
        if self.vi < self.viv:
            self.temp.append("Intellectual Disability")
        else:
            self.temp.append("Normal Score")
        self.data.append(self.temp)
        
        #Setting table parameters
        self.col_width = self.pdf.w / 4.5
        self.row_height = self.pdf.font_size+2
        self.spacing = 2
        #Drawing the table
        for row in self.data:
            for item in row:
                self.pdf.cell(self.col_width, self.row_height*self.spacing,txt=item, border=1)
            self.pdf.ln(self.row_height*self.spacing)
        self.pdf.output(filepath+"/Reports/"+self.name+".pdf")

def VLCALL():
    global Age
    c = Caller(Age)
    global VLresult
    VLresult = c.getresult()

def gph():
    global VLresult,VLresultl
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
    frame = Frame(root,width=750,height=750)
    frame.pack()
    plt = Plot(frame)
    VLresultl.append(VLresult)
    plt.plot(VLresultl)
    root.mainloop() 

def TAKETEST():
    global test_number,BSTresult,GDTresult,VLresult,RPMresult,pathdir
    global RPMresultl,BSTresultl,GDTresultl,VLresultl 
    global Name,Age
    RPMresultl = []
    BSTresultl = []
    GDTresultl = []
    VLresultl = []
    test_number+=1
    VLCALL()
    gph()
    r = Report()
    r.genrep(Name,Age,"SSRVM BANGALORE EAST",VLresult)

def FIREBASECALL():
    root = Tk()
    w=500
    h=500
    # get screen width and height
    ws = root.winfo_screenwidth() # width of the screen
    hs = root.winfo_screenheight() # height of the screen
    # calculate x and y coordinates for the Tk root window
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    # set the dimensions of the screen
    # and where it is placed
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    root.title("Login")
    root.configure(background='peach puff')
    f = Frame(root,width=750,height=750)
    f.configure(background='peach puff')
    f.pack()
    login = LoginTeacher(f,root,test_number)
    root.mainloop()
    global Name,Age,pathdir
    choice = login.returnchoice()
    if choice == 1:
        Name,pathdir = login.returnnametocalling()
        Age = login.returnagetocalling()
        TAKETEST()

FIREBASECALL()

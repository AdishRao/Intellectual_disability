from tkinter import Tk, Frame, Label, Button ,Entry
#from time import sleep

class Question:
    def __init__(self, question, answers):
        self.question = question
        self.answers = answers
 #       self.c_age=0
 #    def onok(self):
 #       self.c_age= entry.get()

    def check(self, letter, view):
        global yes
        global no
        global might
        global basal_age
        global index_arr
        global i
        if(letter == "A"):
            label = Label(view, text="yes")
            yes += 1
            basal_age+=0.7
            i += 1
            index_arr[i] = 1
        elif(letter == "B"):
            label = Label(view, text="no")
            no +=1
            i += 1
            index_arr[i] = 2
        else:
            label = Label(view, text="could have passed")
            might +=1
            basal_age += 0.35
            i += 1
            index_arr[i] = 3

        if (index_arr[i]==1 and index_arr[(i)-2]==1 and index_arr[(i)-1]==3):
            basal_age += 0.35
        print("current basal age is ")
        print(basal_age, " months")

        label.pack()
        view.after(1000, lambda *args: self.unpackView(view))


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
    global questions, window, index, button, yes, no,might, number_of_questions,social_quotient
    if(len(questions) == index + 1):
        #Label(window, text="Thank you for answering the questions. 1. yes " + str(yes) +" 2. no " +str(no) + " 3.might"+str(might) + " of " + str(number_of_questions) + " questions answered right||basal_age =  "+str(basal_age),font=('15')).pack()
        Label(window,text="Thank you for answering the questions.\n basal_age = " + str(basal_age)).pack()
        social_quotient=(basal_age/(10*12))*100#chrono age taken as 10 as all question included are till 9-10 yearsold
        Label(window, text="social quotient = " + str(social_quotient)).pack()
        if(social_quotient<20):
            Label(window, text="Profound Intelletual disability").pack()
        elif((social_quotient>=20) and(social_quotient<35)):
            Label(window, text="Severe Intelletual disability").pack()
        elif((social_quotient>=35) and (social_quotient<50)):
            Label(window, text="Moderate Intelletual disability").pack()
        elif((social_quotient>=50) and (social_quotient<70)):
            Label(window, text="Mild Intelletual disability").pack()
        else:
            Label(window, text="Normal IQ").pack()

        return
    button.pack_forget()
    label_des.pack_forget()
    label_entry.pack_forget()
    entry.pack_forget()
    index += 1
    questions[index].getView(window).pack()

questions = []
file = open("vineland2questions.txt", "r")
line = file.readline()
while(line != ""):
    questionString = line
    answers = []
    for i in range (3):
        answers.append(file.readline())

    questions.append(Question(questionString, answers))
    line = file.readline()
file.close()
index = -1
yes =0
no=0
might=0
basal_age=0
i=0
index_arr = [0] * 90
number_of_questions = len(questions)

window = Tk()
window.geometry("600x300")
label_heading = Label(window, text="VINELAND SOCIAL MATURITY TEST",bg="black",fg="white",font=('Helvetica', '20'))
label_heading.pack()
label_des = Label(window, text="\n\nThe Vineland Social Maturity Scale (VSMS) measures the differential social\ncapacities of an individual. It provides an estimate of Social Age (SA) and Social\nQuotient (SQ), and shows high correlation (0.80) with intelligence. It is designed to\nmeasure social maturation in eight social areas: Self-help General (SHG), Self-help\nEating (SHE), Self-help Dressing (SHD), Self direction (SD), Occupation (OCC),\nCommunication (COM), Locomotion (LOM), and Socialization (SOC).",fg="blue",font=('15'))
label_des.pack()
label_entry = Label(window,text="Enter the age of child")
label_entry.pack()
entry = Entry(window, width=10)
entry.pack()
#button = Button(window, text="Start", command = lambda:[askQuestion,onok(self)])
button = Button(window, text="Start", command=askQuestion)
button.pack()
window.mainloop()

#button = Button(window, text="Start", command = lambda x:askQuestion & onok
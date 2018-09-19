from tkinter import *

q=[
    "1. “Crows”, Laugh",
    "2. Balance head  ",
    "3. Grasps objects within reach",
    "4. Reaches for familiar persons",
    "5. Rolls over, (unassisted)",
    "6. Reaches for nearby objects ",
    "7. Occupies self-upright",
    "8. Sits unsupported",
    "9. Pulls self upright",
    "10. “Talks”, imitates sounds",
    "11. Drinks from cup or glass assisted"
    "12. Moves about on floor (creeping, crawling)",
    "13. Grasps with thumb and finger",
    "14. Demands personal attention",
    "15. Stands alone",
    "16. Does not drool",
    "17. Follows simple instructions",
    "18. Walks about room unattended",
    "19. Marks with pencil or crayon or chalk",
    "20. Masticates (chews) solid or semi-solid food",
    "21. Pulls off clothes",
    "22. Transfers objects",
    "23. Overcomes simple obstacles",
    "24. Fetches or carries familiar objects",
    "25. Drinks from cup or glass",
    "26. Walks without support",
    "27. Plays with other children",
    "28. Eats with own hands (biscuits, bread, etc.)",
    "29. Goes about hours or yard",
    "30. Discriminates edible substances from non-edibles",
    "31. Uses names of familiar objects",
    " 32. Walks upstairs unassisted",
    "33. Unwraps sweets, chocolates",
    "34. Talks in short sentences"
]

options = [    ["yes","no","could have passed the item if the opportunity was present"],]*34

class Quiz:
    def __init__(self,master):
        self.opt_selected=IntVar()
        self.basal_age=0
        self.qn=0
        self.correct = 0
        self.index_arr=[0]*34
        self.i=0
        self.a=0

        self.menu = Menu(root)
        root.config(menu=self.menu)
        self.submenu = Menu(self.menu)
        self.menu.add_cascade(label="enter the age of child", menu=self.submenu)
        self.submenu.add_command(label="0-1 years", command=self.zero)
        self.submenu.add_command(label="1-2 years", command=self.one)
        self.submenu.add_command(label="2-3 years", command=self.two)

        self.submenu.add_command(label="3-4 years", command=self.three)
        self.submenu.add_command(label="4-5 years", command=self.four)
        self.submenu.add_command(label="5-6 years", command=self.five)
        self.submenu.add_command(label="6-7 years", command=self.six)
        self.submenu.add_command(label="7-8 years", command=self.seven)
        self.submenu.add_command(label="8-9 years", command=self.eight)
        self.submenu.add_command(label="9-10 years", command=self.nine)
        self.submenu.add_command(label="10-11 years", command=self.ten)
        self.submenu.add_command(label="11-12 years", command=self.eleven)
        self.submenu.add_command(label="12-15 years", command=self.twelve)
        self.submenu.add_separator()
        self.submenu.add_command(label="exit", command=self.donothing)


        self.ques=self.create_q(master,self.qn)
        self.opts=self.create_options(master,3)
        self.display_q(self.qn)
        self.button=Button(master,text="Back",command=self.back_btn)
        self.button.pack(side=BOTTOM)
        self.button = Button(master, text="Next",command=self.next_btn)
        self.button.pack(side=BOTTOM)

    def donothing(self):
            root.destroy()
    def zero(self):
        self.a = 17
    def one(self):
        self.a = 34
    def two(self):
        self.a = 44
    def three(self):
        self.a = 50
    def four(self):
        self.a = 56
    def five(self):
        self.a = 61
    def six(self):
        self.a = 65
    def seven(self):
        self.a = 70
    def eight(self):
        self.a = 74
    def nine(self):
        self.a = 77
    def ten(self):
        self.a = 81
    def eleven(self):
        self.a = 84
    def twelve(self):
        self.a = 89

    def create_q(self,master,qn):
        w=Label(master,text=q[qn])
        w.pack(side=TOP)
        return w

    def create_options(self,master,n):
        b_val=0
        b=[]
        while b_val<n:
            btn = Radiobutton(master,text="foo",variable=self.opt_selected,value=b_val+1)
            b.append(btn)
            btn.pack(side=TOP,anchor="w")
            b_val=b_val+1
        return b

    def display_q(self,qn):
        b_val=0
        self.opt_selected.set(0)
        self.ques['text']=q[qn]
        for op in options[qn]:
            self.opts[b_val]['text']=op
            b_val=b_val+1

    def print_results(self):
        print("no of quetions answered",self.correct,"/",len(q))
        result_label = Label(root, text=self.basal_age)
        result_label.pack(side=BOTTOM)

    def back_btn(self):
        print("go back")

    def next_btn(self):
        if self.opt_selected.get()==1:
            self.basal_age+=0.7
            self.i += 1
            self.index_arr[self.i]=1
        elif self.opt_selected.get()==3:
            self.basal_age+=0.35
            self.i += 1
            self.index_arr[self.i]=3
        else:
            self.i += 1
            self.index_arr[self.i]=2

        if (self.index_arr[self.i]==1 and self.index_arr[(self.i)-2]==1 and self.index_arr[(self.i)-1]==3):
            self.basal_age += 0.35
        print("current basal age is ")
        print(self.basal_age," months")
        self.correct+=1
        self.qn=self.qn+1
        if self.qn>=(self.a):
            self.print_results()
            #root.destroy()
        else:
            self.display_q(self.qn)

root=Tk()
root.geometry("500x300")
app=Quiz(root)
root.mainloop()
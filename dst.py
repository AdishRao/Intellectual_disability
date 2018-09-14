from tkinter import *
from tkinter import ttk
import random

root = Tk()
root.title('Digit Span Test')
root.geometry("250x200")

class DST:
    def __init__(self, root, string_var):
        #variables
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

ft = DST(root, "Forward Score")
root.mainloop()

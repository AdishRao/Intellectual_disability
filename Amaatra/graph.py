import plotly as py
import plotly.graph_objs as go
import plotly.io as pio
from tkinter import *
from PIL import Image
from PIL import ImageTk
from tkinter import ttk
import sys

class Plot:
    def __init__(self,master):
        
        print('Starting the plot function')
        self.master=master
        frame1 = Frame(master,width=500,height=50)
        frame1.pack(side=TOP)
        maxlabel = Label(frame1, text = "BST min: 90| GDT min: 21| RPM min: 26| Vineland min: 90",wraplength=500,justify="left") #search
        maxlabel.pack()

    def plot(self,bst,rpm,gdt,vi):
        self.z = 0
        print(bst)

        i = 1
        y1 = []
        print(f'bst {bst} gdt {gdt} rpm {rpm} vi {vi}')
        for x1 in bst :
            y1.append(i)
            i = i+1
        t1 = dict(x=y1,y=bst)
        BST = go.Bar(t1,name='Binet Simon Test')

        i = 1
        y1 = []
        
        for x1 in gdt :
            y1.append(i)
            i = i+1
        t1 = dict(x=y1,y=gdt)
        GDT = go.Bar(t1,name="Gessel's Drawing Test")
        i = 1
        y1 = []
        
        for x1 in rpm :
            y1.append(i)
            i = i+1
        t1 = dict(x=y1,y=rpm)


        RPM = go.Bar(t1,name="Reaven's Progressive Matrix")
        i = 1
        y1 = []
        
        for x1 in vi :
            y1.append(i)
            i = i+1
        t1 = dict(x=y1,y=vi)
        VI = go.Bar(t1,name='Vineland Social Maturity Scale')

        fig = py.tools.make_subplots(rows=2, cols=2, subplot_titles=('BST', 'GDT','RPM', 'Vinelands'))

        fig.append_trace(BST, 1, 1)
        fig.append_trace(GDT, 1, 2)
        fig.append_trace(RPM, 2, 1)
        fig.append_trace(VI, 2, 2)

        fig['layout'].update(height=600, width=600, title='Test results comparison')
        pio.write_image(fig, 'Images/Report.png')
        frame2 = Frame(self.master,width=500,height=400)
        frame2.pack(side=TOP)
        photo = Image.open('Images/Report.png')
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



        
            
            

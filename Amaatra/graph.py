
import plotly as py
import webbrowser, os
import plotly.graph_objs as go
import plotly.io as pio
from tkinter import *
from PIL import Image
from PIL import ImageTk
from tkinter import ttk
import pandas as pd
import sys

class Plot:
    def __init__(self,master):
        
        print('Starting the plot function')
        self.master=master
        frame1 = Frame(master,width=500,height=50)
        frame1.pack(side=TOP)
        maxlabel = Label(frame1, text = "RPM min: 26| DST min: 26| BST min: 91| GDT min: 21| Vineland min: 91",wraplength=500,justify="left") #search
        maxlabel.pack()

    def plot(self,bst,gdt,rpm,vi):
        i = 1
        y = []
        
        for x in bst :
            y.append(i)
            i = i+1

        trace1 = go.Bar(bst, y)

        i = 1
        y = []
        
        for x in gdt :
            y.append(i)
            i = i+1

        trace2 = go.Bar(gdt, y)
        i = 1
        y = []
        
        for x in rpm :
            y.append(i)
            i = i+1

        trace3 = go.Bar(rpm, y)
        i = 1
        y = []
        
        for x in vi :
            y.append(i)
            i = i+1

        trace4 = go.Bar(vi, y)

        fig = py.tools.make_subplots(rows=2, cols=2, subplot_titles=('BST', 'GDT','RPM', 'Vinelands'))

        fig.append_trace(trace1, 1, 1)
        fig.append_trace(trace2, 1, 2)
        fig.append_trace(trace3, 2, 1)
        fig.append_trace(trace4, 2, 2)

        fig['layout'].update(height=600, width=600, title='Test results comparison')
        pio.write_image(fig, 'Report.png')
        #py.offline.plot(fig, filename='results.html')
        #webbrowser.open('file://' + os.path.realpath('results.html'))
        frame2 = Frame(self.master,width=500,height=400)
        frame2.pack(side=TOP)
        photo = Image.open('Report.png')
        photo = photo.resize((500, 400), Image.ANTIALIAS)
        self.render = ImageTk.PhotoImage(photo)
        photolabel = Label(frame2,image=self.render)
        photolabel.image = self.render
        photolabel.pack()
        endb = Button(self.master,text="Finish",command = self.quitb)
        endb.pack(side=BOTTOM)

    def quitb(self):
        self.master.destroy()
        self.master.quit()
        
print('Plot successful')


        
            
            

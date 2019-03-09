from tkinter import *
from PIL import Image
from PIL import ImageTk
from tkinter import ttk
#import all classes
from tests.rpm import *
from tests.bst import *
from tests.gdt import *
from tests.vl import *
from AmaatraLoginFirebase import *
from graph import Plot

#results to store on cloud
RPMresult = BSTresult = GDTresult = VLresult = 0
RPMresultl = list() 
BSTresultl = list()
GDTresultl = list()
VLresultl = list()

Name = ""
Age = 0
test_number = 0

def RPMCALL():
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
    RPMcall = RPM(root,6)
    root.mainloop()
    global RPMresult
    RPMresult=RPMcall.getresult()

def BSTCALL():
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
    BSTcall = BST(root,6)
    root.mainloop()
    global BSTresult
    BSTresult=BSTcall.getresult()

def GDTCALL():
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
    global GDTresult
    GDTresult=GDTcall.getresult()

def VLCALL():
    c = Caller()
    global VLresult
    VLresult = c.getresult()

def gph():
    print("In Graph")
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
    plt = Plot(root)
    plt.plot(RPMresultl)
    root.mainloop() 


def TAKETEST():
    global test_number
    test_number = 1
    RPMCALL()
    BSTCALL()
    GDTCALL()
    VLCALL()
    gph()

def FIREBASECALL():
    root = Tk()
    root.geometry('500x500')
    root.title("Amaatra-Login")
    f = Frame(root,width=750,height=750)
    f.pack()
    login = LoginTeacher(f,root)
    root.mainloop()
    global Name,Age
    Name = login.returnnametocalling()
    Age = login.returnagetocalling()
    choice = login.returnchoice()
    if choice == 1:
        TAKETEST()
    if choice == 2:
        #SHOWRESULTS()
        pass
    if choice == 3:
        #RETAKETEST()
        pass

FIREBASECALL()

print(test_number)

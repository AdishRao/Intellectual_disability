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

Name = ""
Age = 0
test_number = 0

def RPMCALL():
    global Age
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
    RPMcall = RPM(root,Age)
    root.mainloop()
    global RPMresult
    RPMresult=RPMcall.getresult()

def BSTCALL():
    global Age
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
    BSTcall = BST(root,Age)
    root.mainloop()
    global BSTresult
    BSTresult=BSTcall.getresult()

def GDTCALL():
    global Age
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
    GDTcall = GDT(root,Age)
    root.mainloop() 
    global GDTresult
    GDTresult=GDTcall.getresult()

def VLCALL():
    global Age
    c = Caller(Age)
    global VLresult
    VLresult = c.getresult()

def gph():
    global RPMresult,BSTresult,GDTresult,VLresult,RPMresultl,BSTresultl,GDTresultl,VLresultl
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
    BSTresultl.append(BSTresult)
    RPMresultl.append(RPMresult)
    VLresultl.append(VLresult)
    GDTresultl.append(GDTresult)
    plt.plot(BSTresultl,RPMresultl,GDTresultl,VLresultl)
    root.mainloop() 

def TAKETEST():
    global test_number,BSTresult,GDTresult,VLresult,RPMresult
    global RPMresultl  
    global BSTresultl 
    global GDTresultl 
    global VLresultl 
    RPMresultl = []
    BSTresultl  = []
    GDTresultl = []
    VLresultl  = []
    test_number = 1
    #RPMCALL()
    #BSTCALL()
    #GDTCALL()
    VLCALL()
    print(f'BST {BSTresult} GDT {GDTresult} VL {VLresult} RPM {RPMresult}' )
    gph()

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

print("Test Number",test_number)
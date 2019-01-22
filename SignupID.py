from tkinter import *
from PIL import ImageTk, Image
import os
import tkinter.messagebox
import pyrebase
import datetime


config = {
    "apiKey": "AIzaSyCvpPBVuvkQd2D4RYOutvbDvmC_od8U3_M",
    "authDomain": "example1-92a61.firebaseapp.com",
    "databaseURL": "https://example1-92a61.firebaseio.com",
    "projectId": "example1-92a61",
    "storageBucket": "example1-92a61.appspot.com",
    "messagingSenderId": "235374803572"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()


#def setBackground(root):
#img = ImageTk.PhotoImage(Image.open("img1.jpg"))
#label = ttk.Label(root,image = img)
#label.image = img
#label.grid(row=0,column=0,columnspan=15,rowspan=15)

#def setStyle(root):
#style = ttk.Style(root)
#style.theme_use('aqua')
#style.configure('.',font=('Helvetica', 20,))


#root = Tk()
#root.title("Checking background images")

top = Tk()

C = Canvas(top, bg="blue", height=750, width=750)
filename = PhotoImage(file = "img2.png")
background_label = Label(top, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

c = Button(text="        OK         ")
c.pack()

C.pack()
top.mainloop()
#img = ImageTk.PhotoImage(Image.open("img1.jpg"))
#label = ttk.Label(root,image = img)
#label.image = img
#label.grid(row=0,column=0,columnspan=25,rowspan=25)

#style = ttk.Style(root)
#style.theme_use('aqua')
#style.configure('.',font=('Helvetica', 15,))
###
#photo = PhotoImage(file = "img2.png")
#f = Frame(root,width=500,height=500)
#f.pack()
#f1 = Label(f,image=photo)
#f1.pack()

#c = Button(text="        OK         ")
#c.pack()
#root.mainloop()

#image2 =Image.open('C:\\Users\\adminp\\Desktop\\titlepage\\front.gif')

#background_image= PhotoImage("img3.gif")
#background_label = Label(root, image=background_image)
#background_label.image = background_image
#background_label.place(x=0, y=0, relwidth=1, relheight=1)





#btn1 = Button(root, text='New Student',width=20,bg='red',fg='white', anchor="center")
#btn1.grid(row=0,column=1,sticky='NSEW',ipady=10, ipadx=20)
#btn2 = Button(root, text='Student Details',width=20,bg='red',fg='white', anchor="center")
#btn2.grid(row=1,column=1,sticky='NSEW',ipady=10, ipadx=20)


c = Button(text="        OK         ")
c.grid()
#root.mainloop()

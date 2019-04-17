from tkinter import *
from PIL import Image
from PIL import ImageTk
import pyrebase
from tkinter import ttk

config = {
    "apiKey": "AIzaSyDc3JTW47RqgD1oAtbar5n4HZ6nDEVBXt4",
    "authDomain": "intellectualdisability-a9894.firebaseapp.com",
    "databaseURL": "https://intellectualdisability-a9894.firebaseio.com",
    "projectId": "intellectualdisability-a9894",
    "storageBucket": "intellectualdisability-a9894.appspot.com",
    "messagingSenderId": "255261471519"
}
firebase = pyrebase.initialize_app(config)
auth =firebase.auth()
i=0
sid=''

class login:
    def __init__(self,master):
        self.master = master
        self.email = Label(master,text="Enter Email:")
        self.email.place(x=200,y=195,anchor="center")
        self.password = Label(master,text="Enter Password:")
        self.password.place(x=135,y=225)
        self.emailid= Entry(self.master)
        self.psswd= Entry(self.master)
        self.emailid.place(x=250,y=180)
        self.psswd.place(x=250,y=220)
        self.login = Button(master,text="Login",command=self.loginb)
        self.login.place(x=250,y=450,anchor="center")


    def loginb(self):
        try:
            email = self.emailid.get()
            password = self.psswd.get()
            print(email)
            print(password)
            user = auth.sign_in_with_email_and_password(email,password)
            global i,sid
            info=auth.get_account_info(user['idToken'])
            sid=str(info['users'][0]['localId'])
            i=3 
            self.master.destroy()
            self.master.quit()
        except:
            self.errorlabel = Label(self.master, text = "Wrong email or password, try again!")
            self.errorlabel.pack(side=BOTTOM)
            self.emailid.destroy()
            self.psswd.destroy()
            self.emailid= Entry(self.master)
            self.psswd= Entry(self.master)
            self.emailid.place(x=250,y=180)
            self.psswd.place(x=250,y=220)


class displayinfo: 
    def bla(self,sample_string):
        print(sample_string)
        self.frame.destroy()
        frame1 = Frame(self.master,width=500,height=50)
        frame1.pack(side=TOP)
        maxlabel = Label(frame1, text = "RPM min: 26| DST min: 26| BST min: 91| GDT min: 21| Vineland min: 91",wraplength=500,justify="left") #search
        maxlabel.pack()
        frame2 = Frame(self.master,width=500,height=400)
        frame2.pack(side=TOP)
        storage = firebase.storage()
        storage.child("report/"+str(sample_string)+".jpg").download('Report/'+str(sample_string)+'.png')
        photo = Image.open('Report/'+sample_string+'.png')
        photo = photo.resize((500, 400), Image.ANTIALIAS)
        self.render = ImageTk.PhotoImage(photo)
        photolabel = Label(frame2,image=self.render)
        photolabel.image = self.render
        photolabel.pack()
    def __init__(self,master):
        self.master=master
        self.frame = Frame(master,width=500,height=500)
        self.frame.pack()
        global sid
        db = firebase.database()
        self.useruid = []
        self.userval = []
        self.b1 =[]
        count = 0
        all_users = db.child("Doc").child(sid).get()
        for user in all_users.each():
            self.useruid.append(str(user.key()))
            self.userval.append(user.val())
            self.b1.append(count)
            print(str(user.key()))
            self.b1[count] = Button(self.frame,text=str(user.val()[str(user.key())]),command=lambda i=str(user.key()):self.bla(i))
            self.b1[count].pack()
            Label(self.frame).pack()
            count+=1
        #print(b1.index())


while i==0:
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
    an = login(root)
    root.mainloop()

while i==3:
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
    an = displayinfo(root)
    root.mainloop()
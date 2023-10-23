from tkinter import *
root=Tk()
root.geometry("500x500")
def getvals():
    print(f"The value of user name is {userval.get()}")
    print(f"The value of password is {passval.get()}")
user=Label(root,text="User name",borderwidth=8,relief=SUNKEN)
password=Label(root,text="Password",borderwidth=8,relief=SUNKEN)
user.grid()
password.grid(row=1)

# Variable classes in tkinter
# BooleanVar,DoubleVar,IntVar,StringVar

userval=StringVar()
passval=StringVar()
userentry=Entry(root,textvariable=userval)
passentry=Entry(root,textvariable=passval)
userentry.grid(row=0,column=1)
passentry.grid(row=1,column=1)
Button(root,text="ENTRY",font="bold",command=getvals).grid()
root.mainloop()

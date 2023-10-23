from tkinter import *
root=Tk()
root.geometry("800x500")
def hello():
    print("Hello Tkinter")
def name():
    print("My name is Saad")
f1=Frame(root,borderwidth=8,bg="grey",relief=SUNKEN)
f1.pack(side=LEFT,anchor="nw")

b1=Button(f1,fg="red",text="Print Now",command=hello)
b1.pack(side=LEFT,anchor="nw",padx=23)
b2=Button(f1,fg="red",text="Tell me name now",command=name)
b2.pack(side=LEFT,anchor="nw",padx=23)
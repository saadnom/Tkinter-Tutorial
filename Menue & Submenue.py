from tkinter import *
root=Tk()
root.geometry("533x536")
root.title("Pycharm")
def fun1():
    print("You click on New Project")
mymenu=Menu(root)
mymenu.add_command(label="File",command=fun1)
mymenu.add_command(label="Exit",command=quit)
root.config(menu=mymenu)


def fun1():
    print("You click on New Project")
def fun2():
    print("You click on Save")
def fun3():
    print("You click on Save As")
def fun4():
    print("You click on Print")
mymenubar=Menu(root)
m1=Menu(mymenubar,tearoff=0)
m1.add_command(label="New Project",command=fun1)
m1.add_command(label="Save",command=fun2)
m1.add_separator()
m1.add_command(label="Save As",command=fun3)
m1.add_command(label="Print",command=fun4)
root.config(menu=mymenubar)
mymenubar.add_cascade(label='File',menu=m1)
root.mainloop()
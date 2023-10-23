from tkinter import *
root=Tk()
root.geometry("380x380")
def Saad(event):
    print(f"You click the button at {event.x},{event.y}")
widget=Button(root,text="Click me please")
widget.pack()
widget.bind("<Button-1>",Saad)
widget.bind("<Triple-1>",quit)
root.mainloop()
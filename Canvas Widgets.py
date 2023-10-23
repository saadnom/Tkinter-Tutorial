from tkinter import *
root=Tk()
canvas_width=800
canvas_height=400
root.geometry(f'{canvas_width}x{canvas_height}')
root.title("My GUI")
can_width=Canvas(root,width=canvas_width,height=canvas_height)
can_width.pack()
can_width.create_line(0,0,800,400,fill='blue')
can_width.create_line(0,400,800,0,fill='blue')
can_width.create_rectangle(3,7,700,300,fill='blue')
can_width.create_text(200,200,text='Python')
can_width.create_oval(300,200,550,310)
root.mainloop()

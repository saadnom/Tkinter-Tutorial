from tkinter import *
root=Tk()
root.geometry("500x500")
def getval():
    print("Sumbitting form")
    print(f"{namevalue.get(),phonevalue.get(),gendervalue.get(),emergencyvalue.get(),paymentvalue.get(),foodservicevalue.get()}")
    with open('record.txt','a') as f:
        f.write(f"{namevalue.get(),phonevalue.get(),gendervalue.get(),emergencyvalue.get(),paymentvalue.get(),foodservicevalue.get()}\n")

## Labels
Label(root,text="Welcome to Saad Travels",font="Algerian 15 bold ",pady=15).grid(row=0,column=3)
name=Label(root,text="Name")
phone=Label(root,text="Phone")
gender=Label(root,text="Gender")
emergency=Label(root,text="Emergency Contact")
payment=Label(root,text="Payment Mode")

## Packing the Labels
name.grid(row=1,column=2)
phone.grid(row=2,column=2)
gender.grid(row=3,column=2)
emergency.grid(row=4,column=2)
payment.grid(row=5,column=2)

## Tkinter variables
namevalue=StringVar()
phonevalue=StringVar()
gendervalue=StringVar()
emergencyvalue=StringVar()
paymentvalue=StringVar()
foodservicevalue=IntVar()

## Entries
nameentry=Entry(root,textvariable=namevalue)
phoneentry=Entry(root,textvariable=phonevalue)
genderentry=Entry(root,textvariable=gendervalue)
emergencyentry=Entry(root,textvariable=emergencyvalue)
paymententry=Entry(root,textvariable=paymentvalue)

## Packing the entries
nameentry.grid(row=1,column=3)
phoneentry.grid(row=2,column=3)
genderentry.grid(row=3,column=3)
emergencyentry.grid(row=4,column=3)
paymententry.grid(row=5,column=3)

## Check Box
foodservice=Checkbutton(text="Want to prebook your meals?",pady=12,variable=foodservicevalue)
foodservice.grid(row=6,column=3)
Button(text="Sumbit to Saad Travels",command=getval).grid(row=7,column=3)
root.mainloop()

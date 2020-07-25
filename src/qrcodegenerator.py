#__author__ = "adij1206"
#__date__ = "$Jul 25, 2020 9:59:37 AM$"

from Tkinter import *
import tkMessageBox as messageBox
import os
import pyqrcode
root = Tk()
root.title("QR Code Generator")

def generate():
    if len(subject.get()!=0):
        global myqr
        myqr = pyqrcode.create(subject.get())
        qrimage = myqr.xbm(scale = 8)
        global photo
        photo = BitmapImage(data=qrimage)
    else:
        messageBox.showinfo("Error!","Please Enter The Subject")
    try:
        showCode()
    except:
        pass

def showCode():
    global photo
    notificationLabel.config(image=photo)
    subLabel.config(text="Showing QR Code for:"+subject.get())

def save():
    dir = path1 = os.getcwd()+"\\QR Codes"
    
    if not os.path.exists(dir):
        os.makedirs(dir)
    try:
        if(len(name.get())!=0):
            qrImage = myqr.png(os.path.join(dir,name.get()+".png"),scale=8)
        else:
            messageBox.showinfo("Error!","File Name Cannot Be Empty!")
    except:
        messageBox.showinfo("Error!","Please Generate The Code First")
        
lab1 = Label(root,text="Enter Text/Link :",font=("Helvetica",12))
lab1.grid(row=0,column=0)

lab2 = Label(root,text="Enter File Name :",font=("Helvetica",12))
lab2.grid(row=1,column=0)

subject = StringVar()
subjectEntry = Entry(root,textvariable=subject,font=("Helvetica",12))
subjectEntry.grid(row=0,column=1)

name = StringVar()
nameEntry = Entry(root,textvariable=name,font=("Helvetica",12))
nameEntry.grid(row=1,column=1)

createButton = Button(root,text="Create QR Code",font=("Helvetica",12),width=15,command=generate)
createButton.grid(row=0,column=2)

notificationLabel = Label(root)
notificationLabel.grid(row=2,column=1)

subLabel = Label(root,text="")
subLabel.grid(row=3,column=1)

showButton = Button(root,text="Save as PNG",font=("Helvetica",12),width=15,command=save)
showButton.grid(row=1,column=2)

#Making Layout
total_rows=3
total_columns=3

for row in range(total_rows+1):
    root.grid_rowconfigure(row,weight=1)

for column in range(total_columns+1):
    root.grid_columnconfigure(column,weight=1)
root.mainloop()
    
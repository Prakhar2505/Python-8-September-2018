import tkinter
from tkinter import *

mainWindow = tkinter.Tk()
mainWindow.title("Example Tkinter")

headingLabel = tkinter.Label(mainWindow, text="Hello World")
headingLabel.pack()

userEntry = Entry(mainWindow)
userEntry.pack()

def fun():
    # print("Hello")
    name = userEntry.get()
    print("Hello your name is: ", name)

showButton = tkinter.Button(mainWindow, text="Button", command=fun())
showButton.pack()

mainWindow.mainloop()

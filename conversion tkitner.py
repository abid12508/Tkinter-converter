#import library
from tkinter import *
from turtle import *
import math
import string
import random
def maincode():
        #window
        window = Tk()
        #left and right frame
        leftframe = Frame(window)
        leftframe.pack(side=LEFT)
        rightframe = Frame(window)
        rightframe.pack(side=RIGHT)
        #win adj
        window.geometry("800x600")
        window.configure(bg="azure")
        window.title("Conversion")
        window.resizable(False, False)
        #input1
        input1 = Entry(window)
        input1.place(relx = 0.45, rely = 0.5, anchor = CENTER, width=250)
        #string variables
        a = StringVar()
        a.set("default")
        oc = StringVar(window)
        oc.set("Select")
        #main function
        def function1(x):
            if x == "Inches to feet":
                def inchestofeet(): 
                    x1 = input1.get()
                    label1e = float(x1)/12
                    label1 = Label(window, text=label1e, bg="lightblue", borderwidth=2, relief="solid")
                    label1.place(x=345, y=200, anchor=CENTER)
                    label1text = Label(window, text="(float of input)/12 = ans")
                    label1text.place(x=200, y=200, anchor=CENTER)
                inchestofeet()
                #answer button
                answeritf = Button(window, text='Answer (click me)', command=inchestofeet)
                answeritf.place(x=370, y=310)
            elif x == "Ounces to pounds":
                def ouncestopounds():
                    x2 = input1.get()
                    label2e = float(x2)/16
                    label2 = Label(window, text=label2e, bg="#f4b6b7", borderwidth=2, relief="solid")
                    label2.place(x=345, y=180, anchor=CENTER)
                    label2text = Label(window, text="(float of input)/16 = ans")
                    label2text.place(x=200, y=180, anchor=CENTER)
                ouncestopounds()
                #answer button
                answerotp = Button(window, text="Answer (click me)", command=ouncestopounds)
                answerotp.place(x=370, y=310)
            elif x == "Feet to yards":
                def feettoyards():
                    x3 = input1.get()
                    label3e = float(x3)/3
                    label3 = Label(window, text=label3e, bg="#90ee90", borderwidth=2, relief="solid")
                    label3.place(x=345, y=220, anchor=CENTER)
                    label1text = Label(window, text="(float of input)/3 = ans")
                    label1text.place(x=200, y=220, anchor=CENTER)
                feettoyards()
                #answerbutton
                answerfty = Button(window, text="Answer (click me)", command=feettoyards)
                answerfty.place(x=370, y=310)

            else:
                a.set("bye")
                print (a.get())
        #drop down menu
        drop = OptionMenu(window,oc, "Ounces to pounds","Inches to feet", "Feet to yards", command=function1)
        drop.place(x=250, y=310)


        #mainloop
        window.mainloop()
def password():
    passwordwindow = Tk()
    passwordwindow.geometry("400x200")
    passwordwindow.resizable(False, False)
    passwordwindow.title("Password")
    passwordwindow.configure(bg="azure")
    password = "12"
    Entrypassword = Entry(passwordwindow)
    Entrypassword.place(relx = 0.45, rely = 0.5, anchor = CENTER)
    def conditionals():
        if Entrypassword.get() == password:
            maincode()
            passwordwindow.destroy
        else:
            passwordtext = "Try again"
        passwordtextlabel = Label(passwordwindow, text=passwordtext)
        passwordtextlabel.place(relx = 0.45, rely = 0.2, anchor=CENTER)
    Passwordbutton = Button(passwordwindow, text="Finish", command=conditionals)
    Passwordbutton.place(relx = 0.45, rely = 0.6, anchor = CENTER)
    passwordwindow.mainloop()
password()
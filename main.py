from tkinter import *
from tkinter import messagebox
import base64
import os

def decrypt():
    print("")

def encrypt():
def main_screen():

    global screen
    global code
    global text1

    screen=Tk()
    screen.geometry("375*398")

    #icon
    image_icon=PhotoImage(file=keys.png)
    screen.iconphoto(False,image_icon)
    screen.title("Pct App")

    def reset():
        code.set("")
        text1.delete(1.0,END)

    Label(text="Enter Text for encryption and decryption", fg="black", font=("calibri",13)).place(x=10,y=10)
    text1=Text(font="robote 20",bg="white",relief=GROOVE,wrap=WORD,bd=0)
    text1.place(x=10,y=50,width=355,height=100)

    Label(text="Enter secret key for encryption and decryption", fg="black", font=("calibri",13)).place(x=10,y=170)

    code=StringVar()
    Entry(textvariable=code,width=19,bd=0,font=("arial",25),show="*").place(x=10,y=200)

    Button(text="ENCRYPT",height="2",width=23,bg="#ed3833",fg="white",bd=0,command=encrypt).place(x=10,y=250)
    Button(text="DECRYPT", height="2", width=23, bg="#00BD56", fg="white", bd=0,command=decrypt).place(x=200, y=250)
    Button(text="RESET", height="2", width=50, bg="#1089ff", fg="white", bd=0,command=reset).place(x=10, y=300)

    Entry(textvariable)

    screen.mainloop()

main_screen()


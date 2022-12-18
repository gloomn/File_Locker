# © 2022 Lee-Ki-Joon(Gloomn) <ithan0704@naver.com>

from tkinter import *
import tkinter as tk
import tkinter.messagebox as tkmb
from glui import standardButton
from glui import standardLabel
from glui import standardEntry
import subprocess
import os

#window default setting
window = tk.Tk()
window.configure(bg="#fff")
window.title("File Locker (Test Version: alphaV)")
window.geometry("600x300")
window.resizable(False, False)
window.eval('tk::PlaceWindow . center')

#login variables
user_id, password = StringVar(), StringVar()

def register():
    if(os.path.getsize("#221$07$14.txt") == 0):
        subprocess.call(["python", "registerForm.py"])
    else:
        tkmb.showerror("You are already Registered!", "Error: You are already registered!")


def login():
    print("login")

frameLogin = tk.Frame(window)
standardLabel.stdLabel(85, 20, 18, 1, "#000","#fff", "맑은 고딕", 30, "File Locker Program", "bold")
standardLabel.stdLabel(100, 125, 10, 1, "#000","#fff", "맑은 고딕", 13, "User Name:", "bold")
standardLabel.stdLabel(110, 155, 10, 1, "#000","#fff", "맑은 고딕", 13, "Password:", "bold")
standardLabel.stdLabel(500, 280, 15, 1, "#000","#fff", "맑은 고딕", 8, "©2022 Gloomn")
standardEntry.stdEntry(220, 130, 20,1,"#a2a4a6", "#000", "#fff", "맑은 고딕", "10", "User ID", user_id, '')
standardEntry.stdEntry(220, 160, 20,1,"#a2a4a6", "#000", "#fff", "맑은 고딕", "10", "Password", password, '*')
standardButton.fltButton(220,199,20, 2,login, "Login", "#ffcc66", "#141414")
standardButton.fltButton(220, 240, 20, 2, register, "Register", "#ffcc66", "#141414")


#window main icon change
window.iconbitmap('resources/mainIcon_Black.ico')
window.mainloop()
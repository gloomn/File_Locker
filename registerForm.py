# © 2022 Lee-Ki-Joon(Gloomn) <ithan0704@naver.com>
from tkinter import *
import tkinter as tk
import tkinter.messagebox as tkmb
from glui import standardLabel
from glui import standardButton
from glui import standardEntry
import hashlib

window = tk.Tk()
window.configure(bg="#fff")
window.title("File Locker (Register Form)")
window.geometry("400x500")
window.resizable(False, False)
window.eval('tk::PlaceWindow . center')

user_id, password, password_check = StringVar(), StringVar(), StringVar()

def register():
    if (password.get() == password_check.get()):
        userId_hash = hashlib.sha256(user_id.get().encode())
        password_hash = hashlib.sha256(password.get().encode())
        print(userId_hash.hexdigest())
        print(password_hash.hexdigest())
        f = open("#221$07$14.txt", 'w')
        f.write(userId_hash.hexdigest()+ "\n")
        f.write(password_hash.hexdigest())
        f.close()
        window.destroy()
    else:
        tkmb.showerror("Error:code1", "Error: Password and Password check is not matching!")

standardLabel.stdLabel(85, 50, 10, 1, "#000","#fff", "맑은 고딕", 30, "Register", "bold")
standardLabel.stdLabel(130, 150, 10, 1, "#000","#fff", "맑은 고딕", 10, "User Name" )
standardLabel.stdLabel(125, 200, 10, 1, "#000","#fff", "맑은 고딕", 10, "Password")
standardLabel.stdLabel(128, 250, 15, 1, "#000","#fff", "맑은 고딕", 10, "Password Check")
standardLabel.stdLabel(500, 280, 15, 1, "#000","#fff", "맑은 고딕", 8, "©2022 Gloomn")
standardEntry.stdEntry(130, 170, 20,1,"#a2a4a6", "#000", "#fff", "맑은 고딕", "10", "User ID", user_id, '')
standardEntry.stdEntry(130, 220, 20,1,"#a2a4a6", "#000", "#fff", "맑은 고딕", "10", "Password", password, '')
standardEntry.stdEntry(130, 270, 20,1,"#a2a4a6", "#000", "#fff", "맑은 고딕", "10", "Password Check", password_check, '')
standardButton.fltButton(130,300,20, 2,register, "Register", "#ffcc66", "#141414")


window.iconbitmap('resources/mainIcon_Black.ico')
window.mainloop()
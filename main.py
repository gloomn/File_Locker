#© 2022 Lee-Ki-Joon(Gloomn) <ithan0704@naver.com>

from tkinter import *
import tkinter as tk
from ui import standardButton
from ui import standardLabel
from ui import standardEntry

#window default setting
window = tk.Tk()
window.configure(bg="#fff")
window.title("File Locker (Test Version: alphaV)")
window.geometry("600x300")
window.resizable(False, False)
window.eval('tk::PlaceWindow . center')

#login variables
user_id, password = StringVar(), StringVar()

def login():
    print("helloworld")
frameLogin = tk.Frame(window)
standardLabel.stdLabel(5, 5, 10, 1, "#000","#fff", "맑은 고딕", 10, "User Name:")
standardLabel.stdLabel(5, 25, 10, 1, "#000","#fff", "맑은 고딕", 10, "Password:")
standardEntry.stdEntry(50, 50, 15,1,"#a2a4a6", "#000", "#fff", "맑은 고딕", "10", "User ID", user_id, '')
standardEntry.stdEntry(50, 100, 15,1,"#a2a4a6", "#000", "#fff", "맑은 고딕", "10", "Password", password, '*')
standardButton.fltButton(100,100,20, 2,login, "Login", "#ffcc66", "#141414")

#window main icon change
window.iconbitmap('resources/mainIcon_Black.ico')
window.mainloop()
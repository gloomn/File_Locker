#© 2022 Lee-Ki-Joon(Gloomn) <ithan0704@naver.com>

from tkinter import *
import tkinter as tk
from ui import flatButton

#window default setting
window = tk.Tk()
window.configure(bg="#fff")
window.title("File Locker (Test Version: alphaV)")
window.geometry("600x300")
window.resizable(False, False)
window.eval('tk::PlaceWindow . center')

#login variables
user_id, password = StringVar(), StringVar()

def cmd():
    print("helloworld")
frameLogin = tk.Frame(window)
tk.Label(window, text = "Username : ").grid(row = 0, column = 0, padx = 10, pady = 10)
tk.Label(window, text = "Password : ").grid(row = 1, column = 0, padx = 10, pady = 10)
tk.Entry(window, textvariable = user_id).grid(row = 0, column = 1, padx = 10, pady = 10)
tk.Entry(window, textvariable = password, show='*').grid(row = 1, column = 1, padx = 10, pady = 10)
flatButton.fltButton(100,100,20, 2, "Login", "#ffcc66", "#141414",cmd, "hand2")

#window main icon change
window.iconbitmap('resources/mainIcon_Black.ico')
window.mainloop()
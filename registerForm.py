# © 2022 Lee-Ki-Joon(Gloomn) <ithan0704@naver.com>
from tkinter import *
import tkinter as tk
from ui import standardLabel

window = tk.Tk()
window.configure(bg="#fff")
window.title("File Locker (Register Form)")
window.geometry("400x500")
window.resizable(False, False)
window.eval('tk::PlaceWindow . center')

user_id, password = StringVar(), StringVar()

standardLabel.stdLabel(5, 5, 10, 1, "#000","#fff", "맑은 고딕", 10, "User Name:")
standardLabel.stdLabel(5, 25, 10, 1, "#000","#fff", "맑은 고딕", 10, "Password:")
standardLabel.stdLabel(5, 45, 10, 1, "#000","#fff", "맑은 고딕", 10, "Password Check:")


window.iconbitmap('resources/mainIcon_Black.ico')
window.mainloop()
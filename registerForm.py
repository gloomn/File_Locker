# © 2022 Lee-Ki-Joon(Gloomn) <ithan0704@naver.com>
from tkinter import *
import tkinter as tk
import tkinter.messagebox as tkmb
from glui import standardLabel
from glui import standardButton
from glui import standardEntry
import hashlib
import openpyxl


def registerFormAction():
    #register form setting
    window = tk.Tk()
    window.configure(bg="#fff")
    window.title("File Locker (Register Form)")
    window.geometry("400x500")
    window.resizable(False, False)
    window.eval('tk::PlaceWindow . center')

    #get user's data from the entry
    user_id, password, password_check = StringVar(window), StringVar(window), StringVar(window)

    #register function when pressed the register button
    def register():
        #when password and password_check is same -> save data in excel file with hashed.
        if (len(user_id.get()) == 0 or len(password.get()) == 0 or len(password_check.get()) == 0):
            tkmb.showerror("Error Code: 002", "Please Insert your ID & Password!")
        elif (password.get() == password_check.get()):
            userId_hash = hashlib.sha256(user_id.get().encode())
            password_hash = hashlib.sha256(password.get().encode())
            #=============================================================================
            wb = openpyxl.Workbook()

            sheet = wb.active
            sheet.title = "asdfas9df72"
            sheet['A1'] = userId_hash.hexdigest()
            sheet['A2'] = password_hash.hexdigest()

            wb.save('#20$6&7!#04.xlsx')
            #=============================================================================
            window.destroy()
            tkmb.showinfo("Register Success!", "Your register is completed! \n Login with your ID & Password.")


        else:
            tkmb.showerror("Error Code: 001", "Error: Password and Password check is not matching!")

    #register form design
    standardLabel.stdLabel(window,85, 50, 10, 1, "#000","#fff", "맑은 고딕", 30, "Register", "bold")
    standardLabel.stdLabel(window, 130, 150, 10, 1, "#000","#fff", "맑은 고딕", 10, "User Name" )
    standardLabel.stdLabel(window, 125, 200, 10, 1, "#000","#fff", "맑은 고딕", 10, "Password")
    standardLabel.stdLabel(window, 128, 250, 15, 1, "#000","#fff", "맑은 고딕", 10, "Password Check")
    standardLabel.stdLabel(window, 500, 280, 15, 1, "#000","#fff", "맑은 고딕", 8, "©2022 Gloomn")
    standardEntry.stdEntry(window, 130, 170, 20,1,"#a2a4a6", "#000", "#fff", "맑은 고딕", "10", "User ID", user_id, '')
    standardEntry.stdEntry(window, 130, 220, 20,1,"#a2a4a6", "#000", "#fff", "맑은 고딕", "10", "Password", password, '')
    standardEntry.stdEntry(window, 130, 270, 20,1,"#a2a4a6", "#000", "#fff", "맑은 고딕", "10", "Password Check", password_check, '')
    standardButton.fltButton(window,130,300,20, 2,register, "Register", "#ffcc66", "#141414")
    window.bind('<Return>', lambda event: register())

    window.iconbitmap('resources/mainIcon_Black.ico')
    window.mainloop()
# © 2022 Lee-Ki-Joon(Gloomn) <ithan0704@naver.com>
from tkinter import *

def fltButton(x, y, width, height, command,  text = "standardButton", backGroundColor = "#4287f5", foreGroundColor = "#000", cursor = "hand2"):
    def on_enter(e):
        flatButton['background']=backGroundColor
        flatButton['foreground']=foreGroundColor

    def on_leave(e):
        flatButton['background']=foreGroundColor
        flatButton['foreground']=backGroundColor

    flatButton = Button(width=width, height=height, text=text,
                        fg=backGroundColor,
                        bg=foreGroundColor,
                        border=0,
                        activeforeground=foreGroundColor,
                        activebackground=backGroundColor,
                        command=command,
                        relief=SUNKEN,
                        cursor=cursor)
    flatButton.bind("<Enter>", on_enter)
    flatButton.bind("<Leave>", on_leave)

    flatButton.place(x=x, y=y)


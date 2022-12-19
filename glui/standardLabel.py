# © 2022 Lee-Ki-Joon(Gloomn) <ithan0704@naver.com>
from tkinter import *
def stdLabel(target, x, y, width, height, foreGroundColor = "#000", backGroundColor = "#fff", fontFamily = "맑은 고딕", fontSize = 10, text = "standardLabel", weight="normal", slant="roman"):


    standardLabel = Label(master=target,
                          width = width,
                          height=height,
                          fg=foreGroundColor,
                          bg=backGroundColor,
                          text=text,
                          font=(fontFamily, fontSize, slant, weight),
                          relief=SOLID,
                        border=0)

    standardLabel.place(x=x, y=y)


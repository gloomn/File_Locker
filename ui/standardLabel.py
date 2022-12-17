# © 2022 Lee-Ki-Joon(Gloomn) <ithan0704@naver.com>
from tkinter import *

def stdLabel(x, y, width, height, foreGroundColor, backGroundColor, fontFamily, fontSize, text):


    standardLabel = Label(width = width,
                          height=height,
                          fg=foreGroundColor,
                          bg=backGroundColor,
                          text=text,
                          font=(fontFamily, fontSize),
                          relief="solid",
                        border=0)

    standardLabel.place(x=x, y=y)


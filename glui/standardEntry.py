# © 2022 Lee-Ki-Joon(Gloomn) <ithan0704@naver.com>
from tkinter import *

def stdEntry(x, y, width, borderWidth, borderBackground, foreGroundColor, backGroundColor, fontFamily, fontSize, text, textVariable, show):


    standardEntry = Entry(width = width,
                          fg=foreGroundColor,
                          bg=backGroundColor,
                          text=text,
                          font=(fontFamily, fontSize),
                          relief=GROOVE,
                          textvariable=textVariable,
                          borderwidth=0,
                          highlightbackground=borderBackground,
                          highlightthickness=borderWidth,
                          show=show)

    standardEntry.place(x=x, y=y)
"""
Projekt rulett
tkinteri abil lihtsustatud ruleti simulatsioon
"""

import tkinter as tk
from tkinter import ttk
from tkinter.font import Font
##
####ruletinupu_font =  tk.font(family='Helvetica', size=12, weight='bold')
##
##myFont = Font(family="Times New Roman", size=12)

def arvuta_panused():

    panusestring = ""

    for p in panuste_sonastik:
        panusestring += str(lauanupud[p]) + " Panus:" + str(panuste_sonastik[p]) + "\n"
    return panusestring

    
def vasak_hiireklahv(event, nupp, nupu_kirje):
    nupp.config(fg='blue')
    panuste_sonastik[nupp] = panuste_sonastik.get(nupp, 0) + bet
    panused.set(arvuta_panused())
    print(panuste_sonastik.get(nupp, "Tühi"))
    
def parem_hiireklahv(event, nupp, nupu_kirje):
    nupp.config(fg='red')
    panuste_sonastik[nupp] = panuste_sonastik.get(nupp, 0) - bet
    if panuste_sonastik.get(nupp, 0)  <= 0:
        panuste_sonastik.pop(nupp, None)
    panused.set(arvuta_panused())
    print(panuste_sonastik.get(nupp, "Tühi"))


def lauanupp(frame, text, col=0, row=0, rowspan=1):

    if text in ("1","3","5","7","9","12","14","16","18","19","21","23","25","27","30","32","34","36"):
        bg = "red"
    elif text in ("2","4","6","8","10","11","13","15","17","20","22","24","26","28","29","31","33","35"):
        bg = "black"
    else:
        bg = "light grey"
    nupp = tk.Button(frame, text=text)
    lauanupud[nupp] = "Nupp" + text
    nupp.bind('<Button-1>', lambda event, obj=nupp: vasak_hiireklahv(event, nupp, lauanupud[nupp]))
    nupp.bind('<Button-3>', lambda event, obj=nupp: parem_hiireklahv(event, nupp, lauanupud[nupp]))    
    nupp.grid(column=col, row=row, rowspan=rowspan)
    nupp.config(width=4, height=5, font=("Times New Roman", 13, "bold"), fg="white", bg=bg)

    return nupp

  
root = tk.Tk()

root.title("Rulett")
root.geometry('1000x600')
tabloo = ttk.Frame(root)
ruletilaud = ttk.Frame(root)
panuseinfo = ttk.Frame(root)
panusenupud = ttk.Frame(root)
animatsioon = ttk.Frame(root)

animatsioon.grid(column=0, row=0)
tabloo.grid(column=0, row=1)
ruletilaud.grid(column=1, row=2)
panuseinfo.grid(column=2, row=1, rowspan=5)


panused = tk.StringVar()
show_bets = tk.Label(panuseinfo, textvariable=panused)
show_bets.grid(column=0, row=0, sticky='e', padx=20)
show_bets.config(height=20)
scrollb = ttk.Scrollbar(panuseinfo, orient='vertical')
scrollb.grid(row=0, column=1, sticky='e', padx=20)



panusenupud.grid(column=1, row=3)
panusenupp = tk.Button(panusenupud, text="Mängi")  
panusenupp.grid(column=0, row=0, rowspan=1, pady=20)
panusenupp.config(width=10, height=2)

tablooinfo = ttk.Label(tabloo, text='Tablooinfo')
tablooinfo.grid(column=0, row=0)

bet = 1
panuste_sonastik = dict()
lauanupud = dict()


# Ruletilaua nupud
nupp_0_frame = ttk.Frame(ruletilaud)
nupp_0_frame.grid(column=0, row=0)
nupp_0 = lauanupp(nupp_0_frame, text="0", col=0, row=0, rowspan=3)
##nupp_0.grid(column=0, row=0, rowspan=3)
nupp_0.config(height=16, width=5)

nupp_1_36_frame = ttk.Frame(ruletilaud)
nupp_1_36_frame.grid(column=1, row=0)

nupp_1 = lauanupp(nupp_1_36_frame, text="1", col=0, row=0)
nupp_2 = lauanupp(nupp_1_36_frame, text="2", col=0, row=1)
nupp_3 = lauanupp(nupp_1_36_frame, text="3", col=0, row=2)
nupp_4 = lauanupp(nupp_1_36_frame, text="4", col=1, row=0)
nupp_5 = lauanupp(nupp_1_36_frame, text="5", col=1, row=1)
nupp_6 = lauanupp(nupp_1_36_frame, text="6", col=1, row=2)
nupp_7 = lauanupp(nupp_1_36_frame, text="7", col=2, row=0)
nupp_8 = lauanupp(nupp_1_36_frame, text="8", col=2, row=1)
nupp_9 = lauanupp(nupp_1_36_frame, text="9", col=2, row=2)
nupp_10 = lauanupp(nupp_1_36_frame, text="10", col=3, row=0)
nupp_11 = lauanupp(nupp_1_36_frame, text="11", col=3, row=1)
nupp_12 = lauanupp(nupp_1_36_frame, text="12", col=3, row=2)
nupp_13 = lauanupp(nupp_1_36_frame, text="13", col=4, row=0)
nupp_14 = lauanupp(nupp_1_36_frame, text="14", col=4, row=1)
nupp_15 = lauanupp(nupp_1_36_frame, text="15", col=4, row=2)
nupp_16 = lauanupp(nupp_1_36_frame, text="16", col=5, row=0)
nupp_17 = lauanupp(nupp_1_36_frame, text="17", col=5, row=1)
nupp_18 = lauanupp(nupp_1_36_frame, text="18", col=5, row=2)
nupp_19 = lauanupp(nupp_1_36_frame, text="19", col=6, row=0)
nupp_20 = lauanupp(nupp_1_36_frame, text="20", col=6, row=1)
nupp_21 = lauanupp(nupp_1_36_frame, text="21", col=6, row=2)
nupp_22 = lauanupp(nupp_1_36_frame, text="22", col=7, row=0)
nupp_23 = lauanupp(nupp_1_36_frame, text="23", col=7, row=1)
nupp_24 = lauanupp(nupp_1_36_frame, text="24", col=7, row=2)
nupp_25 = lauanupp(nupp_1_36_frame, text="25", col=8, row=0)
nupp_26 = lauanupp(nupp_1_36_frame, text="26", col=8, row=1)
nupp_27 = lauanupp(nupp_1_36_frame, text="27", col=8, row=2)
nupp_28 = lauanupp(nupp_1_36_frame, text="28", col=9, row=0)
nupp_29 = lauanupp(nupp_1_36_frame, text="29", col=9, row=1)
nupp_30 = lauanupp(nupp_1_36_frame, text="30", col=9, row=2)
nupp_31 = lauanupp(nupp_1_36_frame, text="31", col=10, row=0)
nupp_32 = lauanupp(nupp_1_36_frame, text="32", col=10, row=1)
nupp_33 = lauanupp(nupp_1_36_frame, text="33", col=10, row=2)
nupp_34 = lauanupp(nupp_1_36_frame, text="34", col=11, row=0)
nupp_35 = lauanupp(nupp_1_36_frame, text="35", col=11, row=1)
nupp_36 = lauanupp(nupp_1_36_frame, text="36", col=11, row=2)
nupp_2to1_1 = lauanupp(nupp_1_36_frame, text="2:1", col=12, row=0)
nupp_2to1_2 = lauanupp(nupp_1_36_frame, text="2:1", col=12, row=1)
nupp_2to1_3 = lauanupp(nupp_1_36_frame, text="2:1", col=12, row=2)






root.mainloop()



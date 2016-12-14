"""
Projekt rulett
tkinteri abil lihtsustatud ruleti simulatsioon
"""
from random import randint
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

    
def vasak_hiireklahv(nupp, nupu_kirje):
    current_balance -= bet
    panuste_sonastik[nupp] = panuste_sonastik.get(nupp, 0) + bet
    panused.set(arvuta_panused())
    print(panuste_sonastik.get(nupp, "Tühi"))
    
def parem_hiireklahv(nupp, nupu_kirje):
    current_balance += bet
    panuste_sonastik[nupp] = panuste_sonastik.get(nupp, 0) - bet
    if panuste_sonastik.get(nupp, 0)  <= 0:
        panuste_sonastik.pop(nupp, None)
    panused.set(arvuta_panused())
    print(panuste_sonastik.get(nupp, "Tühi"))


def lauanupp(frame, text, col=0, row=0, rowspan=1, colspan=1):

    nupp = tk.Button(frame, text=text)
    lauanupud[nupp] = "Nupp" + text
    nupp.bind('<Button-1>', lambda event, obj=nupp: vasak_hiireklahv(nupp, lauanupud[nupp]))
    nupp.bind('<Button-3>', lambda event, obj=nupp: parem_hiireklahv(nupp, lauanupud[nupp]))    
    nupp.grid(column=col, row=row, rowspan=rowspan, columnspan=colspan)
    if text in ("1","3","5","7","9","12","14","16","18","19","21","23","25","27","30","32","34","36", "Punane"):
        bg = "red"
    elif text in ("2","4","6","8","10","11","13","15","17","20","22","24","26","28","29","31","33","35", "Must"):
        bg = "black"
    else:
        bg = "green"
    nupp.config(width=4, height=5, font=("Times New Roman", 13, "bold"), fg="white", bg=bg)

    return nupp


def gameround():
    """ Vaata panused üle, arvuta"""
    print("Mängu alga", panuste_sonastik)
    result = randint(0, 36)
    print("Tulemus", result)


def create_window():
    abiinfo = tk.Toplevel(root)
    abiinfo.title("Mängujuhend")
    txt = tk.Text(abiinfo)
    txt.grid(column=0, row=0)
    txt.insert(insert, abitekst)

abitekst = """•Panuse tegemiseks klõpsake ruletilaua panustamisalale. \n
            •Mängimiseks klõpsake nupule "Mängi"."""



root = tk.Tk()

root.title("Rulett")
root.geometry('1000x600')
tabloo = ttk.Frame(root)
ruletilaud = ttk.Frame(root)
panuseinfo = ttk.Frame(root)
panusenupud = ttk.Frame(root)
animatsioon = ttk.Frame(root)
saldoframe = ttk.Frame(root)

tabloo.grid(column=1, row=0, sticky="new")
animatsioon.grid(column=0, row=1)
saldoframe.grid(column=0, row=2, sticky="s")
ruletilaud.grid(column=1, row=2)
panuseinfo.grid(column=2, row=1, rowspan=5)


balanss = tk.StringVar()
balanss.set(1000)
txt_saldo = tk.Label(saldoframe, text="Saldo", font=("Times New Roman", 14, "bold"))
txt_saldo.grid(column=0, row=0, sticky="s")
saldo = tk.Label(saldoframe, textvariable=balanss, font=("Times New Roman", 13, "bold"))
saldo.grid(column=0, row=1)

louend = tk.Canvas(panuseinfo)
louend.grid(row=0, column=0, sticky="nesw")

panused = tk.StringVar()
show_bets = tk.Label(louend, textvariable=panused)
show_bets.grid(column=0, row=0, padx=20)
show_bets.config(height=20)
##scrollb = tk.Scrollbar(show_bets, orient='vertical', command=show_bets.yview)
##scrollb.grid(row=0, column=2, sticky='e', padx=20)



panusenupud.grid(column=1, row=3)
panusenupp = tk.Button(panusenupud, text="Mängi")  
panusenupp.grid(column=0, row=0, rowspan=1, pady=20)
panusenupp.config(width=10, height=2)
panusenupp.bind('<Button-1>', lambda event, obj=panusenupp: gameround())



tablooinfo = ttk.Label(tabloo, text='Tablooinfo')
tablooinfo.grid(column=1, row=0, columnspan=10)

abinupp = tk.Button(tabloo, text="Mängujuhend")  
abinupp.grid(column=0, row=0)
abinupp.bind('<Button-1>', lambda event, obj=abinupp: create_window())

animatsioon = ttk.Label(animatsioon, text='Kujuteldav\nanimatsioon')
animatsioon.grid(column=0, row=0, rowspan=10)
animatsioon.config(width=20)

start_balance = 1000
current_balance = start_balance
bet = 1
panuste_sonastik = dict()
lauanupud = dict()


# Ruletilaua nupud
lauanupud_frame = ttk.Frame(ruletilaud)
lauanupud_frame.grid(column=1, row=0)

nupp_0 = lauanupp(lauanupud_frame, text="0", col=0, row=0, rowspan=3)
nupp_0.config(height=16, width=5)

nupp_1 = lauanupp(lauanupud_frame, text="1", col=1, row=0)
nupp_2 = lauanupp(lauanupud_frame, text="2", col=1, row=1)
nupp_3 = lauanupp(lauanupud_frame, text="3", col=1, row=2)
nupp_4 = lauanupp(lauanupud_frame, text="4", col=2, row=0)
nupp_5 = lauanupp(lauanupud_frame, text="5", col=2, row=1)
nupp_6 = lauanupp(lauanupud_frame, text="6", col=2, row=2)
nupp_7 = lauanupp(lauanupud_frame, text="7", col=3, row=0)
nupp_8 = lauanupp(lauanupud_frame, text="8", col=3, row=1)
nupp_9 = lauanupp(lauanupud_frame, text="9", col=3, row=2)
nupp_10 = lauanupp(lauanupud_frame, text="10", col=4, row=0)
nupp_11 = lauanupp(lauanupud_frame, text="11", col=4, row=1)
nupp_12 = lauanupp(lauanupud_frame, text="12", col=4, row=2)
nupp_13 = lauanupp(lauanupud_frame, text="13", col=5, row=0)
nupp_14 = lauanupp(lauanupud_frame, text="14", col=5, row=1)
nupp_15 = lauanupp(lauanupud_frame, text="15", col=5, row=2)
nupp_16 = lauanupp(lauanupud_frame, text="16", col=6, row=0)
nupp_17 = lauanupp(lauanupud_frame, text="17", col=6, row=1)
nupp_18 = lauanupp(lauanupud_frame, text="18", col=6, row=2)
nupp_19 = lauanupp(lauanupud_frame, text="19", col=7, row=0)
nupp_20 = lauanupp(lauanupud_frame, text="20", col=7, row=1)
nupp_21 = lauanupp(lauanupud_frame, text="21", col=7, row=2)
nupp_22 = lauanupp(lauanupud_frame, text="22", col=8, row=0)
nupp_23 = lauanupp(lauanupud_frame, text="23", col=8, row=1)
nupp_24 = lauanupp(lauanupud_frame, text="24", col=8, row=2)
nupp_25 = lauanupp(lauanupud_frame, text="25", col=9, row=0)
nupp_26 = lauanupp(lauanupud_frame, text="26", col=9, row=1)
nupp_27 = lauanupp(lauanupud_frame, text="27", col=9, row=2)
nupp_28 = lauanupp(lauanupud_frame, text="28", col=10, row=0)
nupp_29 = lauanupp(lauanupud_frame, text="29", col=10, row=1)
nupp_30 = lauanupp(lauanupud_frame, text="30", col=10, row=2)
nupp_31 = lauanupp(lauanupud_frame, text="31", col=11, row=0)
nupp_32 = lauanupp(lauanupud_frame, text="32", col=11, row=1)
nupp_33 = lauanupp(lauanupud_frame, text="33", col=11, row=2)
nupp_34 = lauanupp(lauanupud_frame, text="34", col=12, row=0)
nupp_35 = lauanupp(lauanupud_frame, text="35", col=12, row=1)
nupp_36 = lauanupp(lauanupud_frame, text="36", col=12, row=2)
nupp_2to1_1 = lauanupp(lauanupud_frame, text="2:1", col=13, row=0)
nupp_2to1_2 = lauanupp(lauanupud_frame, text="2:1", col=13, row=1)
nupp_2to1_3 = lauanupp(lauanupud_frame, text="2:1", col=13, row=2)

nupp_1_12 = lauanupp(lauanupud_frame, text="1. 12", col=1, row=3, colspan=4)
nupp_2_12 = lauanupp(lauanupud_frame, text="2. 12", col=5, row=3, colspan=4)
nupp_3_12 = lauanupp(lauanupud_frame, text="3. 12", col=9, row=3, colspan=4)
nupp_1_12.config(width=19, height=1)
nupp_2_12.config(width=19, height=1)
nupp_3_12.config(width=19, height=1)

nupp_1_18 = lauanupp(lauanupud_frame, text="1 kuni 18", col=1, row=4, colspan=2)
nupp_even = lauanupp(lauanupud_frame, text="Paaris", col=3, row=4, colspan=2)
nupp_black = lauanupp(lauanupud_frame, text="Must", col=5, row=4, colspan=2)
nupp_red = lauanupp(lauanupud_frame, text="Punane", col=7, row=4, colspan=2)
nupp_odd = lauanupp(lauanupud_frame, text="Paaritu", col=9, row=4, colspan=2)
nupp_19_36 = lauanupp(lauanupud_frame, text="19 kuni 36", col=11, row=4, colspan=2)
nupp_1_18.config(width=9, height=1)
nupp_even.config(width=9, height=1)
nupp_black.config(width=9, height=1)
nupp_red.config(width=9, height=1)
nupp_odd.config(width=9, height=1)
nupp_19_36.config(width=9, height=1)




root.mainloop()



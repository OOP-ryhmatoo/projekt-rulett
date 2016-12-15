"""
Projekt rulett
tkinteri abil lihtsustatud ruleti simulatsioon
"""

from random import randint
import tkinter as tk
from tkinter import ttk
from tkinter.font import Font
from tkinter import scrolledtext


def arvuta_panused():

    panusestring = ""

    for p in panuste_sonastik:
        panuseala = lauanupud[p][0].replace("\n", " ")
        panusestring += "Väli: " + panuseala + ", Panus: " + str(panuste_sonastik[p])  + "€\n"
    return panusestring

    
def vasak_hiireklahv(nupp):
    
    balanss.set(balanss.get() - bet)
    panuste_sonastik[nupp] = panuste_sonastik.get(nupp, 0) + bet
    show_bets.delete(1.0, "end")
    show_bets.insert("end", arvuta_panused())
    
    
def parem_hiireklahv(nupp):
    
    balanss.set(balanss.get() + bet)
    panuste_sonastik[nupp] = panuste_sonastik.get(nupp, 0) - bet
    if panuste_sonastik.get(nupp, 0)  <= 0:
        panuste_sonastik.pop(nupp, None)
    show_bets.delete(1.0, "end")
    show_bets.insert("end", arvuta_panused())


def lauanupp(frame, text, col=0, row=0, rowspan=1, colspan=1):

    nupp = tk.Button(frame, text=text)
    nupp.bind('<Button-1>', lambda event, obj=nupp: vasak_hiireklahv(nupp))
    nupp.bind('<Button-3>', lambda event, obj=nupp: parem_hiireklahv(nupp))
    nupp.bind("<Enter>", lambda event, obj=nupp: event.widget.config(fg="yellow"))
    nupp.bind("<Leave>", lambda event, obj=nupp: event.widget.config(fg="white"))
    nupp.grid(column=col, row=row, rowspan=rowspan, columnspan=colspan)
    
    if text in punased:
        bg = "red"
    elif text in mustad:
        bg = "black"
    else:
        bg = "green"
        
    nupp.config(width=4, height=3, font=("Times New Roman", 13, "bold"), fg="white", bg=bg)

    if text in ("1 kuni 18", "19 kuni 36", "Paaris", "Paaritu", "Punane", "Must"):
        payout = 1
    elif text in ("1. 12", "2. 12", "3. 12", "1.\nveerg", "2.\nveerg", "3.\nveerg"):
        payout = 2
    else:
        payout = 35
        
    lauanupud[nupp] = (text, payout)

    return nupp



def gameround():
    """  """
    
    # Kui panuseid pole, siis pole midagi võita ka
    if not panuste_sonastik:
        return
    
    win = 0
    result = randint(0, 36)
    result_str =  str(result)  
    
    for k in panuste_sonastik:
        bet_amount = panuste_sonastik[k]
        btn, pay = lauanupud[k]
        # Võit numbriga
        if result_str == btn:
##            print("Võitis numbriga")
            win += panuste_sonastik[k] * pay
        # Võit punase/mustaga
        if result_str in punased and btn == "Punane":
            win += panuste_sonastik[k] * pay
##            print("punane võitis")
        if result_str in mustad and btn == "Must":
            win += panuste_sonastik[k] * pay
##            print("must võitis")
        # Võit 1-18/9-36
        if result_str in pool_1 and btn == "1 kuni 18":
            win += panuste_sonastik[k] * pay
##            print("1 kuni 18 võitis")
        if result_str in pool_2 and btn == "19 kuni 36":
            win += panuste_sonastik[k] * pay
##            print("19 kuni 36 võitis")
        # Võit paaris/paaritu
        if result_str in paaris and btn == "Paaris":
            win += panuste_sonastik[k] * pay
##            print("punane võitis")
        if result_str in paaritu and btn == "Paaritu":
            win += panuste_sonastik[k] * pay            
        # Võit veeruga
        if result_str in veerg_1 and btn == "1.\nveerg":
            win += panuste_sonastik[k] * pay
##            print("1 veerg võitis")
        if result_str in veerg_2 and btn == "2.\nveerg":
            win += panuste_sonastik[k] * pay
##            print("2 veerg võitis")
        if result_str in veerg_3 and btn == "3.\nveerg":
            win += panuste_sonastik[k] * pay
##            print("3 veerg võitis")
        # Võit kolmandikuga
        if result_str in kolmandik_1 and btn == "1. 12":
            win += panuste_sonastik[k] * pay
##            print("1 kolmandik võitis")
        if result_str in kolmandik_2 and btn == "2. 12":
            win += panuste_sonastik[k] * pay
##            print("2 kolmandik võitis")
        if result_str in kolmandik_3 and btn == "3. 12":
            win += panuste_sonastik[k] * pay
##            print("3 kolmandik võitis")

    balanss.set(balanss.get() + win)
    # Eemalda panused mänguringi järel
    panuste_sonastik.clear()
    panused.set(arvuta_panused())
    show_bets.delete(1.0, "end")

    if win:
        win_msg.set("Võit: " + str(win) + " €")
    else:        
        win_msg.set("Proovi uuesti\nTee oma panused")


def create_window():
    """ Mängujuhend uues aknas """
    abiinfo = tk.Toplevel(root)
    abiinfo.title("Mängujuhend")
    txt = tk.Text(abiinfo, wrap="word")
    txt.grid(column=0, row=0)
    abitekst = """•Panuse tegemiseks tehke vasaku hiireklahviga klõps ruletilaua panustamisalale.
•Panuse eemaldamiseks tehke vasaku hiireklahviga klõps ruletilaua panustamisalale.
•Mängimiseks klõpsake nupule "Mängi".
•Sinu panuste väljal näed oma hetke panuseid

Reeglid:
----------------------------------------------------------------------------
Panuse Nimi:    Võitvad Numbrid: 	           Väljamakse:
Number 	        0 kuni 36                     €1 : €35
Kolmik 	        Suvaline kolmik
  	        (1, 4, 7, 10 jne)             €1 : €2
Tosin 	        Suvaline sektor laualt
 	        (12 järjestikust numbrit)     €1 : €2
Paaritu	        Suvaline paaritu number 	     €1 : €1
Paaris 	        Suvaline paarisnumber         €1 : €1
Must värv       Suvaline musta värvi number   €1 : €1
Punane Värv	    Suvaline punast värvi number 	€1 : €1
Pool lauda 	    Numbrid 1-18 või 19-36        €1 : €1
"""
    txt.insert("insert", abitekst)
    sulgemisnupp = tk.Button(abiinfo, text="Sulge", font=("Times New Roman", 13, "bold"), command=abiinfo.destroy)
    sulgemisnupp.grid(column=0, row=1)



punased = ("1","3","5","7","9","12","14","16","18","19","21","23","25","27","30","32","34","36", "Punane")
mustad = ("2","4","6","8","10","11","13","15","17","20","22","24","26","28","29","31","33","35", "Must")
veerg_1 = ("1","4","7","10","13","16","19","22","25","28","31","34")
veerg_2 = ("2","5","8","11","14","17","20","23","26","29","32","35")
veerg_3 = ("3","6","9","12","15","18","21","24","27","30","33","36")
kolmandik_1 = ("1","2","3","4","5","6","7","8","9","10","11","12")
kolmandik_2 = ("13","14","15","16","17","18","19","20","21","22","23","24")
kolmandik_3 = ("25","26","27","28","29","30","31","32","33","34","35","36")
pool_1 = ("1","2","3","4","5","6","7","8","9","10","11","12", "13","14","15","16","17","18")
pool_2 = ("19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36")
paaris = ("2","4","6","8","10","12","14","16","18","20","22","24","26","28","30","32","34","36")
paaritu = ("1","3","5","7","9","11","13","15","17","19","21","23","25","27","29","31","33","35")

start_balance = 1000
bet = 1
panuste_sonastik = dict()
lauanupud = dict()

root = tk.Tk()
root.resizable(0,0)
root.title("Rulett")
root.geometry('1110x500')
# Kõik need freimid
abinupp = ttk.Frame(root)
tabloo = ttk.Frame(root)
ruletilaud = ttk.Frame(root)
panuseinfo = ttk.Frame(root)
panusenupud = ttk.Frame(root)
animatsioon = ttk.Frame(root)
saldoframe = ttk.Frame(root)

#Help nupp
abinupp.grid(column=0, row=0)
tabloo.grid(column=1, row=0, columnspan=1, pady= 9)
animatsioon.grid(column=0, row=1)
saldoframe.grid(column=0, row=2, sticky="s")
ruletilaud.grid(column=1, row=2, pady=35)
panuseinfo.grid(column=2, row=0, rowspan=5)

# Saldoinfo
balanss = tk.IntVar()
balanss.set(start_balance)
txt_saldo = tk.Label(saldoframe, text="Saldo", font=("Times New Roman", 14, "bold"))
txt_saldo.grid(column=0, row=0, columnspan=2)
saldo = tk.Label(saldoframe, textvariable=balanss, font=("Times New Roman", 13, "bold"))
saldo.grid(column=0, row=1)
txt_currency = tk.Label(saldoframe, text="€", font=("Times New Roman", 13, "bold"))
txt_currency.grid(column=1, row=1)

# Panuste info
panused = tk.StringVar()
show_bets_header = tk.Label(panuseinfo, text="Sinu panused", font=("Times New Roman", 13, "bold"))
show_bets_header.grid(column=0, row=0)
show_bets = scrolledtext.ScrolledText(panuseinfo, height=20, width = 28)
show_bets.grid(column=0, row=1, padx=10)

# Mängimise nupp
panusenupud.grid(column=1, row=3)
panusenupp = tk.Button(panusenupud, text="Mängi", font=("Times New Roman", 13, "bold"))  
panusenupp.grid(column=0, row=0, rowspan=1, pady=20)
panusenupp.config(width=10, height=2)
panusenupp.bind('<Button-1>', lambda event, obj=panusenupp: gameround())


# Võiduteated
win_msg = tk.StringVar()
win_msg.set("Tee oma panused")
tablooinfo = tk.Label(tabloo, textvariable=win_msg, font=("Times New Roman", 13, "bold"), relief="sunken", width=20, height=2)
tablooinfo.grid(column=0, row=0)

abinupp = tk.Button(abinupp, text="Mängujuhend", font=("Times New Roman", 13, "bold"), relief="ridge", anchor="w")  
abinupp.grid(column=0, row=0)
abinupp.bind('<Button-1>', lambda event, obj=abinupp: create_window())

##animatsioon = ttk.Label(animatsioon, text='Kujuteldav\nanimatsioon')
##animatsioon.grid(column=0, row=1, rowspan=10)
##animatsioon.config(width=20)




# Ruletilaua nupud
lauanupud_frame = ttk.Frame(ruletilaud)
lauanupud_frame.grid(column=1, row=0)

nupp_0 = lauanupp(lauanupud_frame, text="0", col=0, row=0, rowspan=3)
nupp_0.config(height=10, width=5)

# Tegelikult poleks neid muutujaid üldse vaja, kui aega üle jääb(ha-ha), siis võiks tsükliga kokku lükata
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
nupp_2to1_1 = lauanupp(lauanupud_frame, text="1.\nveerg", col=13, row=0)
nupp_2to1_2 = lauanupp(lauanupud_frame, text="2.\nveerg", col=13, row=1)
nupp_2to1_3 = lauanupp(lauanupud_frame, text="3.\nveerg", col=13, row=2)

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



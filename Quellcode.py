import tkinter as tk
import tkinter.ttk as ttk
import math
import turtle
import time
#from PIL import Image, ImageTk

maxDistanz = 0
maxHöhe = 0

def StartEnter(event):
    ausführen()

# =========================================================================================================================================================================
#                                                                       ABSCHNITT DATENÜBERTRAGUNG
# =========================================================================================================================================================================


def push():
    global reseingabeWindrichtung, eingabeWindrichtung
    global reseingabeWindgeschwindigkeit, eingabeWindgeschwindigkeit
    global reseingabeAbwurfgeschwindigkeit, eingabeAbwurfgeschwindigkeit
    global reseingabeAbwurfwinkel, eingabeAbwurfwinkel
    global reseingabeAbwurfrichtung, eingabeAbwurfrichtung
    global reseingabeNeigungEbene, eingabeNeigungEbene
    global Genauigkeit, eingabeGenauigkeit

    try:
        float(eingabeWindrichtung.get())
        reseingabeWindrichtung = float(eingabeWindrichtung.get()) +180
    except ValueError:
        reseingabeWindrichtung = 180

    try:
        float(eingabeWindgeschwindigkeit.get())
        reseingabeWindgeschwindigkeit = float(eingabeWindgeschwindigkeit.get())
    except ValueError:  
        reseingabeWindgeschwindigkeit = 0

    try:
        float(eingabeAbwurfgeschwindigkeit.get())
        reseingabeAbwurfgeschwindigkeit = float(eingabeAbwurfgeschwindigkeit.get())
    except ValueError:
        reseingabeAbwurfgeschwindigkeit = 10

    try:
        float(eingabeAbwurfwinkel.get())
        reseingabeAbwurfwinkel = float(eingabeAbwurfwinkel.get())
    except ValueError:
        reseingabeAbwurfwinkel = 30

    try:
        float(eingabeAbwurfrichtung.get())
        reseingabeAbwurfrichtung = float(eingabeAbwurfrichtung.get())
    except ValueError:
        reseingabeAbwurfrichtung = 0

    try:
        float(eingabeNeigungEbene.get())
        reseingabeNeigungEbene = float(eingabeNeigungEbene.get())
    except ValueError:
        reseingabeNeigungEbene = 0.0

    Genauigkeit = str(eingabeGenauigkeit.get())
    startzeit = time.time()
    PopupFenster = tk.Toplevel(HauptFenster)
    
    PopupFenster.geometry("200x50")
    PopupFenster.resizable(0,0)

    if True:
        PopupFenster.title("Erfolg")
        tk.Label(PopupFenster, text ="Datenübertragung \n erfolgreich",font=('Helvetica', 10)).pack()
    else:
        PopupFenster.title("Fehler")
        tk.Label(PopupFenster, text ="Fehler bei der \n datenübertragung",font=('Helvetica', 10)).pack()

    PopupFenster.after(2000, lambda: PopupFenster.destroy()) # in milisekunden
    

    


# =========================================================================================================================================================================
#                                                                       ABSCHNITT BERECHNUNG
# =========================================================================================================================================================================

def ausführen():
    global pen, pen2, pen6, pen7
    global reseingabeWindrichtung
    global reseingabeWindgeschwindigkeit
    global reseingabeAbwurfgeschwindigkeit
    global reseingabeAbwurfwinkel
    global reseingabeAbwurfrichtung
    global reseingabeNeigungEbene
    global knopf1
    global ProgrFenster

    knopf1.grid_forget()
    knopf1 = tk.Button(ProgrFenster,width=32, height=1, text="    Berechne...     ", font=('Helvetica bold', 12))
    knopf1.grid(column=2, row=1,columnspan = 2)
    
    pen.clear()
    anfangszeit = time.time()
    
    
    # Wind
    Windgeschwindigkeit = reseingabeWindgeschwindigkeit                 # Windgeschwindigkeit
    Windrichtung = reseingabeWindrichtung                               # Windrichtung
    r = 0.0015                                                          # Radius Wassertropfen

    # Wurf
    Abwurfgeschwindigkeit = reseingabeAbwurfgeschwindigkeit             # Abwurfgeschwindigkeit
    Abwurfwinkel = reseingabeAbwurfwinkel                               # Abwurfwinkel
    Wurfrichtung = reseingabeAbwurfrichtung                             # Abwurfrichtung
    erwuenschteRichtung = Wurfrichtung
    
    # Luft & Wassertropfen
    cwWert = 0.45                                                       # CW-Wert eines Wassertropfens
    PL = 1.293                                                          # Dichte der Luft
    A = 2*math.pi*r**2                                                  # Oberflächeninhalt des Wassertropfens


    Masse = 4/3*math.pi*r**3*997                                        # Masse des Wassertropfens - mit Faktor 10

    # andere
    Gravitation = 9.81                                                  # Gravitationskraft
    NeigungEbene = reseingabeNeigungEbene                               # Neigung der Ebene

    try :
        float(Zieldistanz.get())
        erwuenschteDistanz = float(Zieldistanz.get())

    except ValueError:
        erwuenschteDistanz = 3.00
        

    # effektive Gravitation y-Richtung
    yEffGravitation = Gravitation * math.cos(NeigungEbene * math.pi / 180)
    # effektive Gravitation x-Richtung
    xEffGravitation = Gravitation * math.sin(NeigungEbene * math.pi / 180)

    def vx(Abwurfgeschwindigkeit, Abwurfwinkel):
        vx = Abwurfgeschwindigkeit * math.cos(Abwurfwinkel * math.pi / 180)

        return vx

    # Anfangs-Geschwindigkeit in y-Richtung

    def vy(Abwurfgeschwindigkeit, Abwurfwinkel):
        vy = Abwurfgeschwindigkeit * math.sin(Abwurfwinkel * math.pi / 180)

        return vy

    # Angabe im Koordinatensystem u. Vermeidung von überlappenden Zahlen 
    if erwuenschteDistanz < 1.2 and erwuenschteDistanz > 0.8:
        pen7.clear()
        pen7.pencolor('black')
        pen7.penup()
        pen7.goto(-120,-199)
        pen7.pendown()
        pen7.goto(-120,-195)
        pen7.penup()
        pen7.goto(-40,-199)
        pen7.pendown()
        pen7.goto(-40,-195)
        pen7.penup()
        pen7.goto(40,-199)
        pen7.pendown()
        pen7.goto(40,-195)
        pen7.penup()
        pen7.goto(120,-199)
        pen7.pendown()
        pen7.goto(120,-195)
        pen7.penup()
        pen7.goto(200,-199)
        pen7.pendown()
        pen7.goto(200,-195)
        pen7.penup()
        pen7.goto(280,-199)
        pen7.pendown()
        pen7.goto(280,-195)
        pen7.penup()

    
        pen7.goto(-280,-199)
        pen7.pendown()
        pen7.goto(-280,-195)
        pen7.penup()
        pen7.write('-1m',align = 'center', font=('Courier',10,'normal'))
        pen7.goto(-360,-199)
        pen7.pendown()
        pen7.goto(-360,-195)
        pen7.penup()
    
        pen7.goto(-200,-119)
        pen7.pendown()
        pen7.goto(-196,-119)
        pen7.penup()
        pen7.goto(-185,-127)
        pen7.write('1m',align = 'center', font=('Courier',10,'normal'))
        pen7.goto(-200,-39)
        pen7.pendown()
        pen7.goto(-196,-39)
        pen7.penup()
        pen7.goto(-200,41)
        pen7.pendown()
        pen7.goto(-196,41)
        pen7.penup()
        pen7.goto(-200,121)
        pen7.pendown()
        pen7.goto(-196,121)
        pen7.penup()
            
        pen7.pencolor('red')
        pen7.penup()
        pen7.goto(-200+erwuenschteDistanz*80,-199)
        pen7.pendown()
        pen7.goto(-200+erwuenschteDistanz*80,-195)
        pen7.penup()
        pen7.write('Ziel',align = 'center', font=('Courier',10,'normal'))

    elif erwuenschteDistanz > -1.2 and erwuenschteDistanz < -0.8:
        pen7.clear()
        pen7.pencolor('black')
        pen7.penup()
        pen7.goto(-120,-199)
        pen7.pendown()
        pen7.goto(-120,-195)
        pen7.penup()
        pen7.write('1m',align = 'center', font=('Courier',10,'normal'))
        pen7.goto(-40,-199)
        pen7.pendown()
        pen7.goto(-40,-195)
        pen7.penup()
        pen7.goto(40,-199)
        pen7.pendown()
        pen7.goto(40,-195)
        pen7.penup()
        pen7.goto(120,-199)
        pen7.pendown()
        pen7.goto(120,-195)
        pen7.penup()
        pen7.goto(200,-199)
        pen7.pendown()
        pen7.goto(200,-195)
        pen7.penup()
        pen7.goto(280,-199)
        pen7.pendown()
        pen7.goto(280,-195)
        pen7.penup()

    
        pen7.goto(-280,-199)
        pen7.pendown()
        pen7.goto(-280,-195)
        pen7.penup()
        pen7.goto(-360,-199)
        pen7.pendown()
        pen7.goto(-360,-195)
        pen7.penup()
    
        pen7.goto(-200,-119)
        pen7.pendown()
        pen7.goto(-196,-119)
        pen7.penup()
        pen7.goto(-185,-127)
        pen7.write('1m',align = 'center', font=('Courier',10,'normal'))
        pen7.goto(-200,-39)
        pen7.pendown()
        pen7.goto(-196,-39)
        pen7.penup()
        pen7.goto(-200,41)
        pen7.pendown()
        pen7.goto(-196,41)
        pen7.penup()
        pen7.goto(-200,121)
        pen7.pendown()
        pen7.goto(-196,121)
        pen7.penup()
        
        pen7.pencolor('red')
        pen7.penup()
        pen7.goto(-200+erwuenschteDistanz*80,-199)
        pen7.pendown()
        pen7.goto(-200+erwuenschteDistanz*80,-195)
        pen7.penup()
        pen7.write('Ziel',align = 'center', font=('Courier',10,'normal'))

        
    else:
        pen7.clear()
        pen7.pencolor('black')
        pen7.penup()
        pen7.goto(-120,-199)
        pen7.pendown()
        pen7.goto(-120,-195)
        pen7.penup()
        pen7.write('1m',align = 'center', font=('Courier',10,'normal'))
        pen7.goto(-40,-199)
        pen7.pendown()
        pen7.goto(-40,-195)
        pen7.penup()
        pen7.goto(40,-199)
        pen7.pendown()
        pen7.goto(40,-195)
        pen7.penup()
        pen7.goto(120,-199)
        pen7.pendown()
        pen7.goto(120,-195)
        pen7.penup()
        pen7.goto(200,-199)
        pen7.pendown()
        pen7.goto(200,-195)
        pen7.penup()
        pen7.goto(280,-199)
        pen7.pendown()
        pen7.goto(280,-195)
        pen7.penup()

    
        pen7.goto(-280,-199)
        pen7.pendown()
        pen7.goto(-280,-195)
        pen7.penup()
        pen7.write('-1m',align = 'center', font=('Courier',10,'normal'))
        pen7.goto(-360,-199)
        pen7.pendown()
        pen7.goto(-360,-195)
        pen7.penup()
    
        pen7.goto(-200,-119)
        pen7.pendown()
        pen7.goto(-196,-119)
        pen7.penup()
        pen7.goto(-185,-127)
        pen7.write('1m',align = 'center', font=('Courier',10,'normal'))
        pen7.goto(-200,-39)
        pen7.pendown()
        pen7.goto(-196,-39)
        pen7.penup()
        pen7.goto(-200,41)
        pen7.pendown()
        pen7.goto(-196,41)
        pen7.penup()
        pen7.goto(-200,121)
        pen7.pendown()
        pen7.goto(-196,121)
        pen7.penup()
        
        pen7.pencolor('red')
        pen7.penup()
        pen7.goto(-200+erwuenschteDistanz*80,-199)
        pen7.pendown()
        pen7.goto(-200+erwuenschteDistanz*80,-195)
        pen7.penup()
        pen7.write('Ziel',align = 'center', font=('Courier',10,'normal'))

    def Wurfberechnung(Wurfrichtung, vx, vy, Abwurfwinkel):
        global maxDistanz, maxHöhe, Genauigkeit

        h = 0
        s = 0

        if Genauigkeit == 'präzise':
            ti = 0.0001
        elif Genauigkeit == 'halbpräzise':
            ti = 0.001
        elif Genauigkeit == 'ausgewogen':
            ti = 0.005
        elif Genauigkeit == 'halbschnell':
            ti = 0.01
        elif Genauigkeit == 'schnell':
            ti = 0.1

        while True:

            yFlr = 0.5 * PL * A * cwWert * (vy ** 2)
            if vy >= 0:
                vy = vy - (yFlr / Masse) * ti - yEffGravitation * ti
            else:
                vy = vy + (yFlr / Masse) * ti - yEffGravitation * ti

            h = h + vy * ti - 0.5 * yEffGravitation * ti ** 2

            xFlr = 0.5 * PL * A * cwWert * (vx ** 2)

            if Abwurfwinkel > 90:
                vx = vx + (xFlr / Masse) * ti - 0.5 * xEffGravitation * ti
            else:
                if vx < 0:
                    vx = vx + (xFlr / Masse) * ti - 0.5 * xEffGravitation * ti
                else :
                    vx = vx - (xFlr / Masse) * ti - 0.5 * xEffGravitation * ti



            s = s + (vx) * ti
            
            if h < 0:
                break
        return s

    def WurfberechnungZeichnung( Wurfrichtung, vx, vy, Abwurfwinkel, pencolor):
        global maxDistanz, maxHöhe, Genauigkeit
        pen.penup()
        pen.goto(-200,-200)
        pen.pendown()

        h = 0
        s = 0
        maxHöhe = h

        
        if Genauigkeit == 'präzise':
            ti = 0.0001
        elif Genauigkeit == 'halbpräzise':
            ti = 0.001
        elif Genauigkeit == 'ausgewogen':
            ti = 0.005
        elif Genauigkeit == 'halbschnell':
            ti = 0.01
        elif Genauigkeit == 'schnell':
            ti = 0.1

        while True:

            yFlr = 0.5 * PL * A * cwWert * (vy ** 2)
            if vy >= 0:
                vy = vy - (yFlr / Masse) * ti - yEffGravitation * ti
            else:
                vy = vy + (yFlr / Masse) * ti - yEffGravitation * ti

            h = h + vy * ti - 0.5 * yEffGravitation * ti ** 2

            xFlr = 0.5 * PL * A * cwWert * (vx ** 2)

            if Abwurfwinkel > 90:
                vx = vx + (xFlr / Masse) * ti - 0.5 * xEffGravitation * ti
            else:
                if vx < 0:
                    vx = vx + (xFlr / Masse) * ti - 0.5 * xEffGravitation * ti
                else :
                    vx = vx - (xFlr / Masse) * ti - 0.5 * xEffGravitation * ti



            s = s + (vx) * ti
            pen.pencolor(pencolor)
            pen.goto(s*80 - 200, h*80 - 200)

            if h>maxHöhe:
                maxHöhe = h
            
            if h < 0:
                break

            maxDistanz = s
        return s


    def angepassterWinkel(erwuenschteDistanz, vx):
        Abwurfwinkel = 0
        while Wurfberechnung(Wurfrichtung, vx, vy(Abwurfgeschwindigkeit, Abwurfwinkel),Abwurfwinkel) < erwuenschteDistanz:
            Abwurfwinkel += 0.1
            
            if (Abwurfwinkel >= 45) and (Wurfberechnung(Wurfrichtung, vx, vy(Abwurfgeschwindigkeit, Abwurfwinkel),Abwurfwinkel) < erwuenschteDistanz):
                return False

        return Abwurfwinkel




    def Koordinaten(Wurfrichtung, vx, vy):
       v1 = vx * math.cos(Wurfrichtung * math.pi/180) + Windgeschwindigkeit * math.cos(Windrichtung * math.pi / 180) #Norden
       v2 = vx * math.sin(Wurfrichtung * math.pi/180) + Windgeschwindigkeit * math.sin(Windrichtung * math.pi / 180) #Osten


       s1 = Wurfberechnung(Wurfrichtung, v1, vy, Abwurfwinkel)

       s2 = Wurfberechnung(Wurfrichtung, v2, vy, Abwurfwinkel)#

       sx = ((s1**2) + (s2 ** 2))**(1/2)


       l = [sx, s1, s2]

       return l

    def s2Berechnung(erwuenschteRichtung, vx, vy):
        v2 = vx * math.sin(erwuenschteRichtung * math.pi / 180)
        s2 = Wurfberechnung(erwuenschteRichtung, v2, vy, angepassterWinkel(erwuenschteDistanz, vx))

        return s2

    def erwuenschteKoordinaten(Wurfrichtung):
        Wurfrichtung = 0

        while round((Koordinaten(Wurfrichtung, vx(Abwurfgeschwindigkeit, Abwurfwinkel), vy(Abwurfgeschwindigkeit, Abwurfwinkel))[2]),
                    0) != s2Berechnung(erwuenschteRichtung, vx(Abwurfgeschwindigkeit, Abwurfwinkel), vy(Abwurfgeschwindigkeit, Abwurfwinkel)):
            if Windrichtung > 360:
                Wurfrichtung -= 1
            elif Windrichtung >= 180:
                Wurfrichtung += 1

        if Windrichtung > 360:
            return (Wurfrichtung + 360)
        elif Windrichtung >= 180:
            return Wurfrichtung

    # ==== Ausgabe Flugparabel ====

    vxWurf = vx(Abwurfgeschwindigkeit, Abwurfwinkel) + math.cos((Windrichtung - Wurfrichtung) * math.pi / 180) * Windgeschwindigkeit

    
    pencolor = "black"
    WurfberechnungZeichnung( Wurfrichtung, vxWurf, vy(Abwurfgeschwindigkeit, Abwurfwinkel), Abwurfwinkel, pencolor)
    pen6.clear()
    pen6.penup()
    pen6.goto(0,0)
    pen6.pendown()

    pen6.goto(Koordinaten(Wurfrichtung, vx(Abwurfgeschwindigkeit, Abwurfwinkel), vy(Abwurfgeschwindigkeit,Abwurfwinkel))[2]*10,Koordinaten(Wurfrichtung, vx(Abwurfgeschwindigkeit, Abwurfwinkel), vy(Abwurfgeschwindigkeit, Abwurfwinkel))[1]*10)

    


    winkelNeu = angepassterWinkel(erwuenschteDistanz, vxWurf)

    # ==== Ausgabe von maximaler Höhe/Distanz ====

    pen2.clear()
    pen2.color('black')
    pen2.goto(200,180)
    pen2.write('maximale Distanz: {}m  '.format(round(maxDistanz, 3) ), align = 'left', font=('Courier',10,'normal'))
    pen2.goto(200,165)
    pen2.write('maximale Höhe: {}m  '.format(round(maxHöhe, 3)), align = 'left', font=('Courier',10,'normal'))
    pen2.color('red')
    pen2.goto(200,150)
    if winkelNeu != 0:
        pen2.write('Angepasster Winkel: {}° '.format(round(winkelNeu,3)), align = 'left', font=('Courier',10,'normal'))
    else:
        pen2.write('Zieldistanz nicht erreichbar.',align = 'left', font=('Courier',8,'normal'))
    
    
    # ==== Angepasste Flugparabel ====
   
    
    
    pencolor = "red"

    WurfberechnungZeichnung(Wurfrichtung, vxWurf, vy(Abwurfgeschwindigkeit, winkelNeu), winkelNeu, pencolor)




    pen6.pencolor(pencolor)
    pen6.penup()
    pen6.goto(0,0)
    pen6.pendown()
    pen6.goto(Koordinaten(erwuenschteKoordinaten(Wurfrichtung), vx(Abwurfgeschwindigkeit, winkelNeu), vy(Abwurfgeschwindigkeit, winkelNeu))[2]*10,Koordinaten(erwuenschteKoordinaten(Wurfrichtung), vx(Abwurfgeschwindigkeit, winkelNeu), vy(Abwurfgeschwindigkeit, winkelNeu))[1]*10)
    pen6.pencolor('black')
    pen2.pencolor('black')
    pen2.goto(200,135)
    pen2.write('Berechnungszeit: {}s  '.format(round(time.time()-anfangszeit,3)), align = 'left', font=('Courier',10,'normal'))


    knopf1.grid_forget()
    knopf1 = tk.Button(ProgrFenster,width=32, height=1, text="Wurfparabel Zeichen", font=('Helvetica bold', 12), command=ausführen)
    knopf1.grid(column=2, row=1,columnspan = 2)
    
    







# =========================================================================================================================================================================
#                                                                           ABSCHNITT EINSTELLUNGEN
# =========================================================================================================================================================================

def Einstellungen(): 
    global eingabeWindrichtung
    global eingabeWindgeschwindigkeit
    global eingabeAbwurfgeschwindigkeit
    global eingabeAbwurfwinkel
    global eingabeAbwurfrichtung
    global eingabeGenauigkeit
    global eingabeNeigungEbene
    
    EinstFenster = tk.Toplevel(HauptFenster)
    EinstFenster.title("Einstellungen")
    EinstFenster.geometry("900x400")
    EinstFenster.resizable(0,0)
    EinstFenster.columnconfigure(0, weight=1)
    EinstFenster.columnconfigure(1, weight=5)
    EinstFenster.columnconfigure(2, weight=5)
    EinstFenster.columnconfigure(3, weight=1)

    tk.Label(EinstFenster, text =" Einstellungen \n",font=('Helvetica bold', 14)).grid(column=0, row=0,padx=5, pady=5, columnspan=4)
    tk.Label(EinstFenster, text ="Leere Felder entsprechen Standardwerten. Bei schneller Berechnung kann es zu signifikanten Abweichungen vom Zielergebniss kommen. \n",font=('Helvetica bold', 10)).grid(column=0, row=1,padx=5, pady=5, columnspan=4)

    tk.Label(EinstFenster, text="Windrichtung in Grad -- Norden [0], Osten[90], Süden[180], Westen[270] --",font=('helvetica', 10)).grid(column=1, row=2, sticky=tk.W, padx=5, pady=5)
    eingabeWindrichtung =  tk.Entry(EinstFenster,width=25)
    eingabeWindrichtung.grid(column=2, row=2, padx=5, pady=5)
    
    tk.Label(EinstFenster, text="Windgeschwindigkeit in m/s",font=('helvetica', 10)).grid(column=1, row=3, sticky=tk.W, padx=5, pady=5)
    eingabeWindgeschwindigkeit =  tk.Entry(EinstFenster,width=25)
    eingabeWindgeschwindigkeit.grid(column=2, row=3, padx=5, pady=5)

    tk.Label(EinstFenster, text="Genauigkeit",font=('helvetica', 10)).grid(column=1, row=4, sticky=tk.W, padx=5, pady=5)
    optionengenauigkeit = ['präzise','halbpräzise','ausgewogen','halbschnell','schnell'] 
    eingabeGenauigkeit = tk.StringVar(EinstFenster)
    eingabeGenauigkeit.set(optionengenauigkeit[2]) 
    dropdown = tk.OptionMenu(EinstFenster, eingabeGenauigkeit, *optionengenauigkeit)
    dropdown.grid(column=2, row=4, padx=5, pady=5)

    tk.Label(EinstFenster, text=" Abwurfgeschwindigkeit in m/s",font=('helvetica', 10)).grid(column=1, row=5, sticky=tk.W, padx=5, pady=5)
    eingabeAbwurfgeschwindigkeit =  tk.Entry(EinstFenster,width=25)
    eingabeAbwurfgeschwindigkeit.grid(column=2, row=5, padx=5, pady=5)
    
    tk.Label(EinstFenster, text=" Abwurfwinkel in Grad",font=('helvetica', 10)).grid(column=1, row=6, sticky=tk.W, padx=5, pady=5)
    eingabeAbwurfwinkel =  tk.Entry(EinstFenster,width=25)
    eingabeAbwurfwinkel.grid(column=2, row=6, padx=5, pady=5)

    tk.Label(EinstFenster, text=" Abwurfrichtung in Grad",font=('Helvetica', 10)).grid(column=1, row=7, sticky=tk.W, padx=5, pady=5)
    eingabeAbwurfrichtung =  tk.Entry(EinstFenster,width=25)
    eingabeAbwurfrichtung.grid(column=2, row=7, padx=5, pady=5)

    tk.Label(EinstFenster, text=" Neigung des Untergrunds in Grad",font=('Helvetica', 10)).grid(column=1, row=8, sticky=tk.W, padx=5, pady=5)
    eingabeNeigungEbene =  tk.Entry(EinstFenster,width=25)
    eingabeNeigungEbene.grid(column=2, row=8, padx=5, pady=5)

    tk.Button(EinstFenster,bg='#E4E0DF',width= 20, text ="   Eingaben übernehmen   ",font=('Helvetica', 12),command = push).grid(column=0,columnspan = 4, row=9, padx=5, pady=5)

    
    
    





# =========================================================================================================================================================================
#                                                                           ABSCHNITT HAUPTPROGRAMM
# =========================================================================================================================================================================

def Hauptprogramm():
    global pen, pen2, pen6, pen7, Zieldistanz
    global knopf1
    global ProgrFenster
    
    # ==== Generierung des UserInterface ====
    ProgrFenster = tk.Tk()
    ProgrFenster.title("Hauptprogramm")
    ProgrFenster.geometry("1200x500")
    ProgrFenster.resizable(0,0)
    ProgrFenster.columnconfigure(0, weight=1)
    ProgrFenster.columnconfigure(1, weight=16)
    ProgrFenster.columnconfigure(2, weight=8)
    ProgrFenster.columnconfigure(3, weight=8)
    ProgrFenster.columnconfigure(4, weight=1)

    platzhalter = tk.Canvas(ProgrFenster)
    platzhalter.config(width=800, height=50)
    platzhalter.grid(column=1, row=0)
    
    canvas = tk.Canvas(ProgrFenster)
    canvas.config(width=800, height=400)
    canvas.grid(column=1, row=1, rowspan=3)
    screen = turtle.TurtleScreen(canvas)
    screen.bgcolor("white")

    canvas1 = tk.Canvas(ProgrFenster)
    canvas1.config(width=300, height=300)
    canvas1.grid(column=2, row=3, columnspan = 2)
    screen1 = turtle.TurtleScreen(canvas1)
    screen1.bgcolor("white")
    
    tk.Label(ProgrFenster, text="Zieldistanz in m",font=('Helvetica bold', 10)).grid(column=2, row=2, padx=5, pady=5)
    Zieldistanz = tk.Entry(ProgrFenster,width = 25)
    Zieldistanz.grid(column = 3, row = 2)

    HauptFenster.bind('<Return>', StartEnter)
    

    # ==== Generierung der zeichenenden Elemente ====
    pen = turtle.RawTurtle(screen)
    pen1 = turtle.RawTurtle(screen)
    pen2 = turtle.RawTurtle(screen)
    pen3 = turtle.RawTurtle(screen)
    pen4 = turtle.RawTurtle(screen1)
    pen5 = turtle.RawTurtle(screen1)
    pen6 = turtle.RawTurtle(screen1)
    pen7 = turtle.RawTurtle(screen)
    
    pen.hideturtle()
    pen2.hideturtle()
    pen4.hideturtle()
    pen6.hideturtle()
    pen7.hideturtle()

    # ==== Zeichnen des Koordinatensystems ====
    pen1.speed(0)
    pen1.shape('square')
    pen1.penup()
    pen1.shapesize(stretch_wid = 0.01, stretch_len = 40)
    pen1._rotate(90)
    pen1.goto(-200,0)        
    pen3.speed(0)
    pen3.shape('square')
    pen3.penup()
    pen3.shapesize(stretch_wid = 0.01, stretch_len = 40)
    pen3.goto(0,-199)

    pen7.pencolor('black')
    pen7.penup()
    pen7.goto(-120,-199)
    pen7.pendown()
    pen7.goto(-120,-195)
    pen7.penup()
    pen7.write('1m',align = 'center', font=('Courier',10,'normal'))
    pen7.goto(-40,-199)
    pen7.pendown()
    pen7.goto(-40,-195)
    pen7.penup()
    pen7.goto(40,-199)
    pen7.pendown()
    pen7.goto(40,-195)
    pen7.penup()
    pen7.goto(120,-199)
    pen7.pendown()
    pen7.goto(120,-195)
    pen7.penup()
    pen7.goto(200,-199)
    pen7.pendown()
    pen7.goto(200,-195)
    pen7.penup()
    pen7.goto(280,-199)
    pen7.pendown()
    pen7.goto(280,-195)
    pen7.penup()

    
    pen7.goto(-280,-199)
    pen7.pendown()
    pen7.goto(-280,-195)
    pen7.penup()
    pen7.write('-1m',align = 'center', font=('Courier',10,'normal'))
    pen7.goto(-360,-199)
    pen7.pendown()
    pen7.goto(-360,-195)
    pen7.penup()

    pen7.goto(-200,-119)
    pen7.pendown()
    pen7.goto(-196,-119)
    pen7.penup()
    pen7.goto(-185,-127)
    pen7.write('1m',align = 'center', font=('Courier',10,'normal'))
    pen7.goto(-200,-39)
    pen7.pendown()
    pen7.goto(-196,-39)
    pen7.penup()
    pen7.goto(-200,41)
    pen7.pendown()
    pen7.goto(-196,41)
    pen7.penup()
    pen7.goto(-200,121)
    pen7.pendown()
    pen7.goto(-196,121)
    pen7.penup()

    # ==== Mittelpunkt und Himmelsrichtungen ====
    pen4.penup()
    pen4.goto(-2.5,135)
    pen4.write('N',align = 'left', font=('Courier',10,'normal'))
    pen4.goto(140,-5)
    pen4.write('O',align = 'left', font=('Courier',10,'normal'))
    pen4.goto(-2.5,-150)
    pen4.write('S', align = 'left', font=('Courier',10,'normal'))
    pen4.goto(-145,-5)
    pen4.write('W', align = 'left', font=('Courier',10,'normal'))
    
    pen5.shape('circle')
    pen5.penup()
    pen5.shapesize(stretch_wid = 0.2, stretch_len = 0.2)
    pen5.goto(0,0)
    
    # ==== Ausgabe leerer Werte für Höhe und Distanz ====
    pen2.penup()
    pen2.color('black')
    pen2.goto(200,180)
    pen2.write('maximale Distanz: - m  ',align = 'left', font=('Courier',10,'normal'))
    pen2.goto(200,165)
    pen2.write('maximale Höhe: - m  ',align = 'left', font=('Courier',10,'normal'))
    pen2.goto(200,135)
    pen2.write('Berechnungszeit: - s  ', align = 'left', font=('Courier',10,'normal'))
    pen2.color('red')
    pen2.goto(200,150)
    pen2.write('Angepasster Winkel: - ° ', align = 'left', font=('Courier',10,'normal'))

    knopf1 = tk.Button(ProgrFenster,width=32, height=1, text="Wurfparabel Zeichen", font=('Helvetica bold', 12), command=ausführen)
    knopf1.grid(column=2, row=1,columnspan = 2)






# =========================================================================================================================================================================
#                                                                           ABSCHNITT BEDIENUNGSANLEITUNG
# =========================================================================================================================================================================
def Bedienung():
    
    AnleiFenster = tk.Tk()
    AnleiFenster.geometry("990x550")
    AnleiFenster.title("Bedienungsanleitung")
    AnleiFenster.resizable(0,0)
    AnleiFenster.configure(bg='#F2F2F2',)

    AnleiFenster.columnconfigure(0, weight=1)
    AnleiFenster.columnconfigure(1, weight=1)
    AnleiFenster.columnconfigure(2, weight=1)

    label0 = tk.Label(AnleiFenster,bg='#F2F2F2',text ="\n Bedienungsweise des Programms",font=('Helvetica bold', 17))
    label0.grid(column=0, row=0, padx=5, pady=5,columnspan=3)

    label1 = tk.Label(AnleiFenster,bg='#F2F2F2',text ="\
    Das Ihnen vorliegende Programm simuliert, mit Hilfe von physikalischen Eckdaten die Flugbahn von Wassertropfen aus einem \n \
    Wassersprenger. Um das Programm zu verwenden müssen Sie lediglich über das Hauptmenü den Button 'Programm starten' \n \
    anklicken. Hierauf öffnet sich ein weiteres Fenster. Nachdem Sie hier den Button 'Wurfparabel zeichnen' anklicken liefert \n \
    Ihnen das Programm mehrere Outputs: \n \
    \n \
    1. Höhe und Distanz \n \
        Diese Werte beschreiben die maximale Höhe und Distanz, die die vom Wassersprenger abgegebenen Wassertropfen erreichen. \n \
    \n \
    2. Flugparabel \n \
        In dem nebenstehenden Koordinatensystem wird eine Parabel gezeichnet. Diese Parabel beschreibt visuell die Flugbahn der \n \
        Wassertropfen. Der Ausgangspunkt der Parabel (Koordinatenursprung) beschreibt die Position des Wassersprengers. \n \
    \n \
    3. Kreisdiagramm \n \
        Das gegebene Diagramm beschreibt die Flugrichtung der Wassertropfen relativ zum Wassersprenger. \n \
    \n \
    4. empfohlener Neigungswinkel \n \
        Unter 'angepasster Winkel' zeigt das Programm an, wie weit (Gradmaß) der Rasensprenger geneigt werden \n \
        mmuss, um den Zielbereich möglichst Verlustfrei zu bewässern.  \n \
    \n \
    Über den Button 'Einstellungen' im Hauptmenü können Sie die physikalischen Eckdaten zur Berechnung anpassen. Außerdem können \n \
    Sie festlegen, wie präzise gezeichnet und gerechnet werden soll. Höhere Präzision benötigt längere Rechenzeiten, geringere \n \
    Präzision führt zu abweichenden Ergebnissen. einfach zu vergleichen ist dies mithilfe des 'Berechnungszeit'-Outputs im \n \
    Programmfenster. Sie müssen Ihre Eingaben über 'Eingaben übernehmen' bestätigen. Nicht gefüllte Felder werden automatisch mit \n \
    Standardwerten aufgefüllt (siehe 4.2.2 Erstellung der Benutzeroberfläche).",font=('Helvetica bold', 12), justify='left')
    label1.grid(column=0, row=1, padx=5, pady=5,columnspan=3, sticky='w')







# =========================================================================================================================================================================
#                                                                           ABSCHNITT BEGRÜßUNGSFENSTER
# =========================================================================================================================================================================

reseingabeWindrichtung = 180
reseingabeWindgeschwindigkeit = 0
reseingabeGenauigkeit = 'ausgewogen'
reseingabeAbwurfgeschwindigkeit = 10
reseingabeAbwurfwinkel = 30
reseingabeAbwurfrichtung = 0
reseingabeCWWERT = 0.4
reseingabeLuftdichte = 1.293
reseingabeFallbeschleunigung = 9.81
reseingabeNeigungEbene = 0
Genauigkeit = 'ausgewogen'
reseingabeZieldistanz = 5

HauptFenster = tk.Tk()
HauptFenster.geometry("1000x500")
HauptFenster.title("Willkommen")
HauptFenster.resizable(0,0)
HauptFenster.configure(bg='#F2F2F2',)

HauptFenster.columnconfigure(0, weight=1)
HauptFenster.columnconfigure(1, weight=1)
HauptFenster.columnconfigure(2, weight=1)

label0 = tk.Label(HauptFenster,bg='#F2F2F2',text ="\n Konrad Martin Drissen, Nils Mario Lange, Alexander-Lucas Meier",font=('Helvetica bold', 10))
label0.grid(column=0, row=0, padx=5, pady=5,columnspan=3)

label1 = tk.Label(HauptFenster,bg='#F2F2F2',text ="\n \n Entwicklung eines Simulationsprogramms zur \n effizienteren Bewässerung durch einen Wassersprenger \n ",font=('Helvetica bold', 17))
label1.grid(column=0, row=1, padx=5, pady=5,columnspan=3)


#image1 = Image.open(r"‪H:\Seminarfach 10\s2-logo.png")
#test = ImageTk.PhotoImage(image1)
#label2 = tk.Label(HauptFenster,bg='#F2F2F2',image=test, text = "\n")
#label2.image = test
#label2.grid(column=0, row=2, padx=5, pady=5,columnspan=5)

label3 = tk.Label(HauptFenster,bg='#F2F2F2', text = "\n \n").grid(column=1, row=3, padx=5, pady=5)

tk.Button(HauptFenster,bg='#E4E0DF',width= 20, text ="   Einstellungen   ",font=('Helvetica bold', 12),command = Einstellungen).grid(column=0, row=4, padx=5, pady=5)
tk.Button(HauptFenster,bg='#E4E0DF',width= 20, text =" Programm  starten ",font=('Helvetica bold', 12),command = Hauptprogramm).grid(column=1, row=4, padx=5, pady=5)
tk.Button(HauptFenster,bg='#E4E0DF',width= 20, text ="Bedienungsanleitung",font=('Helvetica bold', 12),command = Bedienung).grid(column=2, row=4, padx=5, pady=5)

HauptFenster.mainloop()

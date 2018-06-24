from tkinter import*

import socket

s = socket.socket()#Herstellung der drahtlosen Kommunikation
s.connect(('172.20.10.3', 30303))
s.setblocking(True)

k=1#Variablen zur Umrechnung der empfangenden Zahlen
z=1
j=1

class Rennen():
    global Eingabe_vom_ersten_Spielernamen
    Eingabe_vom_ersten_Spielernamen = Tk()#Erstellung des ersten Fensters zur Eingabe vom Spielernamen
    Eingabe_vom_ersten_Spielernamen.title("Spielername 1")#Name des Fensters festgelegt

    text1 = Label(Eingabe_vom_ersten_Spielernamen, text="Spieler 1")#Beschriftung des Eingabefeldes

    global eingabefeld1
    eingabefeld1 = Entry(Eingabe_vom_ersten_Spielernamen, bd=5, width=40)#Eingabefeld eingefügt



                             
    def EingabeName1():
        """ In der Definition wollen wir den ersten Spielernamen eingeben.
        Mit einer if-Schleife legen wir fest,
        dass wenn ein Name eingegeben wird,der Name als Spielername1 festgelegt wird.
        Wenn nichts eingegeben wurde, wird "Gib zuerst einen Namen ein." geprintet.
        Nach der Eingabe wird das Fenster zur Teamwahl geöffnet."""
        global Spielername1
        Spielername1 = eingabefeld1.get() #Eingabe=Spielername1
        if (Spielername1 == ""):
            fehlermeldung.config(text="Gib zuerst einen Namen ein.")#Fehlermeldung falls kein Name eingegeben wurde
        else:
            print(Spielername1)
            Eingabe_vom_ersten_Spielernamen.quit()#Fenster wird geschlossen
            Eingabe_vom_ersten_Spielernamen.destroy()
            TeamwahlSpieler1()#neues Fenster wird geöffnet
    
    Spielername1 = eingabefeld1.get()

    weiter_button = Button(Eingabe_vom_ersten_Spielernamen, bg='SpringGreen3', text="GO!", command=EingabeName1)
    fehlermeldung = Label(Eingabe_vom_ersten_Spielernamen)

    exit_button = Button(Eingabe_vom_ersten_Spielernamen, bg='brown3', text="Beenden", command=Eingabe_vom_ersten_Spielernamen.quit)#Optisches Layout
    exit_button = Button(Eingabe_vom_ersten_Spielernamen, bg='brown3', text="Beenden", command=Eingabe_vom_ersten_Spielernamen.destroy)

    text1.grid(row = 0, column = 0)
    eingabefeld1.grid(row = 0, column = 1)
    weiter_button.grid(row = 1, column = 1)
    exit_button.grid(row = 3, column = 1)
    fehlermeldung.grid(row = 2, column = 0, columnspan = 2)

    #fenster 1 ende

    
    global TeamwahlSpieler1
    def  TeamwahlSpieler1():
        """In dem Fenster Teamwahl werden drei Buttons zur Wahl von einem Team angezeigt.
        Sobald man ein Team ausgewählz hat, wird dies als globale Variable gesetzt
        und es wird das nächste Fenster geöffnet. Nun beginnt das Gleiche für Spieler2"""
        global Teamwahl_vom_ersten_Spieler
        Teamwahl_vom_ersten_Spieler = Tk()
        Teamwahl_vom_ersten_Spieler.title("Teamwahl")#Erstelllung Fenster zur Teamwahl von Spieler1
        global text5
        text5= Label(Teamwahl_vom_ersten_Spieler, text=("Für welches Team möchtest du unterschreiben?"))

    global mercedesteam 
    def mercedesteam1():#Erster Button Team Mercedes 
        """Beim Auswählen von diesem Button wird für Spieler1 das Team Mercedes festgelegt."""
        text5.config(bg='dark turquoise', fg='white', text='Ihr Team ist Mercedes! Drücken sie Weiter um fortzufahren.')
        global Team1
        Team1="Mercedes Benz"#Festlegung des Teams
        global Team1Farbe
        global Team1Schrift
        Team1Farbe="dark turquoise"#Festlegung Farbe
        Team1Schrift="white"#Feslegung Schrift
        weiter_button = Button(Teamwahl_vom_ersten_Spieler, bg='SpringGreen3', text="Weiter!", command=Eingabe_zweiter_Spielername)
        
        Teamwahl_vom_ersten_Spieler.geometry("500x150")
        weiter_button.place(x=200, y=100, width=100, height=30)
        text5.place(x = 90, y = 20, width=320, height=15)

    global ferrariteam   
    def ferrariteam1():#Zweiter Buttton Team Ferrari
        """Beim Auswählen von diesem Button wird für Spieler1 das Team Ferrari festgelegt."""
        text5.config(bg='firebrick2', fg='black', text='Ihr Team ist Ferrari! Drücken sie Weiter um fortzufahren.')
        global Team1
        Team1="Ferrari"#Festlegung des Teams
        global Team1Farbe
        global Team1Schrift
        Team1Farbe="firebrick2"#Festlegung Farbe
        Team1Schrift="black"#Feslegung Schrift
        weiter_button = Button(Teamwahl_vom_ersten_Spieler, bg='SpringGreen3', text="Weiter!", command=Eingabe_zweiter_Spielername)

        Teamwahl_vom_ersten_Spieler.geometry("500x150")
        weiter_button.place(x=200, y=100, width=100, height=30)
        text5.place(x = 100, y = 20, width=300, height=15)

    global redbullracinteam
    def redbullracingteam1():#Dritter Button Team Redbullracing
         """Beim Auswählen von diesem Button wird für Spieler1 das Team Redbull festgelegt."""
         text5.config(bg='navy', fg='yellow', text='Ihr Team ist Red Bull Racing! Drücken sie Weiter um fortzufahren.')
         global Team1
         Team1="Red Bull Racing"#Festlegung des Teams
         global Team1Farbe
         global Team1Schrift
         Team1Farbe="navy"#Festlegung Farbe
         Team1Schrift="yellow"#Feslegung Schrift
         
         weiter_button = Button(Teamwahl_vom_ersten_Spieler, bg='SpringGreen3', text="Weiter!", command=Eingabe_zweiter_Spielername)
         Teamwahl_vom_ersten_Spieler.geometry("500x150")
         weiter_button.place(x=200, y=100, width=100, height=30)
         text5.place(x = 75, y = 20, width=350, height=15)
         mercedes_button = Button(Teamwahl_vom_ersten_Spieler, bg='dark turquoise', fg='white', text="Mercedes-Benz", command=mercedesteam)
         ferrari_button = Button(Teamwahl_vom_ersten_Spieler, bg='firebrick2', fg='black', text="Ferrari", command=ferrariteam)    
         redbullracing_button = Button(Teamwahl_vom_ersten_Spieler, bg='navy', fg='yellow', text="Red Bull Racing", command=redbullracingteam)
        
    
         Teamwahl_vom_ersten_Spieler.geometry("500x100")
    
         text5.place(x = 50, y = 20, width=400, height=15)
         mercedes_button.place(x = 70, y = 50, width=100, height=30)
         ferrari_button.place(x = 200, y = 50, width=100, height=30)
         redbullracing_button.place(x = 330, y = 50, width=100, height=30)
    

    global Eingabe_zweiter_Spielername
    
    def Eingabe_zweiter_Spielername():
        """Diese Definition beendet die Eingaben für Spieler1 und beginnt mit Spieler2."""
        
        Teamwahl_vom_ersten_Spieler.quit()#Schließen des Fensters
        Teamwahl_vom_ersten_Spieler.destroy()
        Eingabe_vom_zweiten_Spielernamen = Tk()#Öffnen des neuen Fensters
        Eingabe_vom_zweiten_Spielernamen.title("Spielername 2")
        text2 = Label(fenster2, text="Spieler 2")

        eingabefeld2 = Entry(Eingabe_vom_zweiten_Spielernamen, bd=5, width=40)
        global EingabeName2
        def EingabeName2():
            """Dieses Fenster funktioniert fast gleich wie für Spieler1 bis auf die Ausnahme,
            dass falls der eingegebene Name für Spieler2 der gleiche wie für Spieler1 ist,
            wird angezeigt 'Geben sie einen anderen Namen ein!' und es muss ein anderer Name eingegeben werden.
            Nach der Eingabe wird wieder das Fenster für die Temawahl geöffnet."""
        
            global Spielername2
            Spielername2 = eingabefeld2.get()#Eingabe des nächsten Spielernamens
            if (Spielername2 == ""):
                fehlermeldung2.config(text="Gib zuerst einen Namen ein.")
            elif(Spielername2 == Spielername1):
                fehlermeldung2.config(text="Geben sie einen anderen Namen ein!")#Fehlermeldung falls beide Spieler den gleichen Namen eingegeben haben                                  
            
            else:
                print(Spielername2)
                Eingabe_vom_zweiten_Spielernamen.quit()
                Eingabe_vom_zweiten_Spielernamen.destroy()
                print("3")
                TeamwahlSpieler2()
                print("4")

        weiter_button = Button(Eingabe_vom_zweiten_Spielernamen, bg='SpringGreen2', text="GO!", command=EingabeName2)
        fehlermeldung2 = Label(Eingabe_vom_zweiten_Spielernamen)
        print("5")
        exit_button = Button(Eingabe_vom_zweiten_Spielernamen, bg='brown2', text="Beenden", command=fenster2.quit)
        exit_button = Button(Eingabe_vom_zweiten_Spielernamen, bg='brown2', text="Beenden", command=fenster2.destroy)

        text2.grid(row = 0, column = 0)
        eingabefeld2.grid(row = 0, column = 1)
        weiter_button.grid(row = 1, column = 1)
        exit_button.grid(row = 3, column = 1)
        fehlermeldung2.grid(row = 2, column = 0, columnspan = 2)
 
    #fenster 2 ende
    
    global TeamwahlSpieler2
    

    def TeamwahlSpieler2():#Teamwahl des zweiten Spielers
        """Nun darf Spieler2 sein Team wählen und hat wie Spieler1 die gleichen drei Teams zur Auswahl."""
        global fenster6
        fenster6 = Tk()
        fenster6.title("Teamwahl")
        global text6
        text6= Label(fenster6, text=("Für welches Team möchtest du unterschreiben?"))

    global mercedesteam2
    def mercedesteam2():
        """Bei Auswahl wird für Spieler2 das Team Mercedes ausgewählt, falls Spieler1 das Team schon ausgwahlt hat,
        wird 'Sie dürfen nicht das gleiche Team wählen!' geprintet."""
        global Team2
        Team2="Mercedes Benz"
        if (Team2==Team1):
            text6.config(fg='red', text='Sie dürfen nicht das gleiche Team wählen!')#Fehlermeldung falls Spieler1 das Team schon gewählt hat

        else:
            text6.config(bg='dark turquoise', fg='white', text='Ihr Team ist Mercedes! Drücken sie Weiter um fortzufahren.')
            Team2=mercedesteam
            global Team2Farbe
            global Team2Schrift
            Team2Farbe="dark turquoise"
            Team2Schrift="white"
            weiter_button = Button(fenster6, bg='SpringGreen3', text="Weiter!", command=Startbildschirm)
            fenster6.geometry("500x150")
            weiter_button.place(x=200, y=100, width=100, height=30)
            text6.place(x = 90, y = 20, width=320, height=15)

    global ferrariteam2
    def ferrariteam2():
        """Bei Auswahl wird für Spieler2 das Team Ferrari ausgewählt, falls Spieler1 das Team schon ausgwahlt hat,
        wird 'Sie dürfen nicht das gleiche Team wählen!' geprintet."""
        global Team2
        Team2="Ferrari"
        if (Team2==Team1):
            text6.config(fg='red', text='Sie dürfen nicht das gleiche Team wählen!')#Fehlermeldung falls Spieler1 das Team schon gewählt hat
        else:
            text6.config(bg='firebrick2', fg='black', text='Ihr Team ist Ferrari! Drücken sie Weiter um fortzufahren.')
            global Team2Farbe
            global Team2Schrift
            Team2Farbe="firebrick2"
            Team2Schrift="black"
            weiter_button = Button(fenster6, bg='SpringGreen3', text="Weiter!", command=Startbildschirm)
            fenster6.geometry("500x150")
            weiter_button.place(x=200, y=100, width=100, height=30)
            text6.place(x = 100, y = 20, width=300, height=15)

    global redbullracingteam2
    def redbullracingteam2():
        """Bei Auswahl wird für Spieler2 das Team Redbull ausgewählt, falls Spieler1 das Team schon ausgwahlt hat,
        wird 'Sie dürfen nicht das gleiche Team wählen!' geprintet."""
        global Team2
        Team2="Red Bull Racing"
        if (Team2==Team1):
            text6.config(fg='red', text='Sie dürfen nicht das gleiche Team wählen!')#Fehlermeldung falls Spieler1 das Team schon gewählt hat
        else:
            text6.config(bg='navy', fg='yellow', text='Ihr Team ist Red Bull Racing! Drücken sie Weiter um fortzufahren.')
            global Team2Farbe
            global Team2Schrift
            Team2Farbe="navy"
            Team2Schrift="yellow"
            weiter_button = Button(fenster6, bg='SpringGreen3', text="Weiter!", command=Startbildschirm)
            fenster6.geometry("500x150")
            weiter_button.place(x=200, y=100, width=100, height=30)
            text6.place(x = 75, y = 20, width=350, height=15)
    


        mercedes_button = Button(fenster6, bg='dark turquoise', fg='white', text="Mercedes-Benz", command=mercedesteam)
        ferrari_button = Button(fenster6, bg='firebrick2', fg='black', text="Ferrari", command=ferrariteam)    
        redbullracing_button = Button(fenster6, bg='navy', fg='yellow', text="Red Bull Racing", command=redbullracingteam)
    
    
        fenster6.geometry("500x100")
    
        text6.place(x = 50, y = 20, width=400, height=15)
        mercedes_button.place(x = 70, y = 50, width=100, height=30)
        ferrari_button.place(x = 200, y = 50, width=100, height=30)
        redbullracing_button.place(x = 330, y = 50, width=100, height=30)
    

#fenster 6 ende
    
    global Startbildschirm
    def Startbildschirm():
        """In dieser Definition schließen wir die Eingabe für Spieler2 und
        öffnen ein neues Fenster mit einem Button für den Rennstart."""
        fenster6.quit()
        fenster6.destroy()#Schließen der Eingabe von Spielerinformationen
        global fenster3
        fenster3 = Tk()
        fenster3.title("Rennbeginn")#Fenster zum Starten des Rennens
        start_button = Button(fenster3, text="Start", command=rennstart)#Festlegen des Startbuttons
        global text3
        text3 = Label(fenster3, text="Drücke hier um ein neues Spiel zu starten?")
    

        fenster3.geometry("400x400")

        text3.place(x = 80, y = 100, width=240, height=100)
        start_button.place(x = 100, y = 200, width= 200, height=100)

    global rennstart
    def rennstart():
        """Hier wird der Rennstartbutton definiert. Er schließt das Fenster und öffnet ein neues Fenster,
        welches die die Zeiten für die Rundenzeit und Geschwindigkeit vom Arduino drahtlos empfängt.
        Die Geschwindig wurde im Arduino + 100000 gerechnet und so können wir die empfangenden Zahelen unterscheiden.
        Die Geschwindigkeit wird in km/h umgerechnet und die Rundenzeit in Minuten.
        Anschließend werden die Werte in einer Tabelle geprintet.  """
        fenster3.quit()
        fenster3.destroy()#Button schließt das letzte Fenster
        #text3.config(text="Erneut spielen?")
        fenster4 = Tk()
        fenster4.title("Rundenzeiten")#Button öffnet das nächste Fenster
        s.send(b'1\n')#Senden des Startsignals an den Arduino
        Rundenanzahl = 5 #Festlegung der Rundenzahl
        fenster4.geometry("450x650")

        spaltespieler1 = Label(fenster4, bg=Team1Farbe, fg=Team1Schrift, text=Spielername1)
        spaltespieler2 = Label(fenster4, bg=Team2Farbe, fg=Team2Schrift, text=Spielername2)
        spalteteam1 = Label(fenster4, fg=Team1Farbe, text=Team1)
        spalteteam2 = Label(fenster4, fg=Team2Farbe, text=Team2)
        spaltespieler1.place(x = 150, y = 15, width = 95, height = 30)
        spaltespieler2.place(x = 300, y = 15, width = 95, height = 30)
        spalteteam1.place(x = 150, y = 50, width = 95, height = 15)
        spalteteam2.place(x = 300, y = 50, width = 95, height = 15)

    
        for i in range(Rundenanzahl):#Tabelle wird in der Größe der Rundenzahl geprintet
            print(i)
            rundenbezifferung = Label(fenster4, bg='skyblue', text=("Runde",(i+1),))
            rundenbezifferung.place(x = 0, y = 85*(i+1), width = 105, height = 20)
            geschwindigkeitsbezifferung = Label(fenster4, bg='beige', text=("Geschwindigkeit"))
            geschwindigkeitsbezifferung.place(x = 0, y = 85*(i+1) + 30, width = 105, height = 20)

 ##   
        x = s.recv(1024)#Python empfängt Zahlen vom Arduino
    
        if (float (x) > 100000):#Zahlen größer 100000 geben Geschwindigkeit an, der Arduino addiert 100000 damit die Zahlen unterschieden werden können
            global k
            if(k<6):
                x = float (x) - 100000#100000 wird abgezogen um auf die Ursprungszahl zu kommen
                x = (float (x)/1000)
                print(x)
                y = s.recv(1024)
                ms = (0.115/(float (y)/1000))
                kmh = (ms*3.6)
                print("KKKKKKKKKKKKKKKKKKKKKKK")
                print(y)
            
                x = s.recv(1024)
                x = (float (x)/1000)
                print(x)
                y = s.recv(1024)
                ms = (0.115/(float (y)/1000))
                kmh = (ms*3.6)

            

        elif (float (x)<= 100000):
            global z
            if(z<6):  
                x = (float (x)/1000)
                print(x)
                y = s.recv(1024)
                ms = (0.115/(float (y)/1000))
                print("ZZZZZZZZZZZZZZZZZZZZZZZ")
                kmh = (ms*3.6)
                print(y)
                
                x = s.recv(1024)
                x = float (x) - 100000
                x = (float (x)/1000)
                print(x)
                y = s.recv(1024)
            ms = (0.115/(float (y)/1000))
            kmh = (ms*3.6)
            

    
        while (k+z)<12:
            print("ICH BIN HIER")
            print(k)
            print(z)
            x = s.recv(1024)
    
            if (float (x) > 100000):
                if(k<6):
                    x = float (x) - 100000
                    x = (float (x)/1000)
                    print(x)
                    y = s.recv(1024)
                    ms = (0.115/(float (y)/1000))
                    print(ms)
                    kmh = (ms*3.6)
                    print(kmh)
                    print(y)
                    rundenzeiten = Label(fenster4, text =(round(x,2),"Sekunden"))
                    rundenzeiten.place (x = 150, y = (k*85), width = 105, height = 20)
                    geschwindigkeit = Label(fenster4, text=(round(kmh, 3)," km/h  ")) 
                    geschwindigkeit.place (x = 150,  y = (k*85) + 30, width = 105, height = 20)
                    k = k + 1
        

            else:
                if(z<6):
                    x = (float (x)/1000)
                    print(x)
                    y = s.recv(1024)
                    ms = (0.115/(float (y)/1000))
                    print(ms)
                    kmh = (ms*3.6)
                    print(kmh)
                    print(y)
                    rundenzeiten = Label(fenster4, text =(round(x,2),"Sekunden"))
                    rundenzeiten.place (x = 300, y = (z*85), width = 105, height = 20)
                    geschwindigkeit = Label(fenster4, text=(round(kmh, 3)," km/h  ")) 
                    geschwindigkeit.place (x = 300,  y = (z*85) + 30, width = 105, height = 20)
                    z = z + 1

        if(k+z==12):
             k=1
             z=1
        
        

mainloop()            

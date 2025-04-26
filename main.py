from BelfoldiJarat import Belfoldijarat
from NemzetkoziJarat import NemzetkoziJarat
from JegyFoglalas import JegyFoglalas
from LegiTarsasag import LegiTarsasag
from os import system, name

def cls():
    if name == 'nt':
        system('cls')
    else:
        system('clear')





class FoglaloRendszer:
    def __init__(self):
        self.foglalasok = []
        self.legitarsasag = []

    def __add__(self, other):
        self.legitarsasag.append(other)

    def fejlec(self):
        cls()
        print("                 Budapesti Repülőtér ")
        print()


    def tarsasagok_jaratok(self):
        print(
            "Légitársaság         Típus           Azonosító        Celallomas              indulási idő          Terminál")
        print(
            "------------         -----           ---------        ----------              ------------          --------")

        for j in self.legitarsasag:
            for i in j.jaratok:
                s = j.nev
                for z in range(20 - len(s)):  # légitársaság neve
                   s += " "
                s += i.jarattipus
                for z in range(40 - len(s)):  # id
                   s += " "
                s += i.id
                for z in range(55 - len(s)):  # célállomás jön
                   s += " "
                s += i.celallomas
                for z in range(76 - len(s)):  # indulási idő
                   s += " "
                s += i.indulasiido
                for z in range(105 - len(s)):  # terminál
                   s += " "
                s += i.terminal
                print(s)


    def foglalas_feltoltes(self):
        self.foglalasok.append(JegyFoglalas(self.legitarsasag[0].nev,self.legitarsasag[0].jaratok[0],1,"Mekk Elek"))
        self.foglalasok.append(JegyFoglalas(self.legitarsasag[0].nev,self.legitarsasag[0].jaratok[1],2,"Péter Dániel"))
        self.foglalasok.append(JegyFoglalas(self.legitarsasag[1].nev,self.legitarsasag[1].jaratok[0],2,"Józsa Dávid"))
        self.foglalasok.append(JegyFoglalas(self.legitarsasag[0].nev,self.legitarsasag[0].jaratok[3],1,"Molnár Júlia"))

    def foglalas_listazas(self):
        self.fejlec()
        print(" ------------------------FOGLALÁSOK LISTÁZÁSA----------------------------")
        for i in self.foglalasok:
            print(f"{i.ltarsasag}  {i.jarat.id} {i.jarat.celallomas} {i.jarat.indulasiido} osztály:{i.osztaly} utas:{i.utas}")

    def foglalas(self):
        print("------------Jegy Foglalás-------------")
        print()
        while True:
            j = input("Kérem adja meg a járat számát, vagy 0-val kiléphet:")
            if j == "0":
                return
            for ltr in self.legitarsasag:
                ut=ltr.checkid(j)
                if ut >0:
                    break
            if ut == -1:
                print("Ez a járat azonosító nem létezik!")
            else:
                break
        print("A repülőgépen két utasosztály érhető el:")
        print(f"Első osztály ár : {ltr.jaratok[ut].ar1}")
        print(f"Másodosztály ár : {ltr.jaratok[ut].ar2}")

        while True:
            o = input(f"Melyik osztályra szeretne jegyet vásárolni ? (1/2):")
            if o=="1" or o=="2":
                break
        utas=input("Kérem adja meg a nevét a foglaláshoz:")
        self.foglalasok.append(JegyFoglalas(ltr,ltr.jaratok[ut],o, utas))
        print(f"Köszönöm, {utas}, a jegye lefoglalásra került a {j} azonosíójú repülőjáratra, {o} osztályra!")
    def menurendszer(self):
        while True:
            cls()
            print("                                             Budapesti Repülőtér")
            print()
            print("                                        1 .... Járatok listázása")
            print("                                        2 .... Jegyfoglalások listázása")
            print("                                        3 .... Jegyfoglalás egy járatra")
            print("                                        4 .... Jegyfoglalás lemondása")
            for i in range(3):
                print()
            c = int(input("Válassz egy menüpontot:"))
            if c == 1:
                cls()
                self.tarsasagok_jaratok()
                print()
                input("Enter a visszalépéshez")
            elif c == 2:
                cls()
                self.foglalas_listazas()
                print()
                input("Enter a visszalépéshez")
            elif c == 3:
                cls()
                self.foglalas()
                print()
                input("Enter a visszalépéshez")

        pass




f=FoglaloRendszer()

L=LegiTarsasag("MRT Légitársaság")
L.jaratok = Belfoldijarat('BE456', 'A1', '2025.05.25 10:00', 'Debrecen', 24, 96, 30000, 20000)
L.jaratok = Belfoldijarat('BE460', 'A2', '2025.05.26 10:00', 'Szeged', 16, 64, 30000, 20000)
L.jaratok = NemzetkoziJarat('NE401', 'B1', '2025.05.24 11:00', 'Berlin', 24, 96, 40000, 30000)
L.jaratok = NemzetkoziJarat('NE560', 'B2', '2025.05.26 12:00', 'Amszterdam', 24, 96, 50000, 40000)
L.jaratok = NemzetkoziJarat('NE332', 'B3', '2025.05.27 13:00', 'Cyprus', 24, 96, 80000, 60000)

f + L

L2=LegiTarsasag("Ryanair")
L2.jaratok = NemzetkoziJarat('RNE346', 'C', '2025.06.01 12:00', 'Amszterdam', 24, 96, 50000, 40000)


f + L2


f.foglalas_feltoltes()
f.menurendszer()



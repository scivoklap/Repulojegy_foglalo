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
    def __init__(self,legitarsasag):
        self.foglalasok = []
        self.legitarsasag = legitarsasag
        self.foglalas_feltoltes()

    def foglalas_feltoltes(self):
        self.foglalasok.append(JegyFoglalas(self.legitarsasag.jaratok[0],1,"Mekk Elek"))
        self.foglalasok.append(JegyFoglalas(self.legitarsasag.jaratok[1],2,"Péter Dániel"))
        self.foglalasok.append(JegyFoglalas(self.legitarsasag.jaratok[2],2,"Józsa Dávid"))
        self.foglalasok.append(JegyFoglalas(self.legitarsasag.jaratok[3],1,"Molnár Júlia"))

    def foglalas_listazas(self):
        for i in self.foglalasok:
            print(f"{i.jarat.id} {i.jarat.celallomas} {i.jarat.indulasiido} osztály:{i.osztaly} utas:{i.utas}")

    def foglalas(self):
        print("------------Jegy Foglalás-------------")
        print()
        while True:
            j = input("Kérem adja meg a járat számát, vagy 0-val kiléphet:")
            if j == "0":
                return
            ut=self.legitarsasag.checkid(j)
            if ut == -1:
                print("Ez a járat azonosító nem létezik!")
            else:
                break
        print("A repülőgépen két utasosztály érhető el:")
        print(f"Első osztály ár : {self.legitarsasag.jaratok[ut].ar1}")
        print(f"Másodosztály ár : {self.legitarsasag.jaratok[ut].ar2}")

        while True:
            o = input(f"Melyik osztályra szeretne jegyet vásárolni ? (1/2):")
            if o=="1" or o=="2":
                break
        utas=input("Kérem adja meg a nevét a foglaláshoz:")
        self.foglalasok.append(JegyFoglalas(self.legitarsasag.jaratok[ut],o, utas))
        print(f"Köszönöm, {utas}, a jegye lefoglalásra került a {j} azonosíójú repülőjáratra, {o} osztályra!")
    def menurendszer(self):
        while True:
            cls()
            print(L)
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
                L.jaratok_lista()
                print()
                input("Enter a visszalépéshez")
            elif c == 2:
                cls()
                f.foglalas_listazas()
                print()
                input("Enter a visszalépéshez")
            elif c == 3:
                cls()
                f.foglalas()
                print()
                input("Enter a visszalépéshez")

        pass


L=LegiTarsasag("                                 *********** MRT_Légitársaság *********")

f=FoglaloRendszer(L)
f.menurendszer()



import os.path

from BelfoldiJarat import Belfoldijarat
from NemzetkoziJarat import NemzetkoziJarat
from JegyFoglalas import JegyFoglalas
from LegiTarsasag import LegiTarsasag
from os import system, name
from datetime import datetime
import csv


def cls():
    if name == 'nt':
        system('cls')
    else:
        system('clear')





class FoglaloRendszer:
    _Mentesfajlnev="Repuloter.csv"
    def __init__(self,userid,usernev):
        self.userid = userid
        self.usernev = usernev
        self.foglalasok = []
        self.legitarsasag = []
        self.fn = 202500000
        self.adat_betoltes()
    def __add__(self, other):
        self.legitarsasag.append(other)

    def adat_betoltes(self):
        if os.path.exists(FoglaloRendszer._Mentesfajlnev):
            with open(FoglaloRendszer._Mentesfajlnev, mode='r') as file:
                csvfile=csv.reader(file)
                for lines in csvfile:
                    pass

        return

    def adatmentes_fileba(self):
        with open(FoglaloRendszer._Mentesfajlnev, mode='w') as file:
            for i in self.legitarsasag:
                pass

        return

    def fejlec(self):
        cls()
        print(f"Bejelentkezett felhasználó:{self.usernev}                       dátum:{datetime.now()}")
        print()
        print("                                                  Budapesti Repülőtér ")


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

    def foglalas_check(self,id):
        for i in range(len(self.foglalasok)):
            if self.foglalasok[i].id==id:
                return i
        return -1

    def foglalas_feltoltes(self):
        self.foglalasok.append(JegyFoglalas(self,0,0))
        self.foglalasok.append(JegyFoglalas(self,1,0))

    def foglalas_listazas(self):
        self.fejlec()
        print(" ------------------------FOGLALÁSOK LISTÁZÁSA----------------------------")
        for i in self.foglalasok:
            if i.userid==self.userid:
                print(f"{i.id} {i.ltarsasag}  {i.jarat.id} {i.jarat.celallomas} {i.jarat.indulasiido}")

    def foglalas(self):
        self.fejlec()
        print("------------Jegy Foglalás-------------")
        print()
        while True:
            j = input("Kérem adja meg a járat számát, vagy 0-val kiléphet:")
            if j == "0":
                return
            for ltr in range(len(self.legitarsasag)):
                ut = self.legitarsasag[ltr].checkid(j)
                if ut >=0:
                    break
            if ut == -1:
                print("Ez a járat azonosító nem létezik!")
            else:
                break
        print(f"A járatra a jegyár: {self.legitarsasag[ltr].jaratok[ut].ar}")

        self.foglalasok.append(JegyFoglalas(self,ltr,ut))
        print(f"Köszönöm, a jegye lefoglalásra került a {j} azonosíójú repülőjáratra!")
        print(f"A jegy azonosítószáma: {self.foglalasok[-1].id}")

    def lemondas(self):
        self.fejlec()
        print("-------------- Foglalás lemondása ----------------")
        print()
        while True:
            l=int(input("Kérem adja meg a lemondandó foglalás azonosítóját, vagy 0-val kiléphet:"))
            if l==0:
                break
            else:
                foglalas=self.foglalas_check(l)
                if foglalas==-1:
                    print("Ilyen azonosítószámú foglalás nem létezik!")
                else:
                    print("A lemondando foglalas:")
                    print(self.foglalasok[foglalas])
                    print()
                    while True:
                        v = (input("Biztosan lemondja ezt a helyfoglalást ? (i/n)")).upper()
                        if v == "I":
                            del self.foglalasok[foglalas]
                            print("A foglalás lemondva")
                            input("Enter a visszalépéshez")
                            return
                        elif v == "N":
                            break





    def menurendszer(self):
        while True:
            self.fejlec()
            print()
            print("                                        1 .... Járatok listázása")
            print("                                        2 .... Jegyfoglalások listázása")
            print("                                        3 .... Jegyfoglalás egy járatra")
            print("                                        4 .... Jegyfoglalás lemondása")
            print("                                        5 .... Kilépés")

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
            elif c == 4:
                cls()
                self.lemondas()
                print()
                input("Enter a visszalépéshez")
            elif c == 5:
                break
        pass




f=FoglaloRendszer(1234,"Mekk Elek")


L=LegiTarsasag("MRT Légitársaság")
L.jaratok = Belfoldijarat('BE456', 'A1', '2025.05.25 10:00', 'Debrecen', 96,  20000)
L.jaratok = Belfoldijarat('BE460', 'A2', '2025.05.26 10:00', 'Szeged', 64, 30000)
L.jaratok = NemzetkoziJarat('NE401', 'B1', '2025.05.24 11:00', 'Berlin', 100, 40000)
L.jaratok = NemzetkoziJarat('NE560', 'B2', '2025.05.26 12:00', 'Amszterdam', 120,  50000)
L.jaratok = NemzetkoziJarat('NE332', 'B3', '2025.05.27 13:00', 'Cyprus', 140, 60000)

f + L

L2=LegiTarsasag("Ryanair")
L2.jaratok = NemzetkoziJarat('RNE346', 'C', '2025.06.01 12:00', 'Amszterdam', 110, 70000)


f + L2



f.foglalas_feltoltes()
f.menurendszer()



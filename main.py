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
    def __init__(self,userid,usernev):
        self.userid = userid
        self.usernev = usernev
        self.celallomasok = []
        self.foglalasok = []
        self.legitarsasag = []
        self.fn = 202500000         # jegy azonosító kezdőérték
    def __add__(self, other):
        self.legitarsasag.append(other)
        for i in other.jaratok:
            if not (i.celallomas in self.celallomasok):
                self.celallomasok.append(i.celallomas)

    def fejlec(self):
        cls()
        print(f"Bejelentkezett felhasználó:{self.usernev}                                     dátum:{datetime.now()}")
        print()
        print("                                                  Budapesti Repülőtér ")


    def tarsasagok_jaratok(self):
        print(
            "Sorszám   Légitársaság         Típus           Azonosító        Célállomás              indulási idő          Terminál           Ár")
        print(
            "--------  ------------         -----           ---------        ----------              ------------          --------         ---------")
        ljarat=[]
        t=0
        for j in range(len(self.legitarsasag)):
            lt = self.legitarsasag[j]
            for i in range(len(lt.jaratok)):
                ljarat.append((j,i))
                t +=1
                s = "  "+str(t)
                for z in range(10 - len(s)):
                   s += " "
                s += lt.nev
                for z in range(20 - len(s)):
                   s += " "
                for z in range(30-len(s)):
                   s+=" "
                s +=lt.jaratok[i].jaratadatok()
                print(s)
        return ljarat
    def foglalas_check(self,id):
        for i in range(len(self.foglalasok)):
            if self.foglalasok[i].id==id:
                return i
        return -1

    def foglalas_feltoltes(self):
        self.foglalasok.append(JegyFoglalas(self,0,0))
        self.foglalasok.append(JegyFoglalas(self,1,0))
        self.foglalasok.append(JegyFoglalas(self,0,1))
        self.foglalasok.append(JegyFoglalas(self,0,2))
        self.foglalasok.append(JegyFoglalas(self,0,3))
        self.foglalasok.append(JegyFoglalas(self,0,2))


    def foglalas_listazas(self):
        self.fejlec()
        print(" ------------------------------------------FOGLALÁSOK LISTÁZÁSA------------------------------------------")
        j = 0
        for i in self.foglalasok:
            j += 1
            if i.userid==self.userid:
                print(f"{j} {i.id} {i.ltarsasag}  {i.jarat.id} {i.jarat.celallomas} {i.jarat.indulasiido}")
        return j


    def I_N_bekeres(self,szoveg):
        while True:
                valasz = (input(szoveg)).upper()
                if valasz == "I":
                    return True
                elif valasz == "N":
                    return False


    def szam_bekeres(self,szoveg,also_hatar,felso_hatar):
        while True:
            try:
                valasz = int(input(szoveg))
                if valasz >= also_hatar and valasz <= felso_hatar:
                    break
            except ValueError as e:
                pass
        return valasz

    def foglalas(self):
        def celallomas_lista():
            j=0
            s=""
            for i in range(len(self.celallomasok)):
                s=s+f"{i+1}:{self.celallomasok[i]}  "
                j += 1
                if j ==10:
                    j = 0
                    print(s)
                    s=""
            print(s)

        def jaratkereses(celallomas):
            s=""
            talalat=[]
            t=0
            for i in range(len(self.legitarsasag)):
                for j in range(len(self.legitarsasag[i].jaratok)):
                    if self.legitarsasag[i].jaratok[j].celallomas==celallomas:
                        s=""
                        t += 1
                        s += str(t)
                        for z in range(3 - len(str(t))):
                            s += " "
                        s += self.legitarsasag[i].nev
                        for z in range(20 - len(s)):
                            s += " "
                        s += self.legitarsasag[i].jaratok[j].jaratadatok()
                        print(s)
                        talalat.append((i,j))
            return talalat


        while True:
            cls()
            self.fejlec()
            print("--------------------------------------------------Jegy Foglalás-------------------------------------------")
            print("                                 1: A legközelebb induló járatok valamelyikére foglalás")
            print("                                 2: Járat keresése célállomás szerint")
            print("                                 3: Visszalépés a főmenübe")

            j = input("Kérem válasszon a menüpontokból:")
            if j == "3":
                return
            elif j == "1":
                cls()
                print("--------------------------------------------------Jegy Foglalás-------------------------------------------")
                print()
                ljaratok = self.tarsasagok_jaratok()
                print()
                k=self.szam_bekeres("Adja meg a járat sorszámát, amire jegyet kíván foglalni, vagy 0-val kiléphet:",0,len(ljaratok))
                if k==0:
                    return
                valasztott=ljaratok[k-1]
                print("-----------------------------------")
                print("A kiválasztott járat:")
                print(self.legitarsasag[valasztott[0]].jaratok[valasztott[1]].jaratadatok())
                if self.I_N_bekeres("Erre a kiválasztott repülőjáratra biztosan jegyet kíván foglalni ? (I/N)"):
                    self.foglalasok.append(JegyFoglalas(self,valasztott[0],valasztott[1]))
                    print("A jegyét lefoglaltuk!")
                    input("Enter")
            elif j == "2":
                print("A jelenlegi járatokkal elérhető célállomások:")
                print()
                celallomas_lista()
                print()
                valasz = self.szam_bekeres("Kérem adja meg a célállomás sorszámát, vagy 0-val kiléphet:",0,len(self.celallomasok)+1,)
                if valasz == 0:
                    return
                else:
                    talalat = jaratkereses(self.celallomasok[valasz-1])
                    if len(talalat)>1:
                        sorszam=self.szam_bekeres("Kérem adja meg a járat sorszámát:",1,len(talalat))
                        vjarat = talalat[sorszam-1]     #a legitarsasag hányadik, a járatokbol hányadik
                    else:
                        vjarat = talalat[0]
                    print()
                    if self.I_N_bekeres("Jegyet kíván foglalni erre a járatra ? (I/N):"):
                        self.foglalasok.append(JegyFoglalas(self, vjarat[0],vjarat[1]))   #átadva: légitársaság száma,
                        print()
                        print(f"A járatra a jegyét lefoglaltuk!")
                        input("Enter")
                    else:
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
        while True:
            v = (input("Megvásárolja ezt a jegyet ? (i/n)")).upper()
            if v == "I" or v == "N":
                break
        if v == "I":
            self.foglalasok.append(JegyFoglalas(self,ltr,ut))
            print(f"Köszönöm, a jegye lefoglalásra került a {j} azonosíójú repülőjáratra!")
            print(f"A jegy azonosítószáma: {self.foglalasok[-1].id}")
        else:
            return

    def lemondas(self):
        self.fejlec()
        print("-------------- Foglalás lemondása ----------------")
        print()
        db=self.foglalas_listazas()
        print()
        while True:
            l=self.szam_bekeres("Kérem adja meg a lemondandó foglalás sorszámát, vagy 0-val kiléphet:",0,db)
            print()
            if l==0:
                break
            else:
                print("A lemondando foglalas:")
                print(
                    "Légitársaság         Típus           Azonosító        Célállomás              indulási idő          Terminál           Ár")
                print(
                    "------------         -----           ---------        ----------              ------------          --------         ---------")
                s = self.foglalasok[l-1].ltarsasag
                for sz in range(20-len(s)):
                    s+=" "
                s+=self.foglalasok[l-1].jarat.jaratadatok()
                print(s)
                print()
                if self.I_N_bekeres("Biztosan lemondja ezt a helyfoglalást ? (i/n):"):
                   print(f"A visszautalt pénzösszeg (jegyár): {self.foglalasok[l-1].jarat.ar}  Huf")
                   del self.foglalasok[l-1]
                   print("A foglalás lemondva!")
                   print()
                   input("Enter a visszalépéshez")
                   return
                else:
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
            try:
                c = int(input("Válassz egy menüpontot:"))
            except ValueError as v:
                c=0
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
            elif c == 4:
                cls()
                self.lemondas()
            elif c == 5:
                break
            else:
                pass
        pass




f=FoglaloRendszer(1234,"Mekk Elek")


L=LegiTarsasag("MRT Légitársaság")
L.jaratok = Belfoldijarat('BE456', 'A1', datetime(2025,6,20, 10,0), 'Debrecen', 96,  20000)
L.jaratok = Belfoldijarat('BE460', 'A2', datetime(2025,6,13,10,0), 'Szeged', 64, 30000)
L.jaratok = NemzetkoziJarat('NE401', 'B1', datetime(2025,6,25,11,0), 'Berlin', 100, 40000)
L.jaratok = NemzetkoziJarat('NE560', 'B2', datetime(2025,6,30,12,0), 'Amszterdam', 120,  50000)
L.jaratok = NemzetkoziJarat('NE332', 'B3', datetime(2025,6,26,15,0), 'Cyprus', 140, 60000)

f + L

L2=LegiTarsasag("Ryanair")
L2.jaratok = NemzetkoziJarat('RNE346', 'C', datetime(2025,6,28,10,0), 'Amszterdam', 110, 70000)


f + L2



f.foglalas_feltoltes()
f.menurendszer()



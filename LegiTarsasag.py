from BelfoldiJarat import Belfoldijarat
from NemzetkoziJarat import NemzetkoziJarat

class LegiTarsasag:
    def __init__(self,nev):
        self._jaratok=[]
        self._nev = nev
        self.adatfeltoles()



    def __str__(self):
        return self._nev


    def jaratok_lista(self):
        print(self._nev)
        print()
        print("--------------JÁRATOK------------")
        print("Típus           Azonosító        Celallomas              indulási idő          Terminál")
        print("-----           ---------        ----------              ------------          --------")
        for i in self._jaratok:
            s = ""
            s+=i.jarattipus
            for j in range(20-len(s)):  # a 25.poziciotol jön az id
                s+=" "
            s+=i.id
            for j in range(35-len(s)): # 35-től a célállomás jön
                s+=" "
            s+=i.celallomas
            for j in range(60-len(s)): # 50-től az indulási idő
                s+=" "
            s+=i.indulasiido
            for j in range(80-len(s)): # 60-tól a terminál
                s+=" "
            s+=i.terminal
            print(s)


    @property
    def jaratok(self):
        return self._jaratok

    @jaratok.setter
    def jaratok(self,uj_jarat):
        self._jaratok.append(uj_jarat)

    def adatfeltoles(self):
        self.jaratok = Belfoldijarat('BE456','A1','2025.05.25 10:00','Debrecen',24,96,30000,20000)
        self.jaratok = Belfoldijarat('BE460','A2','2025.05.26 10:00','Szeged',16,64,30000,20000)
        self.jaratok = NemzetkoziJarat('NE401','B1','2025.05.24 11:00','Berlin',24,96,40000,30000)
        self.jaratok = NemzetkoziJarat('NE560','B2','2025.05.26 12:00','Amszterdam',24,96,50000,40000)
        self.jaratok = NemzetkoziJarat('NE332','B3','2025.05.27 13:00','Cyprus',24,96,80000,60000)

    def checkid(self,id):
        for i in range(len(self._jaratok)):
            if id==self.jaratok[i].id:
                return i
        return -1

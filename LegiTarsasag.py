
class LegiTarsasag:
    def __init__(self,nev):
        self._jaratok=[]
        self._nev = nev


    def __str__(self):
        return self._nev


    @property
    def nev(self):
        return self._nev

    @property
    def jaratok(self):
        return self._jaratok

    @jaratok.setter
    def jaratok(self,uj_jarat):
        self._jaratok.append(uj_jarat)


    def checkid(self,id):
        for i in range(len(self._jaratok)):
            if id==self.jaratok[i].id:
                return i
        return -1

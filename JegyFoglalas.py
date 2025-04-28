class JegyFoglalas:
    def __init__(self,frobj,ltarsasag,jarat):
        self._id = frobj.fn           # jegy azonosítószám a FoglaloRendszer objektumban
        frobj.fn += 1
        self._ltarsasag = frobj.legitarsasag[ltarsasag].nev
        self._jarat = frobj.legitarsasag[ltarsasag].jaratok[jarat]
        self._userid = frobj.userid

    def __str__(self):
        s = self._ltarsasag+"   "+self._jarat.id
        return s
    @property
    def id(self):
        return self._id
    @property
    def ltarsasag(self):
        return self._ltarsasag
    @property
    def jarat(self):
        return self._jarat

    @property
    def userid(self):
        return self._userid





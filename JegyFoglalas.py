class JegyFoglalas:
    def __init__(self,ltarsasag_nev,jarat,osztaly,utas):
        self._ltarsasag = ltarsasag_nev
        self._jarat = jarat
        self._osztaly = osztaly
        self._utas = utas


    @property
    def ltarsasag(self):
        return self._ltarsasag
    @property
    def jarat(self):
        return self._jarat

    @property
    def osztaly(self):
        return self._osztaly

    @property
    def utas(self):
        return self._utas




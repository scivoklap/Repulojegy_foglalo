class JegyFoglalas:
    def __init__(self,jarat,osztaly,utas):
        self._jarat = jarat
        self._osztaly = osztaly
        self._utas = utas

    @property
    def jarat(self):
        return self._jarat

    @property
    def osztaly(self):
        return self._osztaly

    @property
    def utas(self):
        return self._utas




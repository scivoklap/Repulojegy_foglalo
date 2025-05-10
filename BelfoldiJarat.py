from Jarat import Jarat

class Belfoldijarat(Jarat):
    def __init__(self,id,terminal,indulasiido,celallomas,ulohelyek,ar = 10000):
        super().__init__(id,terminal,indulasiido,celallomas,ar)
        self._ulohelyek = ulohelyek
        self._ar = ar
        self._jarattipus = "Belföldi"



    @property
    def id(self):
        return self._id

    @property
    def terminal(self):
        return self._terminal

    @terminal.setter
    def terminal(self, new_terminal):
        self._terminal = new_terminal

    @property
    def indulasiido(self):
        return self._indulasiido

    @indulasiido.setter
    def indulasiido(self, new_starttime):
        self._indulasiido = new_starttime


    @property
    def celallomas(self):
        return self._celallomas


    @celallomas.setter
    def celallomas(self, new_target):
        self._celallomas = new_target

    @property
    def ar(self):
        return self._ar

    @ar.setter
    def ar(self,uj_ar):
        self._ar = uj_ar


    @property
    def jarattipus(self):
        return self._jarattipus

    def ulohelyfoglalas(self):
        if self._ulohelyek>0:
            self._ulohelyek -= 1
            return True
        else:
            return False

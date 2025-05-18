from Jarat import Jarat


class NemzetkoziJarat(Jarat):
    def __init__(self, id, terminal, indulasiido, celallomas, ulohelyek, ar = 60000):
        super().__init__(id, terminal, indulasiido, celallomas,ar)
        self._ulohelyek = ulohelyek
        self._ar = ar
        self._jarattipus = "Nemzetközi"

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
    def ar(self, uj_ar):
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


    def jaratadatok(self):
        s = ''
        s += self._jarattipus
        for z in range(20 - len(s)):  # id
            s += " "
        s += self._id
        for z in range(35 - len(s)):  # célállomás
            s += " "
        s += self._celallomas
        for z in range(56 - len(s)):  # indulási idő
            s += " "
        s += str(self._indulasiido)
        for z in range(85 - len(s)):  # terminál
            s += " "
        s += self._terminal
        for z in range(100 - len(s)):  # ár
            s += " "
        s += str(self._ar)
        return s
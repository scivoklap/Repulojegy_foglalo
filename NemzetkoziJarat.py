from Jarat import Jarat


class NemzetkoziJarat(Jarat):
    def __init__(self, id, terminal, indulasiido, celallomas, ulohelyek1, ulohelyek2, ar1, ar2):
        super().__init__(id, terminal, indulasiido, celallomas)
        self._ulohelyek1 = ulohelyek1
        self._ulohelyek2 = ulohelyek2
        self._ar1 = ar1
        self._ar2 = ar2
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
    def ar1(self):
        return self._ar1

    @ar1.setter
    def ar1(self, uj_ar):
        self._ar1 = uj_ar

    @property
    def ar2(self):
        return self._ar2

    @ar2.setter
    def ar2(self, uj_ar):
        self._ar2 = uj_ar

    @property
    def jarattipus(self):
        return self._jarattipus

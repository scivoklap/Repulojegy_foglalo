from abc import ABC,abstractmethod
class Jarat(ABC):

    def __init__(self,id,terminal,indulasiido,celallomas,ar):
        self._id = id
        self._terminal = terminal
        self._indulasiido = indulasiido
        self._celallomas = celallomas
        self._ar = ar

    @abstractmethod
    def id(self):
        pass

    @abstractmethod
    def terminal(self):
        pass

    @abstractmethod
    def terminal(self,new_terminal):
        pass

    @abstractmethod
    def indulasiido(self):
        pass

    @abstractmethod
    def indulasiido(self,new_starttime):
        pass

    @abstractmethod
    def celallomas(self):
        pass

    @abstractmethod
    def celallomas(self,new_targer):
        pass

    @abstractmethod
    def ar(self,new_ar):
        pass
    @abstractmethod
    def ar(self):
        pass

    @abstractmethod
    def jaratadatok(self):
        pass

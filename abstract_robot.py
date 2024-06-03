from abc import ABC, abstractmethod

class AbstractRobot(ABC):
    @abstractmethod
    def move(self, direction, distance):
        pass

    @abstractmethod
    def pegar_bola(self):
        pass

    @abstractmethod
    def return_to_base(self):
        pass

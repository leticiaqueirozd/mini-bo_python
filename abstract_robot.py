from abc import ABC, abstractmethod

class AbstractRobot(ABC):
    LIMIT = 10

    def __init__(self):
        self.__connection = False
        self.__inside_rift = True
        self.__has_ball = False
        self.__position = [0, 0]

    @abstractmethod
    def andar_frente(self) -> None:
        pass

    @abstractmethod
    def andar_tras(self) -> None:
        pass

    @abstractmethod
    def andar_direita(self) -> None:
        pass

    @abstractmethod
    def andar_esquerda(self) -> None:
        pass

    @abstractmethod
    def loca_atual(self) -> list:
        pass

    @abstractmethod
    def conectar(self) -> bool:
        pass

    @abstractmethod
    def desconectar(self) -> None:
        pass

    @abstractmethod
    def pegar_bola(self) -> bool:
        pass

    @abstractmethod
    def voltar_base(self) -> None:
        pass

    @abstractmethod
    def balls_locations(self) -> list:
        pass

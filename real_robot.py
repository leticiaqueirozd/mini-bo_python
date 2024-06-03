from random import randint
from abstract_robot import AbstractRobot

class RealRobot(AbstractRobot):
    def __init__(self):
        super().__init__()
        self.connected = False
        self.position = [0, 0]

    def move(self, direction, distance):
        if not self.connected:
            raise ConnectionError("O robô não está conectado")
        if abs(distance) > 10:
            raise ValueError("Distância de movimento excede o limite de 10")
        if direction not in ["frente", "trás", "direita", "esquerda"]:
            raise ValueError("Direção de movimento inválida")

        if direction == "frente":
            self.position[1] += distance
        elif direction == "trás":
            self.position[1] -= distance
        elif direction == "direita":
            self.position[0] += distance
        elif direction == "esquerda":
            self.position[0] -= distance

        print(f"Robô moveu {distance} unidades para {direction}. Nova posição: {self.position}")

    def pegar_bola(self):
        if not self.connected:
            raise ConnectionError("O robô não está conectado")
        print("Bola capturada")

    def return_to_base(self):
        if not self.connected:
            raise ConnectionError("O robô não está conectado")
        if self.position != [0, 0]:
            raise ValueError("O robô deve estar na base para retornar")
        print("Robô retornou à base")

    def conectar(self):
        if not self.connected:
            if randint(1, 10) <= 9:
                self.connected = True
                print("Robô conectado")
            else:
                print("Falha ao conectar o robô")
        else:
            print("O robô já está conectado")

    def desconectar(self):
        if self.connected:
            self.connected = False
            print("Robô desconectado")
        else:
            print("O robô já está desconectado")

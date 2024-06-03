from abstract_robot import AbstractRobot

class TestRobot(AbstractRobot):
    def __init__(self):
        super().__init__()
        self.position = [0, 0]

    def move(self, direction, distance):
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

        print(f"Robô de teste moveu {distance} unidades para {direction}. Nova posição: {self.position}")

    def pegar_bola(self):
        print("Bola capturada")

    def return_to_base(self):
        if self.position != [0, 0]:
            raise ValueError("O robô de teste deve estar na base para retornar")
        print("Robô de teste retornou à base")

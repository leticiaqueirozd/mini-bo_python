from random import randint
from abstract_robot import AbstractRobot

class TestRobot(AbstractRobot):
    def andar_frente(self) -> None:
        if self._AbstractRobot__connection:
            if self._AbstractRobot__inside_rift:
                print('Robô real andando para frente')
                self._AbstractRobot__position[0] += 1
                if self._AbstractRobot__position[0] > self.LIMIT:
                    self._AbstractRobot__inside_rift = False
                    raise SystemError('O robô caiu no abismo')
            else:
                raise SystemError('Robô real está fora de funcionamento')
        else:
            raise ConnectionError('Robô real não conectado')

    def andar_tras(self) -> None:
        if self._AbstractRobot__connection:
            if self._AbstractRobot__inside_rift:
                print('Robô real andando para trás')
                self._AbstractRobot__position[0] -= 1
                if self._AbstractRobot__position[0] < self.LIMIT * -1:
                    self._AbstractRobot__inside_rift = False
                    raise SystemError('O robô caiu no abismo')
            else:
                raise SystemError('Robô real está fora de funcionamento')
        else:
            raise ConnectionError('Robô real não conectado')

    def andar_direita(self) -> None:
        if self._AbstractRobot__connection:
            if self._AbstractRobot__inside_rift:
                print('Robô real andando para direita')
                self._AbstractRobot__position[1] += 1
                if self._AbstractRobot__position[1] > self.LIMIT:
                    self._AbstractRobot__inside_rift = False
                    raise SystemError('O robô caiu no abismo')
            else:
                raise SystemError('Robô real está fora de funcionamento')
        else:
            raise ConnectionError('Robô real não conectado')

    def andar_esquerda(self) -> None:
        if self._AbstractRobot__connection:
            if self._AbstractRobot__inside_rift:
                print('Robô real andando para esquerda')
                self._AbstractRobot__position[1] -= 1
                if self._AbstractRobot__position[1] < self.LIMIT * -1:
                    self._AbstractRobot__inside_rift = False
                    raise SystemError('O robô caiu no abismo')
            else:
                raise SystemError('Robô real está fora de funcionamento')
        else:
            raise ConnectionError('Robô real não conectado')

    def loca_atual(self) -> list:
        if self._AbstractRobot__connection:
            return self._AbstractRobot__position
        else:
            raise ConnectionError('Robô real não conectado')

    def conectar(self) -> bool:
        if not self._AbstractRobot__connection:
            probability = randint(0, 11)
            if probability == 1 or probability == 2:
                return False
            else:
                self._AbstractRobot__connection = True
                return True
        else:
            print('Robô real já conectado anteriormente')
            return True

    def desconectar(self) -> None:
        self._AbstractRobot__connection = False

    def pegar_bola(self) -> bool:
        has_ball = False
        count = 0
        if self._AbstractRobot__connection:
            if self._AbstractRobot__inside_rift:
                if not self._AbstractRobot__has_ball:
                    if len(self._AbstractRobot__balls_locations) > 0:
                        for i in self._AbstractRobot__balls_locations:
                            if i[0] == self._AbstractRobot__position[0] and i[1] == self._AbstractRobot__position[1]:
                                self._AbstractRobot__balls_locations.pop(count)
                                has_ball = True
                            count += 1

                        if has_ball:
                            self._AbstractRobot__has_ball = True
                            print('Bola capturada')
                            return True
                        else:
                            print('Não existe bola')
                            return False
                    else:
                        print('Não existe mais bola')
                        return False
                else:
                    raise SystemError('Robô tentou capturar a bola mas já tinha uma bola')
            else:
                raise SystemError('Robô real está fora de funcionamento')
        else:
            raise ConnectionError('Robô real não conectado')

    def voltar_base(self) -> None:
        if self._AbstractRobot__connection:
            if self._AbstractRobot__inside_rift:
                if self._AbstractRobot__has_ball:
                    self._AbstractRobot__position = [0, 0]
                    self._AbstractRobot__has_ball = False
                    print('Voltou pra base e deixou a bola')
                    if len(self._AbstractRobot__balls_locations) == 0:
                        print('Todas as bolas foram capturadas, você venceu')
                else:
                    raise SystemError('Robô real não possui bola, não pode voltar automaticamente para a base')
            else:
                raise SystemError('Robô real está fora de funcionamento')
        else:
            raise ConnectionError('Robô real não conectado')

    def balls_locations(self) -> list:
        if self._AbstractRobot__connection:
            if self._AbstractRobot__inside_rift:
                return self._AbstractRobot__balls_locations
            else:
                raise SystemError('Robô real está fora de funcionamento')
        else:
            raise ConnectionError('Robô real não conectado')
from random import randint


LIMIT = 10


class MiniBo:

    def __init__(self, number_balls: int = 2):
        self.__position = [0, 0]
        self.__connection = False
        self.__inside_rift = True
        self.__has_ball = False
        self.__balls_locations = []
        for i in range(number_balls):
            position1 = randint(-10, 11)
            position2 = randint(-10, 11)
            self.__balls_locations.append([position1, position2])

    def walk_forward(self) -> None:
        if self.__connection:
            
            if self.__inside_rift:
                print('Robô andando para frente')
                self.__position[0] += 1

                if self.__position[0] > LIMIT:
                    self.__inside_rift = False
                    raise SystemError('O robo caiu no abismo')
            
            else:
                raise SystemError('Robô está fora de funcionamento')
        
        else:
            raise ConnectionError('Robô não conectado')

    def walk_backwards(self) -> None:
        if self.__connection:

            if self.__inside_rift:
                print("Robô andando para trás")
                self.__position[0] -= 1
                
                if self.__position[0] < LIMIT * -1:
                    self.__inside_rift = False
                    raise SystemError('O robo caiu no abismo')
            
            else:
                raise SystemError('Robô está fora de funcionamento')
    
        else:
            raise ConnectionError('Robô não conectado')

    def walk_right(self) -> None:
        if self.__connection:

            if self.__inside_rift:
                print("Robô andando para Direita")
                self.__position[1] += 1
                
                if self.__position[1] > LIMIT:
                    self.__inside_rift = False
                    raise SystemError('O robo caiu no abismo')
                
            else:
                raise SystemError('Robô está fora de funcionamento')
    
        else:
            raise ConnectionError('Robô não conectado')

    def walk_left(self):
        if self.__connection:

            if self.__inside_rift:
                print("Robô andando para Esquerda")
                self.__position[1] -= 1
                
                if self.__position[1] < LIMIT * -1:
                    self.__inside_rift = False
                    raise SystemError('O robo caiu no abismo')
            
            else:
                raise SystemError('Robô está fora de funcionamento')
    
        else:
            raise ConnectionError('Robô não conectado')
        
    def location(self) -> list:
        if self.__connection:
            return self.__position
        else:
            raise ConnectionError('Robô não conectado')

    def connect(self) -> bool:
        if not self.__connection:
            probability = randint(0, 11)
            if probability == 1 or probability == 2:
                return False
            else:
                self.__connection = True
                return True
        else:
            print('Robô já conectado anteriormente')
            return True

    def disconnect(self):
        self.__connection = False

    def get_ball(self) -> bool:
        has_ball = False
        count = 0
        if self.__connection:

            if self.__inside_rift:

                if not self.__has_ball:

                    if len(self.__balls_locations) > 0:

                        for i in self.__balls_locations:
                            if i[0] == self.__position[0] and i[1] == self.__position[1]:
                                self.__balls_locations.pop(count)
                                has_ball = True

                            count += 1

                        if has_ball:
                            self.__has_ball = True
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
                raise SystemError('Robô está fora de funcionamento')

        else:
            raise ConnectionError('Robô não conectado')

    def back_base(self) -> None:
        if self.__connection:
            if self.__inside_rift:
                if self.__has_ball:
                    self.__position = [0, 0]
                    self.__has_ball = False
                    print('Voltou pra base e deixou a bola')
                    if len(self.__balls_locations) == 0:
                        print('Todas as bolas foram capturadas você venceu')

                else:
                    raise SystemError('Robô não possui bola não pode voltar automaticamente para a base')
            else:
                raise SystemError('Robô está fora de funcionamento')
        else:
            raise ConnectionError('Robô não conectado')

    def ball_locations(self) -> list:
        if self.__connection:
            if self.__inside_rift:
                return self.__balls_locations
            else:
                raise SystemError('Robô está fora de funcionamento')
        else:
            raise ConnectionError('Robô não conectado')

if __name__ == '__main__':
    robot = MiniBo()
    print()
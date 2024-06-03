import time

from real_robot import RealRobot
from test_robot import TestRobot

system = True
robot = None
while system:
    if robot is None:

        print("****MENU ESCOLHA ROBÔ****\n"
              "[1] Robô real\n"
              "[2] Robô de teste\n"
              "Para sair digite uma letra:\n")

        choice = input()

        if choice.isnumeric():
            choice = int(choice)
            if choice == 1:
                robot = RealRobot()
            elif choice == 2:
                robot = TestRobot()
            else:
                print('Escolha invalida')

        else:
            print('Saindo do Simulador')
            system = False

    else:
        print("****MENU CONTROLE DO ROBÔ****\n"
              "[1] Conectar robô\n"
              "[2] Andar para frente\n"
              "[3] Andar para trás\n"
              "[4] Andar para direita\n"
              "[5] Andar para esquerda\n"
              "[6] Localização atual\n"
              "[7] Desconectar\n"
              "[8] Pegar bola\n"
              "[9] Voltar base\n"
              "[0] Localização das bolas\n"
              "Para sair digite uma letra:\n")

        choice = input()
        if choice.isnumeric():
            choice = int(choice)

            if choice == 1:

                if robot.conectar():
                    print("Robô conectado\n")

                else:
                    print('Conexão com o robô falhou\n')

            elif choice == 2:
                robot.andar_frente()

            elif choice == 3:
                robot.andar_tras()

            elif choice == 4:
                robot.andar_direita()

            elif choice == 5:
                robot.andar_esquerda()

            elif choice == 6:
                print(robot.loca_atual(), '\n')

            elif choice == 7:
                robot.desconectar()

            elif choice == 8:

                if robot.pegar_bola():
                    print("Bola capturada\n")

                else:
                    print("Não capturada bola\n")

            elif choice == 9:
                robot.voltar_base()

            elif choice == 0:
                print(robot.loca_bolas(), '\n')

            else:
                print('Escolha invalida')

        else:
            print('Saindo do Simulador')
            system = False

        time.sleep(0.6)
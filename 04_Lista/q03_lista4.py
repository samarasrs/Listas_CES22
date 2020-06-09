from __future__ import generators
from abc import ABC, abstractmethod

class Veiculos():
    @abstractmethod
    def factory(tipo, motor):
        if tipo == 'automovel':
            return Automovel(motor)
        elif tipo == 'caminhao':
            return Caminhao(motor)
        else:
            raise NameError(" Tipo de veiculo  invalido. Veiculos disponiveis: automovel e caminhao")

    def set_motor(self, motor):
        if motor == 'eletrico':
            Motor_eletrico()

        elif motor == 'combustao':
            Motor_combustao()

        elif motor == 'hibrido':
            Motor_hibrido()

        else:
            raise NameError(" Tipo do motor invalido. Motores disponiveis: eletrico, combustao ou hibrido")

class Automovel(Veiculos):
    def __init__(self, motor):
        self.set_motor(motor)
        self.motor = motor

    def descricao(self):
        print("Automovel como motor", self.motor)


class Caminhao(Veiculos):
    def __init__(self, motor):
        self.set_motor(motor)
        self.motor = motor

    def descricao(self):
        print("Caminhao como motor", self.motor)

class Motor():
    def descricao(self):
        pass


class Motor_eletrico(Motor):
    def descricao(self):
        print("O motor é elétrico")



class Motor_combustao(Motor):
    def descricao(self):
        print("O motor é a combustão")


class Motor_hibrido(Motor):
    def descricao(self):
        print("O motor é híbrido")




car = Veiculos.factory('automovel', 'eletrico')
car.descricao()

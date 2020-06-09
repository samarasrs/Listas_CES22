# Design Pattern Brigde;

class Veiculos():
    def __init__(self, motor):
        self.set_motor(motor)

    def set_motor(self, motor):
        if motor == 'eletrico':
            Motor_eletrico()

        elif motor == 'combustao':
            Motor_combustao()

        elif motor == 'hibrido':
            Motor_hibrido()

        else:
            raise NameError(" Tipo do motor invalido. Motores disponiveis: eletrico, combustao ou hibrido")


class Automoveis(Veiculos):
    def __init__(self, motor):
        super.__init__(motor)


class Caminhoes(Veiculos):
    def __init__(self, motor):
        super.__init__(motor)


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

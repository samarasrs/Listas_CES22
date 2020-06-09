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


class Automoveis(Veiculos):
    def __init__(self, motor):
        super.__init__(motor)
        self.tipo = motor


class Caminhoes(Veiculos):
    def __init__(self, motor):
        super.__init__(motor)


class Motor():
    pass


class Motor_eletrico(Motor):
    pass


class Motor_combustao(Motor):
    pass


class Motor_hibrido(Motor):
    pass

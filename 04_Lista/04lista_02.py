

class Ingredientes():
    def get_descricao(self):
        return self.__class__.__name__

    def get_preco_total(self):
        return self.__class__.cost

class Massa(Ingredientes):
    cost = 1.00

class Decorador(Ingredientes):
    def __init__(self, ingrediente):
        self.ingrediente = ingrediente

    def get_descricao(self):
        return self.ingrediente.get_descricao() + ' ' + Ingredientes.get_descricao(self)

    def get_preco_total(self):
        return self.ingrediente.get_preco_total() + Ingredientes.get_preco_total(self)


class Molho(Decorador):
    cost = 2.00
    def __init__(self, ingrediente):
        Decorador.__init__(self,  ingrediente)

class Mussarela(Decorador):
    cost = 5.00
    def __init__(self, ingrediente):
        Decorador.__init__(self,  ingrediente)

class Peperoni(Decorador):
    cost = 10.00
    def __init__(self, ingrediente):
        Decorador.__init__(self,  ingrediente)

class Frango(Decorador):
    cost = 10.00
    def __init__(self, ingrediente):
        Decorador.__init__(self,  ingrediente)

class Catupiry(Decorador):
    cost = 5.00
    def __init__(self, ingrediente):
        Decorador.__init__(self,  ingrediente)


pizza1 = Peperoni(Mussarela(Molho(Massa())))
print(pizza1.get_descricao())
print(str(pizza1.get_preco_total()))
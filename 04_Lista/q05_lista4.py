from abc import ABC, abstractmethod


class Context(ABC):
    _state = None

    def __init__(self, state) -> None:
        self.transition_to(state)

    def transition_to(self, state):
        print(f"Context: Transition to {type(state).__name__}")
        self._state = state
        self._state.context = self

    def request1(self):
        pass

    def request2(self):
        pass


class State(ABC):
    @property
    def context(self) -> Context:
        return self._context

    @context.setter
    def context(self, context: Context) -> None:
        self._context = context


class Draft(State):
    def __init__(self):
        self.finalizado = False
        self.descrever()
        self.verificar_pronto()
        self.modificar_estado()

    def descrever(self):
        print("Estado atual Draft")

    def verificar_pronto(self):
        while self.finalizado == False:
            print("O documento está pronto para a Moderação? (S/N)")
            self.resposta = input()
            if (self.resposta.upper() == 'S'):
                self.finalizado = True
            else:
                self.finalizado = False

    def modificar_estado(self):
        if self.finalizado:
            self.next = Moderation()
            self.context.transition_to(self.next)


class Moderation(State):
    def __init__(self):
        self.moderado = False
        self.descrever()
        self.verificar_pronto()
        self.modificar_estado()

    def modificar_estado(self):
        if self.moderado:
            self.next = Published()
            self.context.transition_to(self.next)
        else:
            self.next = Draft()
            self.context.transition_to(self.next)

    def verificar_pronto(self):
        print("O Documento foi aprovado? (S/N)")
        self.resposta = input()
        if (self.resposta.upper() == 'S'):
            self.moderado = True
        else:
            self.moderado = False

    def descrever(self):
        print("Estado atual Moderation")


class Published(State):
    def __init__(self):

        self.expirou = False
        self.descrever()
        self.verificar_valido()
        self.modificar_estado()

    def descrever(self):
        print("Estado atual Published")

    def verificar_valido(self):
        while not self.expirou:
            print("A publicação expirou? (S/N)")
            self.resposta = input()
            if self.resposta.upper() == 'S':
                self.expirou = True
            else:
                self.expirou = False

    def modificar_estado(self):
        if self.expirou:
            self.next = Draft()
            self.context.transition_to(self.next)




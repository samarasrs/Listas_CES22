from abc import ABC, abstractmethod

class Context(ABC):
    _state = None

    def __init__(self, state) -> None:
        self.transition_to(state)

    def transition_to(self, state):
        print(f"Context: Transition to {type(state).__name__}")
        self._state = state
        self._state.context = self

    def aprovar_documento(self):
        self._state.aprovar_documento()

    def reprovar_documento(self):
        self._state.reprovar_documento()


class State(ABC):
    @property
    def context(self) -> Context:
        return self._context

    @context.setter
    def context(self, context: Context) -> None:
        self._context = context

    @abstractmethod
    def aprovar_documento(self) -> None:
        pass

    @abstractmethod
    def reprovar_documento(self) -> None:
        pass

class Draft(State):
    def __init__(self):
        self.descrever()

    def descrever(self):
        print("Estado atual Draft")


    def aprovar_documento(self):
        self.next = Moderation()
        self.context.transition_to(self.next)

    def reprovar_documento(self) -> None:
        pass


class Moderation(State):
    def __init__(self):
        self.descrever()

    def aprovar_documento(self):
        self.next = Published()
        self.context.transition_to(self.next)

    def reprovar_documento(self):
        self.next = Draft()
        self.context.transition_to(self.next)

    def descrever(self):
        print("Estado atual Moderation")


class Published(State):
    def __init__(self):
        self.descrever()

    def descrever(self):
        print("Estado atual Published")

    def aprovar_documento(self):
        self.next = Draft()
        self.context.transition_to(self.next)

    def reprovar_documento(self) -> None:
        pass




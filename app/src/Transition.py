from State import State


class Transition:
    def __init__(self, origin: State, destiny: State, symbol: str):
        self.origin = origin
        self.destiny = destiny
        self.symbol = symbol

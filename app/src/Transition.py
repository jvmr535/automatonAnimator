from State import State


class Transition:
    def __init__(self, origin: State, destiny: State, symbol: str):
        self.origin = origin
        self.destiny = destiny
        self.symbol = symbol

    def __str__(self):
        return f'{self.origin} : {self.symbol} -> {self.destiny}'

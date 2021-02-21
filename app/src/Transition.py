from Node import Node


class Transition:
    def __init__(self, origin: Node, destiny: Node, symbol: str):
        self.origin = origin
        self.destiny = destiny
        self.symbol = symbol

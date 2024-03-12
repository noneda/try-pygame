class Npcs:
    id: int
    mid: int
    kill: bool
    minMap: list[list[int]]
    minMaps: list[list[list[int]]]
    posicion: tuple[int, int]
    posiciones: list[tuple[int, int]]

    def Movimiento(self) -> list:
        return self.minMap

    def getMiniMap(self, mnmap: list[list[int]]):
        self.minMap = mnmap

    def getMiniMaps(self, nmaps: list[list[list[int]]]):
        self.minMaps = nmaps

    def getPos(self, pos: tuple[int, int]):
        self.posicion = pos

    def getPoss(self, poss: list[tuple[int, int]]):
        self.posiciones = poss

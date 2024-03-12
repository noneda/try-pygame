from .Father.Npcs import Npcs
import pygame as pg


class Player(Npcs):
    id = 2
    status = True
    kill = False
    mid = 1

    def getKey(self, key):
        self.key = key

    def Coliciones(self, y: int, x: int) -> None:
        if self.minMap[x][y] == 0:
            self.minMap[self.mid][self.mid] = 0
            self.minMap[x][y] = self.id

        elif self.minMap[x][y] == 3:
            self.status = True

        elif self.minMap[x][y] == 4:
            self.kill = True

    def Movimiento(self) -> list[list[int]]:
        y, x = self.mid, self.mid
        if self.key == pg.K_w:
            self.Coliciones(
                x=(x - 1),
                y=(y),
            )
        elif self.key == pg.K_s:
            self.Coliciones(
                x=(x + 1),
                y=(y),
            )
        elif self.key == pg.K_a:
            self.Coliciones(
                x=(x),
                y=(y - 1),
            )
        elif self.key == pg.K_d:
            self.Coliciones(
                x=(x),
                y=(y + 1),
            )
        return self.minMap

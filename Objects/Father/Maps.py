import pygame as pg


class Map:
    sizeCel: int
    map: list[list[int]]

    def Screens(self) -> None:
        self.screen = pg.display.set_mode(
            (len(self.map[1]) * self.sizeCel, len(self.map) * self.sizeCel)
        )
        pg.display.set_caption("Game")

    def sendPost(self, a: int) -> tuple:
        for row in range(len(self.map)):
            for col in range(len(self.map[0])):
                if self.map[row][col] == a:
                    return (row, col)
        return (None, None)

    def sendAllPos(self, id: int) -> list[tuple]:
        send = []
        for row in range(len(self.map)):
            for col in range(len(self.map[0])):
                if self.map[row][col] == id:
                    send.append((row, col))
        return send

    def sendMiniMap(self, a: tuple) -> list[list[int]]:
        start_row, start_col = a[0] - 1, a[1] - 1
        mini_map = [
            [self.map[row][col] for col in range(start_col, start_col + 3)]
            for row in range(start_row, start_row + 3)
        ]
        return mini_map

    def sendMiniMaps(self, poss: list[tuple]) -> list[list[list[int]]]:
        mini_maps = []
        for pos in poss:
            start_row, start_col = pos[0] - 1, pos[1] - 1
            mini_map = [
                [self.map[row][col] for col in range(start_col, start_col + 3)]
                for row in range(start_row, start_row + 3)
            ]
            mini_maps.append(mini_map)
        return mini_maps

    def UpdateMap(self, mini_map: list[list[int]], pos: tuple):
        if 0 < pos[0] < len(self.map) - 1 and 0 < pos[1] < len(self.map[0]) - 1:
            for i, row in enumerate(mini_map):
                for j, value in enumerate(row):
                    self.map[pos[0] - 1 + i][pos[1] - 1 + j] = value

    def UpdateMaps(self, mini_maps: list[list[list[int]]], poss: list[tuple[int, int]]):
        for mini_map, pos in zip(mini_maps, poss):
            self.UpdateMap(mini_map, pos)

    def ShowMap(self):
        for row in range(len(self.map)):
            for col in range(len(self.map[1])):
                if self.map[row][col] == 1:
                    pg.draw.rect(
                        self.screen,
                        (40, 42, 53),
                        (
                            col * self.sizeCel,
                            row * self.sizeCel,
                            self.sizeCel,
                            self.sizeCel,
                        ),
                    )

                elif self.map[row][col] == 2:
                    pg.draw.rect(
                        self.screen,
                        (218, 247, 166),
                        (
                            col * self.sizeCel + 12.5,
                            row * self.sizeCel + 12.5,
                            self.sizeCel - 25,
                            self.sizeCel - 25,
                        ),
                    )

                elif self.map[row][col] == 3:
                    pg.draw.rect(
                        self.screen,
                        (249, 231, 159),
                        (
                            col * self.sizeCel + 25,
                            row * self.sizeCel + 25,
                            self.sizeCel - 50,
                            self.sizeCel - 50,
                        ),
                    )

                elif self.map[row][col] == 4:
                    pg.draw.rect(
                        self.screen,
                        (199, 0, 57),
                        (
                            col * self.sizeCel + 12.5,
                            row * self.sizeCel + 12.5,
                            self.sizeCel - 25,
                            self.sizeCel - 25,
                        ),
                    )

from .Father.Npcs import Npcs
import random as rnd


class Enemy(Npcs):
    id = 4
    kill = False
    mid = 1

    def Movimiento(self) -> list[list[list[int]]]:
        send = []
        for map in self.minMaps:
            y, x = self.mid, self.mid
            valid_moves = []

            if map[y - 1][x] == 0 or map[x - 1][y] == 2:
                valid_moves.append("up")
            if map[y + 1][x] == 0 or map[x + 1][y] == 2:
                valid_moves.append("down")
            if map[y][x - 1] == 0 or map[x][y - 1] == 2:
                valid_moves.append("left")
            if map[y][x + 1] == 0 or map[x][y + 1] == 2:
                valid_moves.append("right")

            save = (0, 0)

            if map[y - 1][x] == 2:
                self.kill = True
                save = (y - 1, x)

            elif map[y + 1][x] == 2:
                self.kill = True
                save = (y + 1, x)

            elif map[y][x - 1] == 2:
                self.kill = True
                save = (y, x - 1)
            elif map[y][x + 1] == 2:
                self.kill = True
                save = (y, x + 1)

            if self.kill:
                map[y][x] = 0
                map[save[0]][save[1]]
                print("Atrapado")

            elif valid_moves:
                new_direction = rnd.choice(valid_moves)
                map[y][x] = 0
                if new_direction == "up":
                    # print("up")
                    map[y - 1][x] = 4
                elif new_direction == "down":
                    # print("down")
                    map[y + 1][x] = 4
                elif new_direction == "left":
                    # print("left")
                    map[y][x - 1] = 4
                elif new_direction == "right":
                    # print("right")
                    map[y][x + 1] = 4
            send.append(map)
        return send

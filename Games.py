import pygame as pg
from Objects.Player import Player
from Objects.Levels import Levels
from Objects.Enemies import Enemy


class game:
    running = True
    level = 0
    map = Levels()
    play = Player()
    evil = Enemy()

    def __init__(self) -> None:
        pg.init()
        while self.running:
            self.ChangeLevels()
            self.Events()
            self.map.screen.fill((255, 255, 255))
            self.map.ShowMap()
            pg.display.flip()
            self.GameOver()

    def ChangeLevels(self):
        if self.play.status:
            self.level += 1
            print(self.level)
            self.map.LevelAct(self.level)
            self.map.Screens()
            self.play.status = False

    def GameOver(self):
        if self.play.kill or self.evil.kill:
            self.running = False
            print("GameOver")
            print(f"Player kill? {self.play.kill}")
            print(f"Enemy kill? {self.evil.kill}")

    def Events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
            elif event.type == pg.KEYDOWN:
                self.play.getKey(key=event.key)
                self.play.getPos(self.map.sendPost(self.play.id))
                self.play.getMiniMap(self.map.sendMiniMap(self.play.posicion))
                self.map.UpdateMap(self.play.Movimiento(), self.play.posicion)
                self.evil.getPoss(self.map.sendAllPos(self.evil.id))
                self.evil.getMiniMaps(self.map.sendMiniMaps(self.evil.posiciones))
                self.map.UpdateMaps(self.evil.Movimiento(), self.evil.posiciones)

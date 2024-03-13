import pygame as pg
from Objects.Player import Player
from Objects.Levels import Levels
from Objects.Enemies import Enemy
from Objects.Texts import Texts


class game:
    running = True
    level = 2
    map = Levels()
    play = Player()
    evil = Enemy()
    txt = Texts()

    def __init__(self) -> None:
        pg.init()
        pg.mixer.init()
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
            if self.level == 4:
                self.GameWin()
            else:
                sound = pg.mixer.Sound("./Medias/Pass.mp3")
                sound.play()
                self.map.LevelAct(self.level)
                self.map.Screens()
                self.ShowText(f"Level {self.level}")
                self.play.status = False

    def GameWin(self):
        sound = pg.mixer.Sound("./Medias/Win.mp3")
        sound.play()
        self.ShowText("¡¡¡ WIN !!!")
        self.running = False

    def GameOver(self):
        if self.play.kill or self.evil.kill:
            sound = pg.mixer.Sound("./Medias/Dead.wav")
            sound.play()
            self.ShowText("Game Mover")
            self.running = False

    def ShowText(self, txt: str):
        self.map.screen.fill((255, 255, 255))
        self.txt.showText(txt)
        self.map.screen.blit(self.txt.sendText(), self.txt.sendTextReact())
        pg.display.flip()
        pg.time.wait(2000)

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

import pygame as pg


class Texts:
    font = None
    text = None
    text_react = None

    def sendText(self):
        return self.text

    def sendTextReact(self):
        return self.text_react

    def showText(self, txt: str):
        self.font = pg.font.Font(None, 150)
        self.text = self.font.render(txt, True, (0, 0, 0))
        self.text_react = self.text.get_rect(center=((18 * 100) // 2, (10 * 100) // 2))

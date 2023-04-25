import pygame as pg


class Button:
    def __init__(self, text, pos, size, font_size):
        self.rect = pg.Rect(pos, size)
        self.text = text
        self.color = (100, 100, 100)
        self.font = pg.font.Font(None, font_size)
        self.rendered_text = self.font.render(text, True, (0, 0, 0))
        self.clicked = False

    def draw(self, screen):
        pg.draw.rect(screen, self.color, self.rect)
        screen.blit(self.rendered_text, self.rendered_text.get_rect(
            center=self.rect.center))

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            self.clicked = True
        elif event.type == pg.MOUSEBUTTONUP and self.clicked and self.rect.collidepoint(event.pos):
            self.clicked = False
            return True
        return False

    def get_clicked(self):
        clicked = self.clicked
        self.clicked = False
        return clicked

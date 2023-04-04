import pygame
import sys

class Button:
    def __init__(self, text, font, pos):
        self.text = text
        self.font = font
        self.pos = pos
        self.rendered_text = font.render(text, True, (255, 255, 255))
        self.rect = self.rendered_text.get_rect(topleft=pos)

    def draw(self, surface):
        pygame.draw.rect(surface, (100, 100, 100), self.rect, 2)
        surface.blit(self.rendered_text, self.rect)

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONUP and self.rect.collidepoint(event.pos):
            return True
        return False

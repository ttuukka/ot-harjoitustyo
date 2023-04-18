import pygame


class Button:
    def __init__(self, text, pos, size, font_size):
        self.rect = pygame.Rect(pos, size)
        self.text = text
        self.color = (100, 100, 100)
        self.font = pygame.font.Font(None, font_size)
        self.rendered_text = self.font.render(text, True, (0, 0, 0))
        self.hovered = False
        self.clicked = False

    def draw(self, screen, hover_color=(200, 200, 200)):
        pygame.draw.rect(
            screen, self.color if not self.hovered else hover_color, self.rect)
        screen.blit(self.rendered_text, self.rendered_text.get_rect(
            center=self.rect.center))

    def handle_mouse_motion(self, event):
        self.hovered = self.rect.collidepoint(event.pos)

    def handle_mouse_button_down(self, event):
        if event.button == 1 and self.hovered:
            self.clicked = True

    def handle_mouse_button_up(self, event):
        if event.button == 1 and self.clicked:
            self.clicked = False
            return True

    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.handle_mouse_motion(event)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            self.handle_mouse_button_down(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            return self.handle_mouse_button_up(event)
        return False

    def is_clicked(self):
        return self.clicked

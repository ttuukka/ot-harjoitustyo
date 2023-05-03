import pygame as pg


class Button:
    """Luokka jonka avulla luodaan painikkeita peliin
    """

    def __init__(self, text, pos, size, font_size):
        """Luokan konstruktori, joka luo uuden painikkeen

        Args:
            text: Painikkeen sisälle tuleva teksti
            pos: Painikkeen sijaint
            size:  Painikkeen koko
            font_size: Painikkeen tekstin fontin koko
        """
        self.rect = pg.Rect(pos, size)
        self.text = text
        self.color = (100, 100, 100)
        self.hover_color = (200, 200, 200)
        self.font = pg.font.Font(None, font_size)
        self.rendered_text = self.font.render(text, True, (0, 0, 0))
        self.clicked = False

    def draw(self, screen):
        """Piirtää painikkeen ruudulle

        Args:
            screen: Ruutu jolle painike piirretään
        """
        color = self.hover_color if self.rect.collidepoint(
            pg.mouse.get_pos()) else self.color
        pg.draw.rect(screen, color, self.rect)
        screen.blit(self.rendered_text, self.rendered_text.get_rect(
            center=self.rect.center))

    def handle_event(self, event):
        """Käsittelee panikkeiden painalluksen

        Args:
            event: Tapahtuman tiedot

        Returns:
            True, jos hiiri on painettu, sekä hiiri on painikkeen päällä alas ja False kun hiire päästetään ylös sekä hiiri on painikkeen päällä 
        """
        if event.type == pg.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            self.clicked = True
        elif event.type == pg.MOUSEBUTTONUP and self.clicked and self.rect.collidepoint(event.pos):
            self.clicked = False
            return True
        return False

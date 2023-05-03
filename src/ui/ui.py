import pygame
from ui.button import Button


class Userinterface:
    """Luokka, jonka avulla piirretään pelin eri tilanteet

    """

    def __init__(self):
        """Luokan konstruktori, joka luo uuden näkymän

        """
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Peli")
        pygame.time.Clock().tick(30)
        self.font = pygame.font.Font(None, 30)

    def create_buttons(self, texts, y_pos):
        """Luo painikkeita halutuilla teksteillä ja sijainilla. 

        Args:
            texts (list): Lista teksteistä, joista halutaan luoda painikkeet
            y_pos (int): Y-koordinaatti josta halutaan ensimmäisen painikkeen alkavan

        Returns:
            Lista: palauttaa luodut  Button -painikkeet listassa 
        """
        buttons = []
        for i, text in enumerate(texts):
            button = Button(text, (100, y_pos + i * 50), (400, 40), 30)
            buttons.append(button)
            button.draw(self.screen)
        return buttons

    def draw_question_page(self, score, question, answers):
        """Piirtää pelin kysymys -näkymän, jossa ruudun yläreunassa on pisteet,
        keskellä kysymys ja sen alapuolella vastauspainikkeet.

        Args:
            score (int): pelaajan pisteet
            question (str): kysymys
            answers (list): Lista jossa on vastausvaihtoehdot
        """
        self.screen.fill((0, 0, 0))
        self.draw_text(f"Score: {score}", 10, 10)
        self.draw_text(question, 100, 100)
        self.create_buttons(answers, 200)

    def draw_text(self, text, i, j):
        """ Luokka joa hoitaa tekstin piirtämisen näkymään.

        Args:
            text (str): teksti joka halutaan pirtää
            i (int): x-koordinaatti tekstille
            j (int): y-koordinaatti tekstille
        """
        text_surface = self.font.render(text, True, (255, 20, 147))
        rect = text_surface.get_rect()
        rect.x = i
        rect.y = j
        self.screen.blit(text_surface, rect)

    def draw_game_over_screen(self, score):
        """Piirtää "Game Over" -näkymän.

        Args:
            score (int): pelaajn pisteet pelin loppuessa
        """
        self.screen.fill((0, 0, 0))
        self.draw_text("Game Over", 100, 100)
        self.draw_text(f"Final Score: {score}", 10, 10)
        self.create_buttons(["Restart", "Exit", "Save Score"], 200)

    def draw_start_screen(self):
        """Piirtää pelin aloitusnäkymän
        """
        self.screen.fill((0, 0, 0))
        self.draw_text("Trivia", 350, 50)
        self.create_buttons(["Start", "High Scores"], 200)

    def draw_high_score_input_screen(self, name):
        """Piirtää näkymän tuloksen tallentamista varten. 

        Args:
            name (str): pelaajan antama nimi 
        """
        self.screen.fill((0, 0, 0))
        self.draw_text("Enter your name:", 50, 100)
        input_box = pygame.Rect(50, 150, 200, 32)
        pygame.draw.rect(self.screen, (255, 255, 255), input_box, 2)
        self.draw_text(name, input_box.x + 5, input_box.y + 5)
        pygame.display.flip()

    def draw_high_score_screen(self, scores):
        """Piirtää näkymän, jossa on 10 parasta tulosta järjestyksessä

        Args:
            scores (list): lista joka sisältää 10 parasta tulosta
        """
        self.screen.fill((0, 0, 0))
        self.draw_text("Top 10 Scores", 200, 10)
        y_pos = 50
        for score in scores:
            self.draw_text(str(score), 200, y_pos)
            y_pos += 20
        self.create_buttons(["Back",], 500)

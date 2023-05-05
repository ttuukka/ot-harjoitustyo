import pygame
from ui.button import Button


class Views:
    """Luokka, jonka avulla piirretään pelin eri näkymät

    """

    def __init__(self):
        """Luokan konstruktori, joka luo uuden näkymän

        """
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Peli")
        pygame.time.Clock().tick(30)

    def create_buttons(self, texts, y_pos, x_pos=100, b_width=400, b_heigth=40):
        """Luo uusia painikkeita ja piirtää ne

        Args:
            texts (list): Lista teksteistä, joista halutaan luoda painikkeet
            y_pos (int): Y-koordinaatti josta halutaan ensimmäisen painikkeen alkavan
            x_pos (int): X-koodinaatti painikkeille
            b_width (int): painikkeiden leveys
            b_height (int): painikkeiden korkeus

        Returns:
            Lista: palauttaa luodut  painikkeet listana 
        """
        buttons = []
        for i, text in enumerate(texts):
            button = Button(text, (x_pos, y_pos + i * (b_heigth + 10)),
                            (b_width, b_heigth), 30)
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
        self.create_buttons(answers, 200, 100, 500)

    def draw_text(self, text, i, j, size=30):
        """ Luokka joka hoitaa tekstin piirtämisen näkymään.

        Args:
            text (str): teksti joka halutaan pirtää
            i (int): x-koordinaatti tekstille
            j (int): y-koordinaatti tekstille
            size (int): teksti koko
        """
        font = pygame.font.Font(None, size)
        text_surface = font.render(text, True, (255, 20, 147))
        rect = text_surface.get_rect()
        rect.x = i
        rect.y = j
        self.screen.blit(text_surface, rect)

    def draw_game_over_screen(self, score):
        """Piirtää "Game Over" -näkymän.

        Args:
            score (int): pelaajan pisteet pelin loppuessa
        """
        self.screen.fill((0, 0, 0))
        self.draw_text("Game Over", 300, 100, 60)
        self.draw_text(f"Final Score: {score}", 10, 10)
        self.create_buttons(
            ["Restart", "Save Score", "High Scores", "Exit"], 200, 300, 200, 60)

    def draw_start_screen(self):
        """Piirtää pelin aloitusnäkymän
        """
        self.screen.fill((0, 0, 0))
        self.draw_text("Trivia", 350, 50, 60)
        self.create_buttons(["Start Normal", "Start Time"], 200, 275, 250, 100)

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

    def draw_high_score_screen(self, normal_scores, time_scores):
        """Piirtää näkymän, jossa on 10 parasta tulosta järjestyksessä

        Args:
            normal_scores (list): lista joka sisältää normaalin pelimuodon 10 parasta tulosta
            time_scores (list): lista joka sisältää aika pelimuodon 10 parasta tulosta
        """
        self.screen.fill((0, 0, 0))
        self.draw_text("Nomal Top 10", 100, 10)
        self.draw_text("Time Top10", 400, 10)
        y_pos = 50
        for score in normal_scores:
            self.draw_text(str(score), 100, y_pos)
            y_pos += 20
        y_pos = 50
        for score in time_scores:
            self.draw_text(str(score), 400, y_pos)
            y_pos += 20
        self.create_buttons(["Back",], 500)

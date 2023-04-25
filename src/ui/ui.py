import pygame
from ui.button import Button


class Userinterface:
    def __init__(self, res=(800, 600)):
        self.screen = pygame.display.set_mode(res)
        pygame.display.set_caption("Peli")
        pygame.time.Clock().tick(30)
        self.font = pygame.font.Font(None, 30)

    def create_buttons(self, texts, y_pos):
        buttons = []
        for i, text in enumerate(texts):
            button = Button(text, (100, y_pos + i * 50), (400, 40), 30)
            buttons.append(button)
            button.draw(self.screen)
        return buttons

    def draw_question_page(self, score, question, answers):
        self.screen.fill((0, 0, 0))
        self.draw_text(f"Score: {score}", 10, 10)
        self.draw_text(question, 100, 100)
        self.create_buttons(answers, 200)
        pygame.display.flip()

    def draw_text(self, text, i, j):
        text_surface = self.font.render(text, True, (255, 20, 147))
        rect = text_surface.get_rect()
        rect.x = i
        rect.y = j
        self.screen.blit(text_surface, rect)

    def draw_game_over_screen(self, score):
        self.screen.fill((0, 0, 0))
        self.draw_text("Game Over", 100, 100)
        self.draw_text(f"Final Score: {score}", 10, 10)
        self.create_buttons(["Restart", "Exit"], 200)
        pygame.display.flip()

    def draw_start_screen(self):
        self.screen.fill((0, 0, 0))
        self.draw_text("Trivia", 350, 50)
        self.create_buttons(["Start", "High Scores"], 200)
        pygame.display.flip()

    def draw_high_score_screen(self):
        self.screen.fill((0, 0, 0))
        self.draw_text("High Scores", 350, 50)
        self.create_buttons(["Back",], 200)
        pygame.display.flip()

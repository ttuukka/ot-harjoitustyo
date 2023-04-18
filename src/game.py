import sys
import pygame
from button import Button
from question import Question


pygame.init()

res = (800, 600)
TEXT_COLOR = (255, 20, 147)
correct_color = (0, 255, 0)
incorrect_color = (255, 0, 0)


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode(res)
        self.clock = pygame.time.Clock()
        self.score = 0
        self.current_question_index = 0
        self.questions = [
            Question('Mikä on Suomen pääkaupunki?', [
                     'Helsinki', 'Turku', 'Tallinna', 'Porvoo'], 0),
            Question('Valitse suurin numero', ['1', '2', '3', '4'], 3),
            Question('What is the smallest country in the world?', [
                     'Vatican City', 'Monaco', 'San Marino', 'Liechtenstein'], 0),
        ]
        self.current_question = None
        self.answer_buttons = []
        self.font = pygame.font.Font(None, 30)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            else:
                self.check_button_clicks(event)

    def check_button_clicks(self, event):
        for button in self.answer_buttons:
            if button.handle_event(event):
                self.check_answer(button)

    def check_answer(self, button):
        correct_answer = self.current_question.answers[self.current_question.correct_answer]
        if button.text == correct_answer:
            self.handle_correct_answer(button)
        else:
            self.handle_incorrect_answer(button)

    def handle_correct_answer(self, button):
        self.score += 1
        button.color = correct_color
        self.current_question_index += 1
        if self.current_question_index >= len(self.questions):
            self.game_over()
        else:
            self.generate_question()

    def handle_incorrect_answer(self, button):
        button.color = incorrect_color

    def generate_question(self):
        self.current_question = self.questions[self.current_question_index]
        self.answer_buttons = []
        for i, answer in enumerate(self.current_question.answers):
            button = Button(answer, (100, 200 + i * 50),
                            (400, 40), 30)
            self.answer_buttons.append(button)

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.draw_text(f"Score: {self.score}", 10, 10)
        if self.current_question is not None:
            self.draw_text(self.current_question.text, 100, 100)
            for button in self.answer_buttons:
                button.draw(self.screen)

    def draw_text(self, text, i, j):
        text_surface = self.font.render(text, True, (TEXT_COLOR))
        rect = text_surface.get_rect()
        rect.x = i
        rect.y = j
        self.screen.blit(text_surface, rect)

    def run(self):
        while True:
            self.clock.tick(60)
            self.handle_events()
            if self.current_question is None:
                self.generate_question()
            self.draw()
            pygame.display.update()

    def game_over(self):
        self.screen.fill((0, 0, 0))
        game_over_text = self.font.render("Game Over", True, (255, 255, 255))
        game_over_rect = game_over_text.get_rect(
            center=(800 // 2, 600 // 2 - 50))
        score_text = self.font.render(
            f"Final Score: {self.score}", True, (255, 255, 255))
        score_rect = score_text.get_rect(center=(800 // 2, 600 // 2 + 50))
        self.screen.blit(game_over_text, game_over_rect)
        self.screen.blit(score_text, score_rect)
        pygame.display.flip()
        pygame.time.wait(3000)
        pygame.quit()
        sys.exit()


def main():
    pygame.init()
    pygame.display.set_caption("Peli")
    Game().run()
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()

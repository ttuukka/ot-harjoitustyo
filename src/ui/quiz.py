import sys
import pygame as pg
from logic.logic import Logic


class Quiz:
    def __init__(self, view, questions):
        self.view = view
        self.logic = Logic(questions)
        self.answer_buttons = []
        self.game_over_buttons = []
        self.start_buttons = []
        self.game_start = True
        self.intialize_quiz()

    def intialize_quiz(self):
        self.game_over_buttons = self.view.create_buttons(
            ["Restart", "Exit"], 200)
        self.start_buttons = self.view.create_buttons(
            ["Start"], 200)

    def run(self):
        while True:
            self.handle_events()
            if self.game_start:
                self.view.draw_start_screen()
            elif self.logic.game_over:
                self.view.draw_game_over_screen(self.logic.score)
            else:
                self.view.draw_question_page(
                    self.logic.score,
                    self.logic.question.text,
                    self.logic.question.answers
                )

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                pg.quit()
                sys.exit()
            elif self.game_start:
                self.handle_start_screen_events(event)
            elif self.logic.game_over:
                self.handle_game_over_events(event)
            else:
                self.check_button_clicks(event)

    def check_button_clicks(self, event):
        for button in self.answer_buttons:
            if button.handle_event(event):
                if self.logic.check_answer(button):
                    self.generate_question()

    def handle_start_screen_events(self, event):
        for button in self.start_buttons:
            if button.handle_event(event) and button.text == "Start":
                self.generate_question()
                self.game_start = False

    def handle_game_over_events(self, event):
        for button in self.game_over_buttons:
            if button.handle_event(event):
                if button.text == "Restart":
                    self.restart_game()
                elif button.text == "Exit":
                    pg.quit()
                    sys.exit()

    def generate_question(self):
        self.answer_buttons = self.view.create_buttons(
            self.logic.get_next_question().answers, 200)

    def restart_game(self):
        self.logic.restart_game()
        self.generate_question()

    def game_over(self):
        self.view.draw_game_over_screen(self.logic.score)

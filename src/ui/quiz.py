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
        self.high_score_screen_buttons = []
        self.scene = "game_start"
        self.intialize_quiz()

    def intialize_quiz(self):
        self.game_over_buttons = self.view.create_buttons(
            ["Restart", "Exit", "Save Score"], 200)
        self.start_buttons = self.view.create_buttons(
            ["Start", "High Scores"], 200)
        self.high_score_screen_buttons = self.view.create_buttons(
            ["Back"], 500)

    def run(self):
        while True:
            self.handle_events()
            if self.scene == "game_start":
                self.view.draw_start_screen()
            elif self.scene == "high_score_screen":
                self.view.draw_high_score_screen(
                    self.logic.get_top10_high_score())
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
            elif self.scene == "game_start":
                self.handle_start_screen_events(event)
            elif self.logic.game_over:
                self.scene = "game_over"
                self.handle_game_over_events(event)
            elif self.scene == "high_score_screen":
                self.handle_high_score_screen_events(event)
            else:
                self.check_button_clicks(event)

    def check_button_clicks(self, event):
        for button in self.answer_buttons:
            if button.handle_event(event):
                if self.logic.check_answer(button):
                    self.generate_question()

    def handle_start_screen_events(self, event):
        for button in self.start_buttons:
            if button.handle_event(event):
                if button.text == "Start":
                    self.generate_question()
                    self.scene = "question_page"
                elif button.text == "High Scores":
                    self.scene = "high_score_screen"

    def handle_game_over_events(self, event):
        for button in self.game_over_buttons:
            if button.handle_event(event):
                if button.text == "Restart":
                    self.restart_game()
                elif button.text == "Save Score":
                    self.handle_save_high_score()
                elif button.text == "Exit":
                    pg.quit()
                    sys.exit()

    def handle_save_high_score(self):
        self.scene = "high_score_input"
        name = ""
        self.view.draw_high_score_input_screen(name)
        active = True

        def handle_keydown(event, name):
            if event.key == pg.K_RETURN:
                return False, name
            if event.key == pg.K_BACKSPACE:
                return True, name[:-1]
            return True, name + event.unicode

        while active:
            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    active, name = handle_keydown(event, name)
            self.view.draw_high_score_input_screen(name)

        self.logic.save_high_score(name)

    def handle_high_score_screen_events(self, event):
        for button in self.high_score_screen_buttons:
            if button.handle_event(event):
                if button.text == "Back":
                    self.scene = "game_start"

    def generate_question(self):
        self.answer_buttons = self.view.create_buttons(
            self.logic.get_next_question().answers, 200)

    def restart_game(self):
        self.scene = "question_page"
        self.logic.restart_game()
        self.generate_question()

    def game_over(self):
        self.view.draw_game_over_screen(self.logic.score)

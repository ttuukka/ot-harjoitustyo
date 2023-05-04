import sys
import pygame as pg
from logic.logic import Logic
from ui.views import Views
from database.score_repository import ScoreRepository
from database.question_repository import QuestionRepository


class UserInterface:
    def __init__(self):
        self.questions = QuestionRepository().questions
        self.views = Views()
        self.logic = Logic(self.questions)
        self.score_repository = ScoreRepository()
        self.answer_buttons = []
        self.game_over_buttons = []
        self.start_buttons = []
        self.high_score_screen_buttons = []
        self.scene = "game_start"
        self.high_score_saved = False
        self.initialize_quiz()

    def initialize_quiz(self):
        self.game_over_buttons = self.views.create_buttons(
            ["Restart", "Save Score", "High Scores", "Exit"], 200, 300, 200, 60)
        self.start_buttons = self.views.create_buttons(
            ["Start Normal", "Start Time"], 200, 275, 250, 100)
        self.high_score_screen_buttons = self.views.create_buttons(
            ["Back"], 500)

    def run(self):
        while True:
            self.handle_events()
            if self.scene == "game_start":
                self.views.draw_start_screen()
            elif self.scene == "high_score_screen":
                normal_scores, time_scores = self.score_repository.get_top10_scores()
                self.views.draw_high_score_screen(normal_scores, time_scores
                                                  )
            elif self.scene == "game_over":
                self.views.draw_game_over_screen(self.logic.score)
            else:
                self.views.draw_question_page(
                    self.logic.score,
                    self.logic.question.text,
                    self.logic.question.answers
                )
            pg.display.flip()

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                pg.quit()
                sys.exit()
            elif self.scene == "game_start":
                self.handle_start_screen_events(event)
            elif self.scene == "game_over":
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
                else:
                    self.scene = "game_over"

    def handle_start_screen_events(self, event):
        for button in self.start_buttons:
            if button.handle_event(event):
                if button.text == "Start Normal":
                    self.logic.set_normal_game_mode()
                elif button.text == "Start Time":
                    self.logic.set_time_game_mode()
                self.scene = "question_page"
                self.generate_question()

    def handle_game_over_events(self, event):
        for button in self.game_over_buttons:
            if button.handle_event(event):
                if button.text == "Restart":
                    self.restart_game()
                elif button.text == "Save Score" and not self.high_score_saved:
                    self.handle_save_high_score()
                    self.high_score_saved = True
                elif button.text == "High Scores":
                    self.scene = "high_score_screen"
                elif button.text == "Exit":
                    pg.quit()
                    sys.exit()

    def handle_save_high_score(self):
        self.scene = "high_score_input"
        name = ""
        self.views.draw_high_score_input_screen(name)
        active = True

        while active:
            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    active, name = self.handle_keydown(event, name)

            self.views.draw_high_score_input_screen(name)

        self.score_repository.save_score(
            name, self.logic.score, self.logic.game_mode)
        self.scene = "game_over"

    def handle_keydown(self, event, name):
        if event.key == pg.K_RETURN:
            return False, name
        elif event.key == pg.K_BACKSPACE:
            return True, name[:-1]
        elif len(name) < 10 and event.unicode.isalnum():
            return True, name + event.unicode
        else:
            return True, name

    def handle_high_score_screen_events(self, event):
        for button in self.high_score_screen_buttons:
            if button.handle_event(event):
                if button.text == "Back":
                    self.scene = "game_over"

    def generate_question(self):
        self.answer_buttons = self.views.create_buttons(
            self.logic.get_next_question().answers, 200)

    def restart_game(self):
        self.scene = "game_start"
        self.high_score_saved = False
        self.logic.restart_game()
        self.generate_question()

    def game_over(self):
        self.views.draw_game_over_screen(self.logic.score)

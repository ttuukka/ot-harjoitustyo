import random


class Logic:
    def __init__(self, question_db):
        self.question_db = set(question_db)
        self.score = 0
        self.question_index = 0
        self.question = None
        self.asked_questions = set()
        self.game_over = False
        self.high_scores = None

    def get_correct_answer(self):
        return self.question.correct_answer

    def get_next_question(self):
        remaining_questions = self.question_db - self.asked_questions
        if not remaining_questions:
            remaining_questions = set(self.question_db)
        self.question = random.choice(list(remaining_questions))
        self.asked_questions.add(self.question)
        return self.question

    def check_answer(self, button):
        if button.text == self.get_correct_answer():
            self.handle_correct_answer()
            return True
        self.handle_incorrect_answer()
        return False

    def handle_correct_answer(self):
        self.score += 1
        self.question_index += 1
        if self.question_index >= len(self.question_db):
            self.game_over = True

    def handle_incorrect_answer(self):
        self.game_over = True

    def restart_game(self):
        self.score = 0
        self.question_index = 0
        self.question = None
        self.game_over = False

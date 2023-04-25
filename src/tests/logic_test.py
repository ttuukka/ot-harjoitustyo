import unittest
from unittest.mock import Mock
from database.question import Question
from logic.logic import Logic


class TestQuestion(unittest.TestCase):
    def setUp(self):
        self.question_db = [
            Question("What is the capital of France?", [
                     "Paris", "London", "New York"], "Paris"),
            Question("What is 2+2?", ["3", "4", "5"], "4"),
            Question("Who invented the telephone?", [
                     "Alexander Graham Bell", "Thomas Edison", "Nikola Tesla"], "Alexander Graham Bell")
        ]
        self.logic = Logic(self.question_db)

    def test_get_next_question(self):
        question = self.logic.get_next_question()
        self.assertIsInstance(question, Question)

    def test_check_correct_answer(self):
        self.logic.question = Question("What is 2+2?", ["3", "4", "5"], "4")
        button_mock = Mock()
        button_mock.text = "4"
        result = self.logic.check_answer(button_mock)
        self.assertTrue(result)

    def test_check_incorrect_answer(self):
        self.logic.question = Question("What is 2+2?", ["3", "4", "5"], "4")
        button_mock = Mock()
        button_mock.text = "3"
        result = self.logic.check_answer(button_mock)
        self.assertFalse(result)

    def test_handle_correct_answer(self):
        self.logic.handle_correct_answer()
        self.assertEqual(self.logic.score, 1)
        self.assertEqual(self.logic.question_index, 1)

    def test_handle_incorrect_answer(self):
        self.logic.handle_incorrect_answer()
        self.assertTrue(self.logic.game_over)

    def test_game_restart(self):
        self.logic.score = 3
        self.logic.question_index = 4
        self.logic.game_over = True
        self.logic.restart_game()
        self.assertEqual(self.logic.score, 0)
        self.assertEqual(self.logic.question_index, 0)
        self.assertFalse(self.logic.game_over)

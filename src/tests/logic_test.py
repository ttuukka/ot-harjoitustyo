import unittest
from unittest.mock import Mock
from database.question import Question
from logic.logic import Logic


class TestLogic(unittest.TestCase):
    def setUp(self):
        self.question_db = [
            Question("What is 2+2?", ["3", "4", "5", "9"], "4")]
        self.question_db2 = [Question("What is 2+2?", ["3", "4", "5"], "4"), Question(
            "What is 1+3?", ["3", "4", "5", "9"], "4"), Question("What is 0+4?", ["3", "4", "5", "9"], "4")]
        self.logic = Logic(self.question_db)
        self.logic2 = Logic(self.question_db2)

    def test_get_next_question(self):
        question = self.logic.get_next_question()
        self.assertIsInstance(question, Question)

    def test_check_correct_answer(self):
        self.logic.game_mode = "normal"
        button_mock = Mock()
        button_mock.text = "4"
        self.logic.get_next_question()
        result = self.logic.check_answer(button_mock)
        self.assertTrue(result)
        self.assertEqual(self.logic.score, 1)

    def test_check_incorrect_answer(self):
        self.logic.game_mode = "normal"
        button_mock = Mock()
        button_mock.text = "3"
        self.logic.get_next_question()
        result = self.logic.check_answer(button_mock)
        self.assertFalse(result)
        self.assertEqual(self.logic.score, 0)
        self.assertEqual(self.logic.game_over, True)

    def test_game_restart(self):
        self.logic.score = 3
        self.logic.game_over = True
        self.logic.restart_game()
        self.assertEqual(self.logic.score, 0)
        self.assertFalse(self.logic.game_over)

    def test_set_time_game_mode(self):
        self.logic.set_time_game_mode()
        self.assertAlmostEqual(self.logic.game_mode, "time")

    def test_set_normal_game_mode(self):
        self.logic.set_normal_game_mode()
        self.assertAlmostEqual(self.logic.game_mode, "normal")

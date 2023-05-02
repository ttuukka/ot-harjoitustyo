import unittest
from unittest.mock import Mock
from unittest.mock import patch
from database.question import Question
from logic.logic import Logic
from io import StringIO
import os


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

    def test_handle_incorrect_answer(self):
        self.logic.handle_incorrect_answer()
        self.assertTrue(self.logic.game_over)

    def test_game_restart(self):
        self.logic.score = 3
        self.logic.game_over = True
        self.logic.restart_game()
        self.assertEqual(self.logic.score, 0)
        self.assertFalse(self.logic.game_over)

    def test_save_high_score(self):
        file_path = "src/database/high_scores.txt"
        if os.path.exists(file_path):
            os.remove(file_path)
        self.logic.score = 11
        self.logic.save_high_score('test_player')
        lista = self.logic.get_top10_high_score()
        self.assertIn('test_player : 11', lista)

    def test_get_top10_high_score(self):
        file_path = "src/database/high_scores.txt"
        if os.path.exists(file_path):
            os.remove(file_path)
        i = 1
        while i < 12:
            self.logic.score = i
            player = f"test_player{i}"
            self.logic.save_high_score(player)
            i += 1
        print(self.logic.get_top10_high_score())
        self.assertListEqual(self.logic.get_top10_high_score(), ['test_player11 : 11', 'test_player10 : 10', 'test_player9 : 9', 'test_player8 : 8',
                             'test_player7 : 7', 'test_player6 : 6', 'test_player5 : 5', 'test_player4 : 4', 'test_player3 : 3', 'test_player2 : 2'])

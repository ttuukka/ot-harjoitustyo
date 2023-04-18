import unittest
import pygame
from game import Game


class TestGame(unittest.TestCase):
    def setUp(self):
        res = (800, 600)
        screen = pygame.display.set_mode(res)
        pygame.init()
        self.game = Game()

    def test_int_values(self):
        self.assertEqual(self.game.score, 0)
        self.assertEqual(self.game.current_question_index, 0)

    def test_correct_answer(self):
        self.game.generate_question()
        correct_button = self.game.answer_buttons[self.game.current_question.correct_answer]
        self.game.check_answer(correct_button)
        self.assertEqual(self.game.score, 1)

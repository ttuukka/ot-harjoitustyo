import unittest
import pygame
from button import Button


class TestButton(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.screen = pygame.display.set_mode((640, 480))
        self.button = Button("Test Button", (100, 100), (200, 50), 30)

    def tearDown(self):
        pygame.quit()

    def test_click(self):
        self.assertFalse(self.button.is_clicked())

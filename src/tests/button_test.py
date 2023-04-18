import pygame
import unittest
from button import Button


class ButtonTest(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.screen = pygame.display.set_mode((640, 480))
        self.font_size = 32
        self.button = Button("Click me", (200, 200), (200, 50), self.font_size)

import unittest
import pygame
from button import Button

class TestButton(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.font = pygame.font.SysFont('Corbel', 24)
        self.button = Button('Test Button', self.font, (100, 100))
    

    def test_click(self):
        event = pygame.event.Event(pygame.MOUSEBUTTONUP, pos=(100, 100))
        self.assertTrue(self.button.is_clicked(event))
        
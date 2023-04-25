import sys
import pygame
from ui.quiz import Quiz
from ui.ui import Userinterface
from database.database import Database

pygame.init()


def main():

    pygame.display.set_caption("Peli")
    view = Userinterface()
    database = Database()
    game = Quiz(view, database.questions)
    game.run()
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()

import sys
import pygame
from ui.quiz import Quiz
from database.database import Database

pygame.init()


def main():

    database = Database()
    game = Quiz(database.questions)
    game.run()
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()

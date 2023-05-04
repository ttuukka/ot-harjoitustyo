import sys
import pygame
from ui.ui import UserInterface


def main():

    game = UserInterface()
    game.run()
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()

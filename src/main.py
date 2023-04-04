import pygame
import sys
from button import Button


pygame.init()

res = (700, 400)

screen = pygame.display.set_mode(res)

font = pygame.font.SysFont("Corbel", 26)
buttons = {
    'ans1': Button("ANSWER 1", font, (10, 10)),
    'ans2': Button("ANSWER 2", font, (10, 50)),
    'ans3': Button("ANSWER 3", font, (10, 100)),
    'ans4': Button("ANSWER 4", font, (10, 150)),
    'quit': Button("QUIT", font, (10, 200)),
}
question = font.render("QUESTION", True, (255, 255, 255))
rect6 = question.get_rect(topleft=(300, 10))

msg = " "
screen.fill((60, 25, 60))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        for button in buttons.values():
            button.draw(screen)
            if button.is_clicked(event):
                print(f"{button.text} was chosen")

        screen.blit(question, rect6)
        pygame.draw.rect(screen, (100, 100, 100), rect6, 2)

        if buttons['quit'].is_clicked(event):
            pygame.quit()

        pygame.display.update()
import pygame

from game import Game

WIDTH, HEIGHT = 800, 800
FPS = 20

win = pygame.display.set_mode((WIDTH, HEIGHT))

def main():


    clock = pygame.time.Clock()
    game = Game(WIDTH, HEIGHT)
    game.set_ans()
    run = True
    while run:
        clock.tick(FPS)
        # Do something
        game.draw(win)

        for event in pygame.event.get():
            # Quit
            if event.type == pygame.QUIT:
                run = False
            # Click
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                game.click(pos)



main()
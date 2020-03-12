import pygame
import globe

screen = pygame.display.set_mode(globe.SCREEN_SIZE, pygame.DOUBLEBUF)

while globe.running:
    # Clears screen.
    screen.fill((100, 100, 100))

    globe.GAME.run_game(screen)

    # Updates screen.
    pygame.display.update()

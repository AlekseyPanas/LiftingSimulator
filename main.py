import pygame
import globe

screen = pygame.display.set_mode(globe.SCREEN_SIZE, pygame.DOUBLEBUF)

globe.convert_alphas()

clock = pygame.time.Clock()

while globe.running:
    # Clears screen.
    screen.fill((100, 100, 100))

    globe.GAME.run_game(screen)

    # Updates screen.
    pygame.display.update()

    # sets fps to a variable. can be set to caption any time for testing.
    # Reads FPS and sets it to caption
    pygame.display.set_caption(str(clock.get_fps()))
    clock.tick(320)

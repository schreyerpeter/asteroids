import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        log_state()
        screen.fill('black')
        pygame.display.flip()
        dt = clock.tick(60) / 1000  # Limit to 60 FPS


if __name__ == "__main__":
    main()

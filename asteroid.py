import random
import pygame
from logger import log_event

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH

# Base class for game objects
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, 'white', self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
       self.position += self.velocity * dt

    def split(self):
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return
        
        log_event("asteroid_split")
        kind = self.radius // ASTEROID_MIN_RADIUS
        for _ in range(2):
            asteroid = Asteroid(self.position.x, self.position.y, ASTEROID_MIN_RADIUS * (kind - 1))
            speed = random.randint(40, 100)
            velocity = pygame.Vector2(1, 0) * speed
            velocity = velocity.rotate(random.randint(0, 360))
            asteroid.velocity = velocity
        self.kill()
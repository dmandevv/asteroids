import pygame
import random
from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        left_angle = self.velocity.rotate(random_angle)
        right_angle = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid_left = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_right = Asteroid(self.position.x, self.position.y, new_radius)

        asteroid_left.velocity = left_angle * 1.2
        asteroid_right.velocity = right_angle * 1.2
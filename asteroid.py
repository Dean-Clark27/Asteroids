import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius)
    
    def update(self, dt):
        self.position += (self.velocity * dt)
        
    def split(self):
        self.kill()
        if (self.radius <= ASTEROID_MIN_RADIUS):
            return
        else:
            random_angle = random.uniform(20,50)
            random_vec1 = self.velocity.rotate(random_angle)
            random_vec2 = self.velocity.rotate(-1 * random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            
            new_asteroid1 = Asteroid(self.position[0], self.position[1], new_radius)
            new_asteroid2 = Asteroid(self.position[0], self.position[1], new_radius)
            
            new_asteroid1.velocity = random_vec1 * 1.2
            new_asteroid2.velocity = random_vec2 * 1.2
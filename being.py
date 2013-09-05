from pvector import PVector
from random import randint
import pygame

class Being(object):

    def __init__(self, canvas, width, height):
        self.canvas = canvas
        self.color = (0, 0, 200)
        self.speed = 4
        self.sight_dist = 10

        self.location = PVector(randint(0, width), randint(0, height))
        self.velocity = PVector(
            randint(-self.speed, self.speed),
            randint(-self.speed, self.speed))

    def update(self):
        self.location.add(self.velocity)

    def draw(self):
        pygame.draw.rect(
            self.canvas, 
            self.color, 
            [self.location.x, self.location.y, 4, 4])

    def check_edges(self, width, height):
        if self.location.x > width:
            self.location.x = 0
        elif self.location.x < 0:
            self.location.x = width - 4

        if self.location.y > height:
            self.location.y = 0
        elif self.location.y < 0:
            self.location.y = height - 4

    def know_beings(self, humans, zombies):
        self.humans = humans
        self.zombies = zombies
from being import Being
from random import randint, random
from pvector import PVector

class Human(Being):

    def __init__(self, canvas, width, height):
        Being.__init__(self, canvas, width, height)
        self.panicked = False
        self.zombified = False
        self.color = (0, 200, 0)
        self.chased_by = None

    def is_zombie(self):
        return self.zombified

    def enter_panic(self, zombie):
        self.panicked = True
        self.color = (0, 125, 0)
        self.speed = 8
        self.chased_by = zombie

    def update(self):
        if not self.zombified:
            if not self.chased_by:
                # if not being chased, just make a random movement
                r = random()

                if r >= 0.50:
                    self.velocity = PVector(
                        randint(-self.speed, self.speed),
                        randint(-self.speed, self.speed))
            else:
                # move away from the zombie chasing this human
                change_x = 0
                change_y = 0

                if self.chased_by.location.x > self.location.x:
                    change_x = -self.speed
                elif self.chased_by.location.x < self.location.x:
                    change_x = self.speed

                if self.chased_by.location.y > self.location.y:
                    change_y = -self.speed
                elif self.chased_by.location.y < self.location.y:
                    change_y = self.speed

                self.velocity = PVector(change_x, change_y)

        Being.update(self)
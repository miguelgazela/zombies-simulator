from being import Being
from time import time
from pvector import PVector
from random import randint, random

class Zombie(Being):

    def __init__(self, canvas, width, height):
        Being.__init__(self, canvas, width, height)
        self.speed = 2
        self.sight_dist = 30
        self.color = (200, 0, 0)

    def update(self):
        human_distance = 1000
        chasing = False

        if hasattr(self, "humans") and not chasing:
            for human in self.humans[:]:
                if not human.is_zombie():
                    distance = self.location.distance(human.location)

                    if distance < human_distance and distance <= (self.sight_dist * 2):
                        # the human in within our sight, so go slightly faster
                        self.speed = 6
                        human_distance = distance
                        change_x = self.speed
                        change_y = self.speed

                        if self.location.x > human.location.x:
                            change_x = -self.speed

                        if self.location.y > human.location.y:
                            change_y = -self.speed

                        if human_distance < 2 * 4:
                            # reset this zombie's hunger time
                            self.last_time = time()

                            # make a new zombie
                            zombie = Zombie(self.canvas, 400, 400)
                            zombie.location.x = human.location.x
                            zombie.location.y = human.location.y
                            zombie.know_beings(self.humans, self.zombies)
                            self.zombies.append(zombie)

                            # remove the human
                            self.humans.remove(human)
                            break

                        chasing = True

                    # notify the human if we are within their sight
                    if distance < human.sight_dist:
                        if human.chased_by is not None:
                            # if the human is already chased, determine how far that zombie is from this human
                            distance_other_zombie = human.chased_by.location.distance(human.location)
                        else:
                            # set ridiculous distance so that when comparing, this zombie will be the closest
                            distance_other_zombie = 1000

                        if distance < distance_other_zombie:
                            # this zombie is the closest, so tell the human to panic and flee
                            human.enter_panic(self)
                    else:
                        if human.chased_by == self:
                            human.chased_by = None

        if not chasing:
            self.speed = 2
            r = random()

            if r >= 0.50:
                change_x = randint(-self.speed, self.speed)
                change_y = randint(-self.speed, self.speed)
            else:
                change_x = self.velocity.x
                change_y = self.velocity.y

        self.velocity = PVector(change_x, change_y)
        Being.update(self)


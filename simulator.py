import pygame
from random import randint
from being import Being
from human import Human
from zombie import Zombie
from time import time

pygame.init()

# define some colors
black   = (0, 0, 0)
white   = (255, 255, 255)
green   = (0, 255, 0)
red     = (255, 0, 0)
blue    = (0, 0, 255)

pi = 3.14159265

# Set the width and height of the screen
w_size = (1280, 720)
canvas = pygame.display.set_mode(w_size)

# Setting window title
pygame.display.set_caption("Zombie simulator")

# Setting main program loop
done = False
clock = pygame.time.Clock()


def generate_zombies(number, canvas, width, height):
    zombies = [Zombie(canvas, width, height) for __ in range(number)]
    return zombies

def generate_population(number, canvas, width, height):
    humans = [Human(canvas, width, height) for __ in range(number)]
    return humans

zombies = generate_zombies(1, canvas, w_size[0], w_size[1])
humans = generate_population(150, canvas, w_size[0], w_size[1])

for zombie in zombies:
    zombie.know_beings(humans, zombies)

for human in humans:
    human.know_beings(humans, zombies)

start = time()
font = pygame.font.Font(None, 25)

while done == False:
    # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            print "User pressed a key."
        if event.type == pygame.KEYUP:
            print "User let go of a key."
        if event.type == pygame.MOUSEBUTTONDOWN:
            print "User pressed a mouse button."

    # ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT
    for zombie in zombies:
        zombie.update()
        zombie.check_edges(w_size[0], w_size[1])

    for human in humans:
        human.update()
        human.check_edges(w_size[0], w_size[1])

    # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
    canvas.fill(white)

    output_string = "Humans: {humans} Zombies: {zombies}".format(humans=len(humans), zombies=len(zombies))
    text = font.render(output_string, True, black)
    canvas.blit(text, [10, 10])

    for zombie in zombies:
        zombie.draw()

    for human in humans:
        human.draw()

    # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

    pygame.display.flip()
    clock.tick(30)

end = time()

print "It took {0} seconds to infect everybody.".format(end-start)

pygame.quit()
exit()
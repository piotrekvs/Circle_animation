import pygame
import sys
from math import *

print(pygame.__version__)

resolution = (800, 800)

screen = pygame.display.set_mode(resolution)
pygame.display.set_caption('Circle')
clock = pygame.time.Clock()
middle = (resolution[0]/2, resolution[1]/2)

radius=300
points=360

cir_x = []
cir_y = []

for p in range(0, points, 1):
    r = 2 * pi
    r = (r / points) * p
    cir_x.append(radius*cos(r)+middle[1]) 
    cir_y.append(radius*sin(r)+middle[0])

multi = 1
skip = 0.01

while True:
    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)

    screen.fill((0,0,0))
    clock.tick(60)
    for num in range(0, points, 1):
        #pygame.draw.circle(screen, (255, 255, 255), (int(cir_x[num]),int(cir_y[num])), 1)
        num2 = num*multi
        num2 = int(num2)
        while num2 >= points:
            num2 -= points
        pygame.draw.aaline(screen, (255, 255, 255), (cir_x[num],cir_y[num]), (cir_x[num2],cir_y[num2]), 1)

    pygame.display.update()

    multi += skip
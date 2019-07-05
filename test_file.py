import pygame
import sys
from math import *
from colorsys import *

print(pygame.__version__)

# Setting window
resolution = (800, 800)
middle = (resolution[0]/2, resolution[1]/2)
screen = pygame.display.set_mode(resolution)
pygame.display.set_caption('Circle')
clock = pygame.time.Clock()

# Calculating points
radius=300
points=360
multi = 1
skip = 0.01

cir_x = []
cir_y = []
for p in range(0, points, 1):
    r = 2 * pi
    r = (r / points) * p
    cir_x.append(radius*cos(r)+middle[1]) 
    cir_y.append(radius*sin(r)+middle[0])

# Extras to animation
# HSV hue=0-360 , saturation=0-100 , value=0-100
line_color_hsv = [0, 100, 100]

# Main window loop
while True:
    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
    # Screen control
    screen.fill((0,0,0))
    clock.tick(60)
    # HSV to RGB
    line_color_rgb = (hsv_to_rgb(line_color_hsv[0]/360, line_color_hsv[1]/100, line_color_hsv[2]/100))
    line_color_rgb = (int(line_color_rgb[0]*255), int(line_color_rgb[1]*255), int(line_color_rgb[2]*255))
    # Lines drawing
    for num in range(0, points, 1):
        # Optional points drawing:
        # pygame.draw.circle(screen, (255, 255, 255), (int(cir_x[num]),int(cir_y[num])), 1)
        num2 = num*multi
        num2 = int(num2)
        while num2 >= points:
            num2 -= points
        pygame.draw.aaline(screen, line_color_rgb , (cir_x[num],cir_y[num]), (cir_x[num2],cir_y[num2]), 1)

    pygame.display.update()
    # Settings after drawing
    multi += skip
    line_color_hsv[0] += 0.2
    if line_color_hsv[0] > 360:
        line_color_hsv[0]=0
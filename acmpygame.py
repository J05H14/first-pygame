import pygame
import sys

pygame.init()

width = 600
height = 720

size = (width, height)

background_color = (0, 0, 100)

screen = pygame.display.set_mode(size)

square = pygame.image.load("square.png")

squareRect = square.get_rect()

speed = [1, 2]

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    squareRect = squareRect.move(speed)

    if squareRect.left < 0 or squareRect.right > width:
        speed[0] = -speed[0]
    if squareRect.top < 0 or squareRect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(background_color)
    screen.blit(square, squareRect)
    pygame.display.flip()
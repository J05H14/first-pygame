import pygame
import sys

pygame.init()

width = 800
height = 800

size = (width, height)

background_color = (0, 0, 100)

screen = pygame.display.set_mode(size)

ball = pygame.image.load("square.png")
ball2 = pygame.image.load("ball.png")

ballRect = ball.get_rect()
ball2Rect = ball2.get_rect()

speed = [25, 50]
speed2 = [30, 10]

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballRect = ballRect.move(speed)
    ball2Rect = ball2Rect.move(speed2)

    if ballRect.left < 0 or ballRect.right > width:
        speed[0] = -speed[0]
    if ballRect.top < 0 or ballRect.bottom > height:
        speed[1] = -speed[1]

    if ball2Rect.left < 0 or ball2Rect.right > width:
        speed2[0] = -speed2[0]
    if ball2Rect.top < 0 or ball2Rect.bottom > height:
        speed2[1] = -speed2[1]

    screen.fill(background_color)
    screen.blit(ball, ballRect)
    screen.blit(ball2, ball2Rect)
    pygame.display.flip()
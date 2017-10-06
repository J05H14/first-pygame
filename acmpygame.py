import pygame
import sys
from pygame import *

pygame.init()

width = 800
height = 800

size = (width, height)

background_color = (0, 0, 100)

screen = pygame.display.set_mode(size)

ball = pygame.image.load("square.png")
enemy = pygame.image.load("ball.png")
proj = pygame.transform.scale(ball, (25, 25))

ballRect = ball.get_rect()
projRect = proj.get_rect()
projRect.center = (-300, -300)

speed = [2, 0]
speed2 = [2, 0]

ballRect.move_ip(0, height - ballRect.bottom)


enemy = pygame.transform.scale(enemy, (100, 100))

enemies = []
enemyNum = 0

for i in range(5):
    newEnemy = enemy.get_rect()
    newEnemy.move_ip(enemyNum * 110, 0)
    enemies.append(newEnemy)
    enemyNum += 1

def enemyUpdate():
    speed2[0] = -speed2[0]
    for i in enemies:
        i.move_ip(0,25)

def hit():
    for i in enemies:
        if projRect.colliderect(i):
            enemies.remove(i)

key.set_repeat(1, 1)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_RIGHT and ballRect.right < width:
                ballRect = ballRect.move(speed[0], speed[1])
            if event.key == K_LEFT and ballRect.left < width:
                ballRect = ballRect.move(-speed[0], -speed[1])
            if event.key == K_SPACE:
                projRect.center = ballRect.center

    projRect.top -= 5

    hit()

    if len(enemies) == 0:
        break

    leftMost = enemies[0]
    rightMost = enemies[len(enemies) - 1]

    if leftMost.left < 0 or rightMost.right > width:
        enemyUpdate()

    screen.fill(background_color)
    screen.blit(ball, ballRect)

    for i in range (len(enemies)):
        enemies[i] = enemies[i].move(speed2)
        screen.blit(enemy, enemies[i])



    screen.blit(proj, projRect)
    pygame.display.flip()

if len(enemies) == 0:
    winWidth = 559
    winHeight = 420
    win = pygame.image.load("win.jpg")
    winRect = win.get_rect()

    winSize = (winWidth, winHeight)
    winScreen = pygame.display.set_mode(winSize)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        screen.blit(win, winRect)
        pygame.display.flip()
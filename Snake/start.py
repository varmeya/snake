import pygame
import time
import random

pygame.init()

displaywidth = 900
displayheight = 600
displaygame = pygame.display.set_mode((displaywidth, displayheight))
pygame.display.update()
pygame.display.set_caption("STOP, TERAZ WĘGORZ")
gameover = False

# koordy
x1 = displaywidth / 2
y1 = displayheight / 2
x1change = 0
y1change = 0

snakeblock = 10
clock = pygame.time.Clock()
snakespeed = 30
fontstyle = pygame.font.SysFont(None, 30)


def infomessage(msg, color):
    msg = fontstyle.render(msg, True, color)
    displaygame.blit(msg, [displayheight / 2, displaywidth / 2])


while not gameover:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1change = -snakeblock
                y1change = 0
            elif event.key == pygame.K_RIGHT:
                x1change = snakeblock
                y1change = 0
            elif event.key == pygame.K_UP:
                y1change = -snakeblock
                x1change = 0
            elif event.key == pygame.K_DOWN:
                y1change = snakeblock
                x1change = 0

    if x1 >= displaywidth or x1 < 0 or y1 >= displayheight or y1 < 0:
        gameover = True

    x1 += x1change
    y1 += y1change
    displaygame.fill((20, 50, 80))

    pygame.draw.rect(displaygame, (30, 0, 100), [x1, y1, snakeblock, snakeblock])
    pygame.display.update()

    clock.tick(snakespeed)

infomessage("Ręka złamana :(", (255, 0, 0))
pygame.display.update()
time.sleep(2)

pygame.quit()
quit()

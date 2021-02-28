import pygame
import time
import random

pygame.init()

snakespeed = 10
displaywidth = 800
displayheight = 600

display = pygame.display.set_mode((displaywidth, displayheight))
pygame.display.set_caption('STOP, TERAZ WĘGORZ')

clock = pygame.time.Clock()

snakeblock = 10

fontstyle = pygame.font.SysFont("arial", 25)
scorefont = pygame.font.SysFont("comicsansms", 35)



def score(score):
    value = scorefont.render("Wynik: " + str(score), True, (200, 0, 50))
    display.blit(value, [0, 0])
    return score


def snake(snakeblock, snakelist):
    for x in snakelist:
        pygame.draw.rect(display, (225, 225, 225), [x[0], x[1], snakeblock, snakeblock])


def infomessage(msg, color):
    msg = fontstyle.render(msg, True, color)
    display.blit(msg, [displaywidth / 6, displayheight / 3])


def level(level):
    value = scorefont.render("Poziom: " + str(level), True, (170, 0, 70))
    display.blit(value, [650, 0])



def game():
    gameover = False
    gameclose = False

    x1 = displaywidth / 2
    y1 = displayheight / 2

    x1change = 0
    y1change = 0

    snakelist = []
    lengthsnake = 1


    pointx = round(random.randrange(0, displaywidth - snakeblock) / 10.0) * 10.0
    pointy = round(random.randrange(0, displayheight - snakeblock) / 10.0) * 10.0

    #przeszkody
    pointx2 = round(random.randrange(0, displaywidth - snakeblock) / 10.0) * 10.0
    pointy2 = round(random.randrange(0, displayheight - snakeblock) / 10.0) * 10.0


    while not gameover:
        while gameclose == True:
            display.fill((50, 50, 50))
            infomessage(f"Twój wynik to {score(lengthsnake-1)}."
                        f"Wciśnij S aby rozpocząć grę lub Q aby wyjść", (30, 30, 30))
            score(lengthsnake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        game()
                    if event.key == pygame.K_q:
                        gameover = True
                        gameclose = False

        #sterowanie
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

        #tworzenie jedzenia i przeszkod
        if x1 >= displaywidth or x1 < 0 or y1 >= displayheight or y1 < 0:
            gameclose = True
        x1 += x1change
        y1 += y1change
        display.fill((0, 0, 10))
        pygame.draw.rect(display, (0, 150, 90), [pointx, pointy, snakeblock, snakeblock])
        pygame.draw.rect(display, (100, 100, 90), [pointx2, pointy2, snakeblock, snakeblock])

        #rosniecie weza
        snakehead = []
        snakehead.append(x1)
        snakehead.append(y1)
        snakelist.append(snakehead)
        if len(snakelist) > lengthsnake:
            del snakelist[0]
        for x in snakelist[:-1]:
            if x == snakehead:
                gameclose = True

        snake(snakeblock, snakelist)
        score(lengthsnake - 1)

        def gamelvl():
            if score(lengthsnake - 1) < 10:
                level(1)
            elif score(lengthsnake - 1) <= 11:
                level(2)
            elif score(lengthsnake - 1) <= 30:
                level(3)
            elif score(lengthsnake - 1) <= 40:
                level(4)
            elif score(lengthsnake - 1) <= 50:
                level(5)
        gamelvl()





        pygame.display.update()
        if x1 == pointx2 and y1 == pointy2:
            pointx2 = round(random.randrange(0, displaywidth - snakeblock) / 10.0) * 10.0
            pointy2 = round(random.randrange(0, displayheight - snakeblock) / 10.0) * 10.0
            gameclose= True


        if x1 == pointx and y1 == pointy:
            pointx = round(random.randrange(0, displaywidth - snakeblock) / 10.0) * 10.0
            pointy = round(random.randrange(0, displayheight - snakeblock) / 10.0) * 10.0
            lengthsnake += 1



        clock.tick(snakespeed)


    pygame.quit()
    quit()

game()
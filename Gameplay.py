# handles the gameplay using the OOP files 
import pygame
from Snake import Snake

# initialize pygame and font
pygame.init()
pygame.font.init()

# default screen size
WIDTH = 700
HEIGHT = 400

# game screen window tuple
size = (WIDTH, HEIGHT)

# set the game window size and caption
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Snake")

# create the game window
pygame.display.flip()

# setting up the snake object we are using
gameSnake = Snake(screen, WIDTH, HEIGHT, (0, 143, 17))
snake_posX = WIDTH/2
snake_posY = HEIGHT/2

# for the score text
score_font = pygame.font.SysFont('freesansbold.ttf', 30)

# game loop
running = True
delay = 0

while (running):
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            running = False

        elif (event.type == pygame.KEYDOWN):
            if (event.key == pygame.K_a):
                gameSnake.keyLeft()

            if (event.key == pygame.K_d):
                gameSnake.keyRight()

    # auto snake movement
    if (delay == 480):
        gameSnake.moveForward()
        delay = 0

    if (gameSnake.checkForBorderCollision() == True):
        running = False

    if (gameSnake.checkSnakeCollidesOneself() == True):
        running = False

    text_surface = score_font.render("Score: " + str(gameSnake.getScore()), 1,  (255, 255, 255), (0, 0, 0))
    screen.blit(text_surface, (0, 0))

    delay += 1
    pygame.display.update()
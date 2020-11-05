# necessary libraries
import pygame
import copy
import random

# importing food class
from Food import Food


class Snake:

    def __init__(self, window, width, height, snake_color):
        """class constructor

        :param window: is the game window
        :param width: is the window width
        :param height: is the window height
        :param color: is the color for the snake
        """
        # constant game window screen sizes
        self.width = width
        self.height = height
        self.window = window
        self.snake_color = snake_color
        self.snake_size = 20

        # maybe not needed
        self.snake_posX = width/2
        self.snake_posY = height/2

        # holds the entire snake's body
        self.snakeBody = []

        # up, left, down, right
        self.directions = [0, 1, 2, 3]
        self.cur_direction = self.directions[1]

        # keeping track of the score
        self.score = 0

        # for drawing food
        self.food_color = (177, 18, 38)
        self.food = Food(window, self.food_color, 20, width, height)

        # snake head
        self.setSnakeFirstPosition()

        self.moveForward()
        self.draw()

    def setSnakeFirstPosition(self):
        """sets the snake's initial position to the center of screen"""
        # append the head of the snake
        self.snakeBody.append(
            [self.width/2, self.height/2, self.snake_size, self.snake_size])
        self.addSnakeBodyPart()
        self.addSnakeBodyPart()
        self.addSnakeBodyPart()

    def setSnakePosition(self, x, y):
       """sets the snake's position to coordinate x, y

       :param x: x-coordinate
       :param y: y-coordinate
       """
       # for reference, params are x, y, width, height
       # add snake body part
       self.snakeBody.append([x, y, self.snake_size, self.snake_size])

    def addSnakeBodyPart(self):
        """ adds a body part to the snake """
        if (self.cur_direction == 0):
            self.snakeBody.append([self.snakeBody[len(self.snakeBody)-1][0], 
                              self.snakeBody[len(self.snakeBody)-1][1]+20, self.snake_size, self.snake_size])
        elif (self.cur_direction == 1):
            self.snakeBody.append([self.snakeBody[len(self.snakeBody)-1][0]+20, 
                              self.snakeBody[len(self.snakeBody)-1][1], self.snake_size, self.snake_size])
        elif (self.cur_direction == 2):
            self.snakeBody.append([self.snakeBody[len(self.snakeBody)-1][0], 
                              self.snakeBody[len(self.snakeBody)-1][1]-20, self.snake_size, self.snake_size])
        elif (self.cur_direction == 3):
            self.snakeBody.append([self.snakeBody[len(self.snakeBody)-1][0]-20, 
                              self.snakeBody[len(self.snakeBody)-1][1], self.snake_size, self.snake_size])

    def keyLeft(self):
        """ move snake left """
        if (self.cur_direction == 1):
            # store head position
            head_pos = copy.copy(self.snakeBody[0])
            # update head position
            self.snakeBody[0][1] += self.snake_size

            # update all trailing body parts to head position
            for i in range(1, len(self.snakeBody)):
                # store trailing part
                prev_pos = copy.copy(self.snakeBody[i])
                # update current part
                self.snakeBody[i] = head_pos
                # update head position
                head_pos = prev_pos
            self.cur_direction = 2

        elif (self.cur_direction == 0):
            # store head and update pos
            head_pos = copy.copy(self.snakeBody[0])
            self.snakeBody[0][0] -= self.snake_size
            for i in range(1, len(self.snakeBody)):
                prev_pos = copy.copy(self.snakeBody[i])
                self.snakeBody[i] = head_pos
                head_pos = prev_pos
            self.cur_direction = 1

        elif (self.cur_direction == 2):
            head_pos = copy.copy(self.snakeBody[0])
            self.snakeBody[0][0] += self.snake_size
            for i in range(1, len(self.snakeBody)):
                prev_pos = copy.copy(self.snakeBody[i])
                self.snakeBody[i] = head_pos
                head_pos = prev_pos
            self.cur_direction = 3

        elif (self.cur_direction == 3):
            head_pos = copy.copy(self.snakeBody[0])
            self.snakeBody[0][1] -= self.snake_size
            for i in range(1, len(self.snakeBody)):
                prev_pos = copy.copy(self.snakeBody[i])
                self.snakeBody[i] = head_pos
                head_pos = prev_pos
            self.cur_direction = 0
        self.draw()

    def keyRight(self):
        """ move snake right """
        if (self.cur_direction == 1):
            # store head position
            head_pos = copy.copy(self.snakeBody[0])
            # update head position
            self.snakeBody[0][1] -= self.snake_size
            # update all trailing body parts to head position
            for i in range(1, len(self.snakeBody)):
                # store trailing part
                prev_pos = copy.copy(self.snakeBody[i])
                # update current part
                self.snakeBody[i] = head_pos
                # update head position
                head_pos = prev_pos
            self.cur_direction = 0

        elif (self.cur_direction == 0):
            # store head and update pos
            head_pos = copy.copy(self.snakeBody[0])
            self.snakeBody[0][0] += self.snake_size
            for i in range(1, len(self.snakeBody)):
                prev_pos = copy.copy(self.snakeBody[i])
                self.snakeBody[i] = head_pos
                head_pos = prev_pos
            self.cur_direction = 3

        elif (self.cur_direction == 2):
            head_pos = copy.copy(self.snakeBody[0])
            self.snakeBody[0][0] -= self.snake_size
            for i in range(1, len(self.snakeBody)):
                prev_pos = copy.copy(self.snakeBody[i])
                self.snakeBody[i] = head_pos
                head_pos = prev_pos
            self.cur_direction = 1

        elif (self.cur_direction == 3):
            head_pos = copy.copy(self.snakeBody[0])
            self.snakeBody[0][1] += self.snake_size
            for i in range(1, len(self.snakeBody)):
                prev_pos = copy.copy(self.snakeBody[i])
                self.snakeBody[i] = head_pos
                head_pos = prev_pos
            self.cur_direction = 2
        self.draw()

    def moveForward(self):
        """ moves snake forward """
        if (self.cur_direction == 1):
            # store head position
            head_pos = copy.copy(self.snakeBody[0])
            # update head position
            self.snakeBody[0][0] -= self.snake_size
            # update all trailing body parts to head position
            for i in range(1, len(self.snakeBody)):
                # store trailing part
                prev_pos = copy.copy(self.snakeBody[i])
                # update current part
                self.snakeBody[i] = head_pos
                # update head position
                head_pos = prev_pos

        elif (self.cur_direction == 0):
            # store head and update pos
            head_pos = copy.copy(self.snakeBody[0])
            self.snakeBody[0][1] -= self.snake_size
            for i in range(1, len(self.snakeBody)):
                prev_pos = copy.copy(self.snakeBody[i])
                self.snakeBody[i] = head_pos
                head_pos = prev_pos

        elif (self.cur_direction == 2):
            head_pos = copy.copy(self.snakeBody[0])
            self.snakeBody[0][1] += self.snake_size
            for i in range(1, len(self.snakeBody)):
                prev_pos = copy.copy(self.snakeBody[i])
                self.snakeBody[i] = head_pos
                head_pos = prev_pos

        elif (self.cur_direction == 3):
            head_pos = copy.copy(self.snakeBody[0])
            self.snakeBody[0][0] += self.snake_size
            for i in range(1, len(self.snakeBody)):
                prev_pos = copy.copy(self.snakeBody[i])
                self.snakeBody[i] = head_pos
                head_pos = prev_pos
        self.draw()

    def checkForBorderCollision(self):
        """ checks if snake collides with borders of game window """
        for body_part in self.snakeBody:
            # if the x coordinate goes to the left or right of the screen
            if (body_part[0] <= 0 or body_part[0] >= self.width):
                return True

            # if the y coordinate goes to the top or bottom of the screen
            elif (body_part[1] <= 0 or body_part[1] >= self.height):
                return True

    def checkForFoodCollision(self):
        """ checks if snake is eating food """
        # get snake head position
        x = self.snakeBody[0][0]
        y = self.snakeBody[0][1]
        size1 = self.snakeBody[0][2]
        size2 = self.snakeBody[0][3]

        # get food position and then check if they intersect
        food_pos = self.food.getFoodPos()
        if (pygame.Rect(x, y, size1, size2).colliderect(pygame.Rect(food_pos[0], food_pos[1], size1, size2))):
            return True
        else:
            return False

    def checkSnakeCollidesOneself(self):
        """ checks if snake hits one of its own body parts """
        snake_h = self.snakeBody[0]
        snake_head = pygame.Rect(snake_h[0], snake_h[1], snake_h[2], snake_h[3])

        for i in range(1, len(self.snakeBody)):#body_part in self.snakeBody:
            if (snake_head.colliderect(pygame.Rect(self.snakeBody[i][0], self.snakeBody[i][1], self.snakeBody[i][2], self.snakeBody[i][3]))):
                return True
        return False

    def draw(self):
        """ draws the snake on call """
        self.window.fill((0, 0, 0))
        self.food.draw() 

        # if the snake eats food
        if (self.checkForFoodCollision()):
            self.score += 5
            # generate new food piece and draw
            x = random.randint(20, self.width-20)
            y = random.randint(20, self.height-20)
            self.food.spawnFood(x, y)

            # confirms that spawned position does not already collide with snake body
            food_pos = self.food.getFoodPos()
            for bp in self.snakeBody:
                if (pygame.Rect(food_pos[0], food_pos[1], self.snake_size, self.snake_size).colliderect(bp[0], bp[1], bp[2], bp[3])):
                    x = random.randint(20, self.width-20)
                    y = random.randint(20, self.height-20)
                    self.food.spawnFood(x, y)

            self.addSnakeBodyPart()
            self.food.draw()

        for body_part in self.snakeBody:
            pygame.draw.rect(self.window, self.snake_color, pygame.Rect(body_part[0], body_part[1], body_part[2], body_part[3]))

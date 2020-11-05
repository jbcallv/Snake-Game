# necessary libraries
import pygame
import copy


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

        self.snake_posX = width/2
        self.snake_posY = height/2

        self.snakeBody = []

        # up, left, down, right
        self.directions = [0, 1, 2, 3]
        self.cur_direction = self.directions[1]

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

    def draw(self):
        """ draws the snake on call """
        self.window.fill((0, 0, 0))
        for body_part in self.snakeBody:
            pygame.draw.rect(self.window, self.snake_color, pygame.Rect(body_part[0], body_part[1], body_part[2], body_part[3]))

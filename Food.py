import pygame

class Food:
    def __init__(self, window, food_color, food_size, width, height):
        self.window = window
        self.food_color = food_color
        self.food_size = food_size

        self.food_pieces = []

        self.width = width
        self.height = height

        self.spawnFoodFirst()

    def spawnFood(self, x, y):
        """ spawns food on call

        :param x: is the x coordinate on which to spawn food
        :param y: is the y coordinate on which to spawn food
        """
        self.food_pieces.clear()
        self.food_pieces.append([x, y, self.food_size, self.food_size])

    def spawnFoodFirst(self):
        """ spawns the food when game starts """
        self.spawnFood(self.width-100, self.height-50)

    def getFoodPos(self):
        """ checks the generated food position. Used only in Snake class

        :rtype list
        :return the x and y coordinates of the food piece on screen
        """
        foodPos = [self.food_pieces[0][0], self.food_pieces[0][1]]
        return foodPos

    def draw(self):
        """ draws all food pieces that are on screen """
        self.window.fill((0, 0, 0))
        for food_obj in self.food_pieces:
            pygame.draw.rect(self.window, self.food_color, pygame.Rect(food_obj[0], food_obj[1], food_obj[2], food_obj[3]))

import pygame

class Food:
    def __init__(self, food_color, food_size):
        self.food_color = food_color
        self.food_size = food_size

        self.food_pieces = []

    def spawnFood(self, x, y):
        """ spawns food on call
        :param x: is the x coordinate on which to spawn food
        :param y: is the y coordinate on which to spawn food
        """
        pass

    def spawnFoodFirst(self):
        """ spawns the food when game starts """
        pass

    def getFoodPos(self):
        """ checks the generated food position
        :rtype list
        :return the x and y coordinates of the food piece on screen
        """
        pass

    def draw(self):
        """ draws all food pieces that are on screen """

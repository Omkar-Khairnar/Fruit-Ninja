import pygame
import os
import random

player_lives = 3  # keep track of lives
score = 0  # keeps track of score
fruits = ['melon', 'orange', 'pomegranate', 'guava', 'bomb']  # entities in the game

# initialize pygame and create window
WIDTH = 800
HEIGHT = 500
FPS = 12  # controls how often the gameDisplay should refresh. In our case, it will refresh every 1/12th second
pygame.init()
pygame.display.set_caption('Fruit-Ninja Game -- Python.hunt')
gameDisplay = pygame.display.set_mode((WIDTH, HEIGHT))  # setting game display size
clock = pygame.time.Clock()

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

background = pygame.image.load('back.jpg')  # game background
font = pygame.font.Font(os.path.join(os.getcwd(), 'comic.ttf'), 42)
score_text = font.render('Score : ' + str(score), True, (255, 255, 255))  # score display
lives_icon = pygame.image.load('images/white_lives.png')  # images that shows remaining lives


# Timer
game_time = 30  # seconds
start_time = pygame.time.get_ticks()

# Generalized structure of the fruit Dictionary
def generate_random_fruits(fruit):
    fruit_path = "images/" + fruit + ".png"
    data[fruit] = {
        'img': pygame.image.load(fruit_path),
        'x': random.randint(100, 500),  # where the fruit should be positioned on x-coordinate
        'y': 800,
        'speed_x': random.randint(-10, 10),
        # how fast the fruit should move in x direction. Controls the diagonal movement of fruits
        'speed_y': random.randint(-80, -60),  # control the speed of fruits in y-directionn ( UP )
        'throw': False,
        # determines if the generated coordinate of the fruits is outside the gameDisplay or not. If outside, then it will be discarded
        't': 0,  # manages the
        'hit': False,
    }

    if random.random() >= 0.75:  # Return the next random floating point number in the range [0.0, 1.0) to keep the fruits inside the gameDisplay
        data[fruit]['throw'] = True
    else:
        data[fruit]['throw'] = False


# Dictionary to hold the data the random fruit generation
data = {}
for fruit in fruits:
    generate_random_fruits(fruit)


def hide_cross_lives(x, y):
    gameDisplay.blit(pygame.image.load("images/red_lives.png"), (x, y))


# Generic method to draw fonts on the screen
font_name = pygame.font.match_font('comic.ttf')

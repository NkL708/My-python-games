from time import sleep

from .board import Board
from .snake import Snake

# Game constants
WEIGHT = 3
HEIGHT = 3
TIME = 1

class Game:
    board = Board()
    snake = Snake()
    
    def start():
        pass
from test_again import Game
from pygame import mixer

g = Game()

while True:
    g.curr_menu.displayMenu()
    g.game_loop()
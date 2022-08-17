import random
from functions_pkg.start_screen import start_game
from functions_pkg.difficulty import easy_play, normal_play, hard_play
from functions_pkg.play_game import play_game

#setting up global variables
cities_selection = []
easy_selection = []
normal_selection = []
hard_selection = []
cities = []
cities_choice= {}
game_difficulty = ''
option = ['A', 'B', 'C', 'D']
high_score = 0
point = 10


# setting up game functions

    

start_game()
game_difficulty = input(f'Enter Difficulty:')
while True:
   
    if game_difficulty == '1' or game_difficulty.lower() == 'easy':
        print(f'Your difficuty level is set to Easy\n')
        cities = easy_play(easy_selection, cities_selection)
        cities1 = cities 
        play_game(cities_choice, option, cities)
    

    elif game_difficulty =='2' or game_difficulty.lower() == 'normal':
        print(f'Your difficuty level is set to Normal\n')
        cities = normal_play(normal_selection, cities_selection)
        cities2 = cities
        play_game(cities_choice, option, cities)
    
    elif game_difficulty == '3' or game_difficulty.lower() == 'hard':
        print(f'Your difficuty level is set to Hard\n')
        cities = hard_play(hard_selection, cities_selection)
        cities3 = cities
        play_game(cities_choice, option, cities)
    
    else:
        print(f'Game Aborted')


    
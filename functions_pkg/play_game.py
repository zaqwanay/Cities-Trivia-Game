
import random

not_cities_easy = ['El Dorado', 'Camelot', 'Fairy Pools', 'Gotham City', 'King\'s Landing',
                   'Basin City', 'The Citadel', 'Dark City', 'Mordor', 'Neverland', 'Castle Rock', 'Bikini Bottom']
not_cities_normal = ['Castle Island', 'Wakanda', 'Riverdale', 'The Shire', 'Quahog City',
                     'Costa Luna', 'Sunnydale', 'Bedrock', 'Whoville', 'Bluffington', 'Myst', 'Emerald City']
not_cities_hard = ['Atlantis', 'Bermuda', 'Genovia', 'Springfield', 'Shangri-La',
                   'Hillwood', 'Venusville', 'New Vegas' 'South Park', 'Arkham', 'Wellsville', 'Hill Valley']


#setting up game play function
def play_game(cities_choice, option, cities):
    score = 0
    option = ['A', 'B', 'C', 'D']
    random.shuffle(cities)
    cities_choice = dict(zip(option, cities))
    print(f'For 10pts, which one of these cities, is not a real city?\n')
    print(cities_choice)
    option_choice = input(f'Ans:')
    for option_choice in cities_choice.keys():
        answer = cities_choice.get(option_choice)
    

    if answer in not_cities_easy or answer in not_cities_normal or answer in not_cities_hard:
        print(f'You chose correctly!. {answer} is not a real city, you get 10pts\n')
        score += 10
        print(f'Your current score is: {score} points\n')

    elif answer not in not_cities_easy or answer not in not_cities_normal or answer not in not_cities_hard:
        print(f'You chose wrongly!. {answer} is a real city.\n')
        print(f'Your total score is: {score} points\n')
        return

    else:
        print(f'Enter a valid option')

    
    

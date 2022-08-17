import random
import csv


cities_list = ['Tokyo', 'Ankara', 'Cairo', 'Tunis', 'Lagos', 'Kampala', 'Abidjan', 'Seoul', 'Delhi', 'Ouagadougou', 'Dhaka', 'Samarkand', 'Bodden Town', 'Lichinga', 'Liepaja', 'Karak', 'Solo',
               'Busan', 'Perth', 'La Paz', 'Dresden', 'Utrecht', 'Kiev', 'Casablanca', 'Jaipur', 'Ghent', 'Vilnius', 'Sibiu', 'Brasov', 'Bremen', 'Ronda', 'Kumasi', 'Banjul', 'Capetown', 'Ibadan', 'Benin City']
not_cities_easy = ['El Dorado', 'Camelot', 'Fairy Pools', 'Gotham City', 'King\'s Landing',
                   'Basin City', 'The Citadel', 'Dark City', 'Mordor', 'Neverland', 'Castle Rock', 'Bikini Bottom']
not_cities_normal = ['Castle Island', 'Wakanda', 'Riverdale', 'The Shire', 'Quahog City',
                     'Costa Luna', 'Sunnydale', 'Bedrock', 'Whoville', 'Bluffington', 'Myst', 'Emerald City']
not_cities_hard = ['Atlantis', 'Bermuda', 'Genovia', 'Springfield', 'Shangri-La',
                   'Hillwood', 'Venusville', 'New Vegas' 'South Park', 'Arkham', 'Wellsville', 'Hill Valley']


def easy_play(easy_selection, cities_selection):
    easy_selection = random.sample(not_cities_easy, k=1) # select one random wrong city from easy list
    cities_selection = random.sample(cities_list, k=3) # to select 3 random correct cities_list
    cities1 = easy_selection + cities_selection
    return cities1
    


def normal_play(normal_selection, cities_selection):
    normal_selection = random.sample(not_cities_normal, k=1)
    cities_selection = random.sample(cities_list, k=3)
    cities2 = normal_selection + cities_selection
    return cities2


def hard_play(hard_selection, cities_selection):
    hard_selection = random.sample(not_cities_hard, k=1)
    cities_selection = random.sample(cities_list, k=3)
    cities3 = hard_selection + cities_selection
    return cities3

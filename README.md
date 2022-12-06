# cities_trivia_game
This game involves a player selecting the non-real city from 4 city option to score point for each correct choice
2. Design and Implementation
In order to have this dictionary of choices, I needed to populate the dictionary with real cities and a non-city value. 
First, I created a list of real cities, then I created 3 lists of non-real cities (easy, normal, and hard lists)
The program randomly selects 3 real cities and 1 non-real city from the lists. For each difficulty game play the non-city is selected from either the easy, normal, or hard lists.
Then the program assigns the values from the list of 4 cities to a dictionary with keys A, B, C, and D. The values are randomized to ensure the position of cities and non-cities are not constant in the dictionary

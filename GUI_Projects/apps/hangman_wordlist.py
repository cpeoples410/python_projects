#word list


#Wordlist themes
"""
- animals
- vehicles
- entertainment (tv shows, social media, movies, etc.)
- video game related
- sports
- others?
"""

#dictionary of categories where THEME = key and LIST = value
CATEGORIES = {"animal":["lion", "tiger", "bear", "hyena", "jackal",
                         "gorilla", "horse", "zebra", "cheetah", "walrus",
                         "penguin", "giraffe", "pelican", "dolphin", "whale",
                         "kangaroo", "panda", "leopard", "elephant", "parrot"],
              "sports":["basketball", "hockey", "baseball", "golf", "bowling",
                        "tennis", "swimming", "kickball", "softball", "boxing",
                        "badminton", "volleyball", "lacrosse", "skateboarding", "rugby",
                        "racketball", "pickleball"],
              "food":["pizza", "macaroni and cheese", "burrito", "hamburger", "ice cream",
                      "applesauce", "fish sticks", "meatloaf", "french fries", "smores",
                      "chicken pot pie", "lasagna", "spaghetti", "shrimp scampi", "chicken nuggets"],
              "cartoons":["Spongebob", "Powerpuff Girls", "Rugrats", "Ducktales",
                          "Adventure Time", "Regular Show", "Steven Universe", "Looney Tunes",
                          "Phineas and Ferb", "Gravity Falls", "Samurai Jack", "Avatar: The Last Airbender"],
              "videogames":["Mario Bros", "Sonic the Hedgehog", "Pokemon", "Final Fantasy",
                      "Crash Bandicoot", "Spyro", "Legend of Zelda", "Pac-Man",
                      "Undertale", "Tetris", "Fire Emblem", "Splatoon",
                      "Minecraft", "Animal Crossing", "Overwatch", "God of War",
                      "World of Warcraft", "Grand Theft Auto", "BioShock", "Among Us"]}


#Dictionary that stores CATEGORY IDs (used for random selection)
ID = {}
index = 0
for key in CATEGORIES:
    ID[index] = key
    index += 1

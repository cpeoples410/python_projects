import random as r
import hangman_wordlist as hw
#from hangman_wordlist import *
#from HangmanPlayer import *

#Hangman Project
"""
Game where player guesses a word. User gets
limited about of guesses. Game is over when the user
guesses the word, or the player runs out of guesses.
"""

"""
Things needed for game:
    - display of game
        > hang man (changes based on number of incorrect answers)
        > number of '_' for charactes in words
          (doesn't affect spaces between words)
    - functions
        > allow player to pick one of the word lists
        > let user guess full word(s) (EXCLUDED FOR NOW)
        > (sounds similar to wheel of fortune)
    - Scoring
"""


board = ["_ _ _ _ ------| _ _",
         "_ _ _ _ | _ _ | _ _",
         "_ _ _ _ _ _ _ | _ _",
         "_ _ _ _ _ _ _ | _ _",
         "_ _ _ _ _ _ _ | _ _",
         "_ _ _ _ _ _ _ | _ _",
         "_ _ _ _ _ _ _ | _ _",
         "_ _ _ _ _ ____|____"]






#-------------------------------------------------------------#
#Will create class at a later time
'''
class Hangman:
    """Class that controls functionality of the game"""
    
    def getRandWord(self):
        """(None) -> str

        Randomly selects a word from any category.
        """
        key = ID.get(r.randint(0, len(CATEGORIES)))
        L = CATEGORIES.get(key)
        word = L[r.randint(0, len(key))]
        return word


    def getWord(self, choice):
        """(None, str) -> str

        Based on user's choice on the category, randomly
        select a word from a specific list.

        *Word input = type of category
        """
        L = CATEGORIES.get(choice)
        index = r.randint(0, len(L))
        word = L[index]
        return word


    def startGame(self):
        """
        """
        return 0


    def endGame(self):
        """
        """
        return 0
'''

#-------------------------------------------------------------#

def replaceSpaces(space, word, letter):
    """(string, char) -> 

    Replace all empty spaces with the letters
    """
    temp = ""
    for index in range(len(word)):
        if letter == word[index]:
            temp = temp + letter
        else:
            temp = temp + space[index]
    space = temp
    return space

def run(target_word):
    """(string) -> None"""
    space = '_' * len(target_word)
    while ('_' in space):
        guess = input("Guess a letter: ")
        if guess in target_word:
            space = replaceSpaces(space, target_word, guess)
        else:
            #will be changed
            print("Letter not found.")
        print(space)
    print(space, "has been found")


if __name__=="__main__":
    print("Welcome to HANGMAN! Which of these categories would you like?")
    #check to see if word is in category
    counter = 0
    rand_word = ""
    while True:
        category = input("ANIMAL -- SPORTS -- FOOD -- CARTOONS -- VIDEOGAMES\n").lower()
        if counter==4:
            print("TOO MANY ERRORS! ENDING GAME NOW!")
            break
        elif category not in hw.CATEGORIES:
            print("I'm sorry, that is not a theme from the category. Please pick another one:")
            counter+=1
        else:
            rand_word = r.choice(hw.CATEGORIES[category])
            print(rand_word)
            break
    if counter<4:
        run(rand_word)
    print("END OF GAME")




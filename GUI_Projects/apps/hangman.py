import random as r
from hangman_wordlist import *
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
        > let user guess full word(s)
        > (sounds similar to wheel of fortune)
    - scoring
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


#-------------------------------------------------------------#

def run():
    """dict{category: [list of words]} -> None"""
    while True:
        print("What would you like to do?")
        playerRes = input("GUESS LETTER -- GUESS WORD -- QUIT GAME").upper()
        if playerRes == "GUESS LETTER":
            char = input("Guess a letter: ")
        elif playerRes == "GUESS LETTER":
            guess = input("What is the word? ")
        elif playerRes == "QUIT GAME":
            break
    #if word is guessed correctly, show winner
    #else, show loser


if __name__=="__main__":
    print("Welcome to HANGMAN! Which of these categories would you like?")
    #check to see if word is in category
    counter = 0
    while True:
        category = input("ANIMAL -- SPORTS -- FOOD -- CARTOONS -- VIDEOGAMES")
        if category not in CATEGORIES:
            print("I'm sorry, that is not a theme from the category. Please pick another one:")
            counter+=1
        if counter == 5:
            print("TOO MANY ERRORS! ENDING GAME NOW!")
            break
        else:
            run()
    print()




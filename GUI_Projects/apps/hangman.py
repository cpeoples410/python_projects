import random as r
import hangman_wordlist as hw
import hangman_board as brd

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
def createLines(word):
    """(string) -> string

    Given a string, replace all alphabetical
    characters with underscores.
    """
    temp = ""
    for index in range(len(word)):
        if word[index].isalpha():
            temp = temp + '_'
        else:
            temp = temp + word[index]
    return temp


def showLetters(space, word, letter):
    """(char, string, char) -> string

    Return a new string where a target letter
    replaces an empty line.
    """
    temp = ""
    for index in range(len(word)):
        if (letter==word[index] or letter.upper()==word[index]):
            temp = temp + word[index]
        else:
            temp = temp + space[index]
    space = temp
    return space


def run(target_word):
    """(string) -> None"""
    hidden = createLines(target_word)
    prev = hidden
    print(hidden)
    while ('_' in hidden and brd.curr_key<6):
        guess = input("Guess a letter: ")
        if guess.isalpha():
            hidden = showLetters(hidden, target_word, guess)
            if prev==hidden:
                print("Letter not found.")
                brd.curr_key +=1
                brd.curr_state = brd.board_state[brd.curr_key]
        else:
            print("Your guess must be a letter")
        brd.printBoard(brd.curr_state)
        print(hidden)
    if ('_' not in hidden):
        print(f"{hidden} has been found!")
    else:
        print(f"GAME OVER! The word we were looking for is {target_word}")


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
            #print(rand_word)
            break
    if counter<4:
        run(rand_word)
    print("END OF GAME")




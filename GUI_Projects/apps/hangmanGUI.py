import tkinter as tk
import random as rand
import hangman_wordlist as hwl
import hangman_board as brd

#HANGMAN GUI


class HangmanGUI:
    """Class for hangman game"""

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Hangman")
        self.window.geometry("500x500")
        #self.window.maxsize(width=500, height=500)
        #self.window.minsize(width=500, height=500)

        #VARIABLE FOR RANDOM WORD
        self.category = ""
        self.target_word = ""

        #TITLE FOR THE GAME
        self.lbl_title = tk.Label(self.window, text="HANGMAN",
                                  font=("Bell Gothic Std Light", 20))
        self.lbl_title.pack()
        
        #FRAME FOR START MENU
        self.frm_start = tk.Frame(self.window)
        self.lbl_options = tk.Label(self.frm_start, text="Choose a Theme",
                                    font=("Bell Gothic Std Light", 15))
        self.lbl_options.grid(row=100, columnspan=5)
        
        #BUTTONS FOR CATEGORY BUTTONS
        self.btn_animal = tk.Button(self.frm_start, text="ANIMAL",
                                    command=lambda: [self.get_rand_word(self.btn_animal),
                                                     self.hide_letters(), self.remove_frame(),
                                                     self.show_frame()])
        self.btn_sports = tk.Button(self.frm_start, text="SPORTS",
                                    command=lambda: [self.get_rand_word(self.btn_sports),
                                                     self.hide_letters(), self.remove_frame(),
                                                     self.show_frame()])
        self.btn_food = tk.Button(self.frm_start, text="FOOD",
                                  command=lambda: [self.get_rand_word(self.btn_food),
                                                   self.hide_letters(), self.remove_frame(),
                                                   self.show_frame()])
        self.btn_toons = tk.Button(self.frm_start, text="CARTOONS",
                                   command=lambda: [self.get_rand_word(self.btn_toons),
                                                    self.hide_letters(), self.remove_frame(),
                                                    self.show_frame()])
        self.btn_games = tk.Button(self.frm_start, text="VIDEOGAMES",
                                   command=lambda: [self.get_rand_word(self.btn_games),
                                                    self.hide_letters(), self.remove_frame(),
                                                    self.show_frame()])
        #BINDING BUTTONS
        self.btn_animal.grid(row=200, column=0)
        self.btn_sports.grid(row=200, column=1)
        self.btn_food.grid(row=200, column=2)
        self.btn_toons.grid(row=200, column=3)
        self.btn_games.grid(row=200, column=4)
        
        self.frm_start.pack()

        self.stage = 0
        self.board_stage = "".join(brd.board_state[self.stage])
        #print(board_stage)


        #FRAME FOR GAME SCREEN
        self.frm_game = tk.Frame(self.window)
        #HANGMAN IMAGE
        self.lbl_board = tk.Label(self.frm_game, text=self.board_stage)
        self.lbl_board.grid(row=100, columnspan=13)

        #LABEL FOR CHOOSEN CATEGORY
        self.lbl_category = tk.Label(self.frm_game, text=self.category)
        self.lbl_category.grid(row=150, columnspan=13)
        
        #HANGMAN EMPTY STRINGS
        self.lbl_hidden = tk.Label(self.frm_game)
        self.lbl_hidden.grid(row=200, columnspan=13)
        
        #HANGMAN CHARACTERS
        self.btn_A = tk.Button(self.frm_game, text="A",
                               command=lambda: [self.find_letter(self.btn_A),
                                                self.remove_button(self.btn_A),
                                                self.end_condition()])
        self.btn_B = tk.Button(self.frm_game, text="B",
                               command=lambda: [self.find_letter(self.btn_B),
                                                self.remove_button(self.btn_B),
                                                self.end_condition()])          
        self.btn_C = tk.Button(self.frm_game, text="C",
                               command=lambda: [self.find_letter(self.btn_C),
                                                self.remove_button(self.btn_C),
                                                self.end_condition()])
        self.btn_D = tk.Button(self.frm_game, text="D",
                               command=lambda: [self.find_letter(self.btn_D),
                                                self.remove_button(self.btn_D),
                                                self.end_condition()])
        self.btn_E = tk.Button(self.frm_game, text="E",
                               command=lambda: [self.find_letter(self.btn_E),
                                                self.remove_button(self.btn_E),
                                                self.end_condition()])
        self.btn_F = tk.Button(self.frm_game, text="F",
                               command=lambda: [self.find_letter(self.btn_F),
                                                self.remove_button(self.btn_F),
                                                self.end_condition()])
        self.btn_G = tk.Button(self.frm_game, text="G",
                               command=lambda: [self.find_letter(self.btn_G),
                                                self.remove_button(self.btn_G),
                                                self.end_condition()])
        self.btn_H = tk.Button(self.frm_game, text="H",
                               command=lambda: [self.find_letter(self.btn_H),
                                                self.remove_button(self.btn_H),
                                                self.end_condition()])
        self.btn_I = tk.Button(self.frm_game, text="I",
                               command=lambda: [self.find_letter(self.btn_I),
                                                self.remove_button(self.btn_I),
                                                self.end_condition()])
        self.btn_J = tk.Button(self.frm_game, text="J",
                               command=lambda: [self.find_letter(self.btn_J),
                                                self.remove_button(self.btn_J),
                                                self.end_condition()])
        self.btn_K = tk.Button(self.frm_game, text="K",
                               command=lambda: [self.find_letter(self.btn_K),
                                                self.remove_button(self.btn_K),
                                                self.end_condition()])
        self.btn_L = tk.Button(self.frm_game, text="L",
                               command=lambda: [self.find_letter(self.btn_L),
                                                self.remove_button(self.btn_L),
                                                self.end_condition()])
        self.btn_M = tk.Button(self.frm_game, text="M",
                               command=lambda: [self.find_letter(self.btn_M),
                                                self.remove_button(self.btn_M),
                                                self.end_condition()])
        self.btn_N = tk.Button(self.frm_game, text="N",
                               command=lambda: [self.find_letter(self.btn_N),
                                                self.remove_button(self.btn_N),
                                                self.end_condition()])
        self.btn_O = tk.Button(self.frm_game, text="O",
                               command=lambda: [self.find_letter(self.btn_O),
                                                self.remove_button(self.btn_O),
                                                self.end_condition()])
        self.btn_P = tk.Button(self.frm_game, text="P",
                               command=lambda: [self.find_letter(self.btn_P),
                                                self.remove_button(self.btn_P),
                                                self.end_condition()])
        self.btn_Q = tk.Button(self.frm_game, text="Q",
                               command=lambda: [self.find_letter(self.btn_Q),
                                                self.remove_button(self.btn_Q),
                                                self.end_condition()])
        self.btn_R = tk.Button(self.frm_game, text="R",
                               command=lambda: [self.find_letter(self.btn_R),
                                                self.remove_button(self.btn_R),
                                                self.end_condition()])
        self.btn_S = tk.Button(self.frm_game, text="S",
                               command=lambda: [self.find_letter(self.btn_S),
                                                self.remove_button(self.btn_S),
                                                self.end_condition()])
        self.btn_T = tk.Button(self.frm_game, text="T",
                               command=lambda: [self.find_letter(self.btn_T),
                                                self.remove_button(self.btn_T),
                                                self.end_condition()])
        self.btn_U = tk.Button(self.frm_game, text="U",
                               command=lambda: [self.find_letter(self.btn_U),
                                                self.remove_button(self.btn_U),
                                                self.end_condition()])
        self.btn_V = tk.Button(self.frm_game, text="V",
                               command=lambda: [self.find_letter(self.btn_V),
                                                self.remove_button(self.btn_V),
                                                self.end_condition()])
        self.btn_W = tk.Button(self.frm_game, text="W",
                               command=lambda: [self.find_letter(self.btn_W),
                                                self.remove_button(self.btn_W),
                                                self.end_condition()])
        self.btn_X = tk.Button(self.frm_game, text="X",
                               command=lambda: [self.find_letter(self.btn_X),
                                                self.remove_button(self.btn_X),
                                                self.end_condition()])
        self.btn_Y = tk.Button(self.frm_game, text="Y",
                               command=lambda: [self.find_letter(self.btn_Y),
                                                self.remove_button(self.btn_Y),
                                                self.end_condition()])
        self.btn_Z = tk.Button(self.frm_game, text="Z",
                               command=lambda: [self.find_letter(self.btn_Z),
                                                self.remove_button(self.btn_Z),
                                                self.end_condition()])

        self.btn_A.grid(row=300, column=0)
        self.btn_B.grid(row=300, column=1)
        self.btn_C.grid(row=300, column=2)
        self.btn_D.grid(row=300, column=3)
        self.btn_E.grid(row=300, column=4)
        self.btn_F.grid(row=300, column=5)
        self.btn_G.grid(row=300, column=6)
        self.btn_H.grid(row=300, column=7)
        self.btn_I.grid(row=300, column=8)
        self.btn_J.grid(row=300, column=9)
        self.btn_K.grid(row=300, column=10)
        self.btn_L.grid(row=300, column=11)
        self.btn_M.grid(row=300, column=12)
        
        self.btn_N.grid(row=400, column=0)
        self.btn_O.grid(row=400, column=1)
        self.btn_P.grid(row=400, column=2)
        self.btn_Q.grid(row=400, column=3)
        self.btn_R.grid(row=400, column=4)
        self.btn_S.grid(row=400, column=5)
        self.btn_T.grid(row=400, column=6)
        self.btn_U.grid(row=400, column=7)
        self.btn_V.grid(row=400, column=8)
        self.btn_W.grid(row=400, column=9)
        self.btn_X.grid(row=400, column=10)
        self.btn_Y.grid(row=400, column=11)
        self.btn_Z.grid(row=400, column=12)
        
        self.window.mainloop()


    #----------[ METHODS ]----------#
    def get_rand_word(self, button):
        """(tk.Button) -> None

        Given a dictionary of CATEGORIES,
        reassign rand_word to a random word from
        one of the keys.
        """
        self.category = button["text"]
        self.lbl_category["text"] = self.category
        L = hwl.CATEGORIES[self.category.lower()]
        self.target_word = rand.choice(L).upper()
        #print(self.target_word, self.category)

    def remove_frame(self):
        """Removes the frame"""
        self.frm_start.pack_forget()

    def show_frame(self):
        """Shows a frame"""
        self.frm_game.pack()

    def hide_letters(self):
        """Change label so that only underscores will show"""
        temp = ""
        for i in range(len(self.target_word)):
            if self.target_word[i].isalpha():
                temp = temp + "_"
            else:
                temp = temp + self.target_word[i]
        self.lbl_hidden["text"] = temp
        print(self.lbl_hidden["text"],len(self.lbl_hidden["text"]))

    def word_found(self):
        """(None) -> boolean

        Return True if the word has been found.
        """
        return self.lbl_hidden["text"]==self.target_word

    def change_board(self):
        """
        Changes the stage of the board if
        the player guesses the wrong letter.
        """
        self.stage +=1
        self.board_stage = "".join(brd.board_state[self.stage])
        self.lbl_board["text"] = self.board_stage
        #print(self.stage, self.board_stage)

    def find_letter(self, button):
        """(tk.Button) -> None

        When a letter button is clicked, check if that letter
        is found in the target word.
        """
        letter = button["text"]
        hidden = self.lbl_hidden["text"]
        L = [hidden[x] for x in range(len(hidden))]
        if letter in self.target_word:
            for i in range(len(self.target_word)):
                if self.target_word[i]==letter:
                    L[i]=letter
        else:
            self.change_board()
        self.lbl_hidden["text"] = "".join(L)

    def remove_button(self, button):
        """Remove a letter after it was clicked on"""
        button.destroy()

    def end_condition(self):
        """
        Change label based on conditions.

        Win condition:
            -> Word has been found before image is completed.
        Lose condition:
            -> Image was completed before word was found.
        """
        if (self.word_found() == True):
            self.lbl_category["text"] = "YOU WIN!"
        elif (self.word_found()==False) and (self.stage==6):
            self.lbl_category["text"] = "Sorry! We were looking for: " + self.target_word


HangmanGUI()


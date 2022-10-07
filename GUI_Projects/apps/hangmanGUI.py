import tkinter as tk
import random as rand
import hangman_wordlist as hwl
import hangman_board as brd
import time

#HANGMAN GUI

#----------------------------------------------------------------#
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
        self.target = ""
        self.hidden = ""
        self.quit_flag = 0
        self.after_id = ""
        self.letters_found = []

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
                                                     self.hide_letters(), self.show_game_frame(),
                                                     self.start_clock()])
        self.btn_sports = tk.Button(self.frm_start, text="SPORTS",
                                    command=lambda: [self.get_rand_word(self.btn_sports),
                                                     self.hide_letters(), self.show_game_frame(),
                                                     self.start_clock()])
        self.btn_food = tk.Button(self.frm_start, text="FOOD",
                                  command=lambda: [self.get_rand_word(self.btn_food),
                                                   self.hide_letters(), self.show_game_frame(),
                                                   self.start_clock()])
        self.btn_toons = tk.Button(self.frm_start, text="CARTOONS",
                                   command=lambda: [self.get_rand_word(self.btn_toons),
                                                    self.hide_letters(), self.show_game_frame(),
                                                    self.start_clock()])
        self.btn_games = tk.Button(self.frm_start, text="VIDEOGAMES",
                                   command=lambda: [self.get_rand_word(self.btn_games),
                                                    self.hide_letters(), self.show_game_frame(),
                                                    self.start_clock()])
        #GRIDS FOR BUTTONS
        self.btn_animal.grid(row=200, column=0)
        self.btn_sports.grid(row=200, column=1)
        self.btn_food.grid(row=200, column=2)
        self.btn_toons.grid(row=200, column=3)
        self.btn_games.grid(row=200, column=4)
        
        self.frm_start.pack()

        self.stage = 0
        self.board_stage = "".join(brd.board_state[self.stage])
        
        #LABEL FOR TIMER
        self.lbl_timer = tk.Label(self.window, text=-1)

        #HANGMAN IMAGE
        self.lbl_board = tk.Label(self.window, text=self.board_stage)
        
        #LABELS FOR CATEGORY AND HIDDEN LETTERS
        self.lbl_category = tk.Label(self.window, text=self.category)
        self.lbl_hidden = tk.Label(self.window)
        
        #FRAME FOR LETTER BUTTONS
        self.frm_game = tk.Frame(self.window)

        self.btn_A = tk.Button(self.frm_game, text="A",
                               command=lambda: [self.find_letter(self.btn_A),
                                                self.end_condition()])
        self.btn_B = tk.Button(self.frm_game, text="B",
                               command=lambda: [self.find_letter(self.btn_B),
                                                self.end_condition()])          
        self.btn_C = tk.Button(self.frm_game, text="C",
                               command=lambda: [self.find_letter(self.btn_C),
                                                self.end_condition()])
        self.btn_D = tk.Button(self.frm_game, text="D",
                               command=lambda: [self.find_letter(self.btn_D),
                                                self.end_condition()])
        self.btn_E = tk.Button(self.frm_game, text="E",
                               command=lambda: [self.find_letter(self.btn_E),
                                                self.end_condition()])
        self.btn_F = tk.Button(self.frm_game, text="F",
                               command=lambda: [self.find_letter(self.btn_F),
                                                self.end_condition()])
        self.btn_G = tk.Button(self.frm_game, text="G",
                               command=lambda: [self.find_letter(self.btn_G),
                                                self.end_condition()])
        self.btn_H = tk.Button(self.frm_game, text="H",
                               command=lambda: [self.find_letter(self.btn_H),
                                                self.end_condition()])
        self.btn_I = tk.Button(self.frm_game, text="I",
                               command=lambda: [self.find_letter(self.btn_I),
                                                
                                                self.end_condition()])
        self.btn_J = tk.Button(self.frm_game, text="J",
                               command=lambda: [self.find_letter(self.btn_J),
                                                
                                                self.end_condition()])
        self.btn_K = tk.Button(self.frm_game, text="K",
                               command=lambda: [self.find_letter(self.btn_K),
                                                self.end_condition()])
        self.btn_L = tk.Button(self.frm_game, text="L",
                               command=lambda: [self.find_letter(self.btn_L),
                                                self.end_condition()])
        self.btn_M = tk.Button(self.frm_game, text="M",
                               command=lambda: [self.find_letter(self.btn_M),
                                                self.end_condition()])
        self.btn_N = tk.Button(self.frm_game, text="N",
                               command=lambda: [self.find_letter(self.btn_N),
                                                
                                                self.end_condition()])
        self.btn_O = tk.Button(self.frm_game, text="O",
                               command=lambda: [self.find_letter(self.btn_O),
                                                self.end_condition()])
        self.btn_P = tk.Button(self.frm_game, text="P",
                               command=lambda: [self.find_letter(self.btn_P),
                                                self.end_condition()])
        self.btn_Q = tk.Button(self.frm_game, text="Q",
                               command=lambda: [self.find_letter(self.btn_Q),
                                                self.end_condition()])
        self.btn_R = tk.Button(self.frm_game, text="R",
                               command=lambda: [self.find_letter(self.btn_R),
                                                self.end_condition()])
        self.btn_S = tk.Button(self.frm_game, text="S",
                               command=lambda: [self.find_letter(self.btn_S),
                                                self.end_condition()])
        self.btn_T = tk.Button(self.frm_game, text="T",
                               command=lambda: [self.find_letter(self.btn_T),
                                                self.end_condition()])
        self.btn_U = tk.Button(self.frm_game, text="U",
                               command=lambda: [self.find_letter(self.btn_U),
                                                self.end_condition()])
        self.btn_V = tk.Button(self.frm_game, text="V",
                               command=lambda: [self.find_letter(self.btn_V),
                                                self.end_condition()])
        self.btn_W = tk.Button(self.frm_game, text="W",
                               command=lambda: [self.find_letter(self.btn_W),
                                                self.end_condition()])
        self.btn_X = tk.Button(self.frm_game, text="X",
                               command=lambda: [self.find_letter(self.btn_X),
                                                self.end_condition()])
        self.btn_Y = tk.Button(self.frm_game, text="Y",
                               command=lambda: [self.find_letter(self.btn_Y),
                                                self.end_condition()])
        self.btn_Z = tk.Button(self.frm_game, text="Z",
                               command=lambda: [self.find_letter(self.btn_Z),
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
        
        
        self.btn_pause = tk.Button(self.frm_game, text="PAUSE",
                                   command=self.pause_game)
        self.btn_resume = tk.Button(self.frm_game, text="RESUME",
                                    command=self.resume_game)
        self.btn_quit = tk.Button(self.frm_game, text="QUIT",
                                  command=self.quit_game)
        self.btn_pause.grid(row=500, column=0, columnspan=6)
        self.btn_quit.grid(row=500, column=7, columnspan=6)
        
        #LABEL THAT ASKS IF USER WANTS TO QUIT
        self.lbl_ask = tk.Label(self.window, text="DO YOU WANT TO QUIT?")
        

        #FRAME THAT ASKS PLAYER TO PLAY ANOTHER GAME
        self.frm_replay = tk.Frame(self.window)
        self.lbl_replay = tk.Label(self.frm_replay, text="DO YOU WANT TO PLAY AGAIN?")

        self.btn_yes = tk.Button(self.frm_replay, text="YES",
                                 command=lambda: [self.play_again(self.btn_yes)])
        self.btn_no = tk.Button(self.frm_replay, text="NO",
                                command=lambda: [self.play_again(self.btn_no)])

        self.lbl_replay.grid(row=400, columnspan=12)
        self.btn_yes.grid(row=500, column=0, columnspan=6)
        self.btn_no.grid(row=500, column=7, columnspan=6)
        
        self.window.mainloop()


    #------------------------[ METHODS ]------------------------#
    
    def get_rand_word(self, button):
        """(tk.Button) -> None

        Given a dictionary of CATEGORIES,
        reassign rand_word to a random word from
        one of the keys.
        """
        self.category = button["text"]
        self.lbl_category["text"] = self.category
        L = hwl.CATEGORIES[self.category.lower()]
        self.target = rand.choice(L).upper()

    #NOT USING; WILL REMOVE FRAME IN METHOD BELOW
    def remove_start_frame(self):
        """Removes the frame"""
        self.frm_start.pack_forget()

    #NEED TO CHECK THIS CODE
    def show_game_frame(self):
        """Shows a frame"""
        self.frm_start.pack_forget()
        self.lbl_timer.pack()
        self.lbl_board.pack()
        self.lbl_category.pack()
        self.lbl_hidden.pack()
        self.frm_game.pack()

    def show_replay_frame(self):
        """Ask player if they want to play another game"""
        self.frm_game.pack_forget()
        self.frm_replay.pack()

    #WORKS (keep)
    def hide_letters(self):
        """Change label so that only underscores will show"""
        for i in range(len(self.target)):
            if self.target[i].isalpha():
                self.hidden = self.hidden + "_"
            else:
                self.hidden = self.hidden + self.target[i]
        self.lbl_hidden["text"] = self.hidden
    
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
        if letter in self.target:
            for i in range(len(self.target)):
                if self.target[i]==letter:
                    L[i]=letter
        else:
            self.change_board()
        self.lbl_hidden["text"] = "".join(L)
        self.letters_found.append(button)
        button["state"] = "disabled"
        
    #--------METHODS FOR TIMER--------
    def start_clock(self):
        """
        Start the timer if the game has started OR
        if the player is resuming the game.
        """
        counter = self.lbl_timer["text"] + 1
        self.lbl_timer.configure(text=counter)
        self.after_id = self.lbl_timer.after(1000, self.start_clock)

    def stop_clock(self):
        """Stop the timer when the game is paused"""
        self.lbl_timer.after_cancel(self.after_id)

    def reset_clock(self):
        """Reset the clock when starting a new game"""
        self.lbl_timer["text"] = 0
        
    #-----------------------------------
    #NEEDS TO DISABLE LETTER BUTTONS?
    def pause_game(self):
        """Stops the timer"""
        self.stop_clock()
        self.btn_pause.grid_remove()
        self.btn_resume.grid(row=500, column=0, columnspan=6)

    #WORKS (keep)
    def resume_game(self):
        """Starts the game if the game was paused"""
        self.start_clock()
        self.btn_resume.grid_remove()
        self.btn_pause.grid(row=500, column=0, columnspan=6)

    #WORKS (keep)
    def quit_game(self):
        """
        Quits the game. Prompts new window that asks
        if user is certain if they want to quit.    
        """
        self.lbl_ask.pack()
        if (self.quit_flag==0):
            self.quit_flag = 1
        else:
            self.window.destroy()

    #WORKS (just change state of buttons!)
    def reset_letters(self):
        """If the button disappeared in previous match, reset button"""
        for button in self.letters_found:
            button["state"] = "normal"
        self.letters_found = []
        
    #WORKS (opional?)
    def reset_board(self):
        self.stage = 0
        self.board_stage = "".join(brd.board_state[self.stage])
        self.lbl_board["text"] = self.board_stage

    #WORKS???
    def reset_game(self):
        """Resets the game, wiping out previous data"""
        self.reset_clock()
        self.reset_board()
        self.reset_letters()
        self.lbl_timer.pack_forget()
        self.lbl_board.pack_forget()
        self.frm_replay.pack_forget()
        self.lbl_category.pack_forget()
        self.lbl_hidden.pack_forget()
        self.frm_start.pack()

    #WORKS (keep)
    def play_again(self, btn):
        """Changes frame depending on user's choice"""
        #if btn is YES -> start from category screen
        #if btn is NO -> quit game?
        if btn["text"] == "YES":
            self.reset_game()
        else:
            self.window.destroy()

    #WORKS (Keep)
    def end_condition(self):
        """
        Change label based on conditions.

        The player WINS if tthe word has been found before
        the image was completed. The player LOSES if the
        image was completed before he word was found.
        """
        if (self.lbl_hidden["text"]==self.target):
            self.lbl_category["text"] = "YOU WIN!"
            self.stop_clock()
            self.show_replay_frame()
        elif (self.word_found()==False) and (self.stage==6):
            self.lbl_category["text"] = "Sorry! We were looking for: " + self.target
            self.stop_clock()
            self.show_replay_frame()


HangmanGUI()

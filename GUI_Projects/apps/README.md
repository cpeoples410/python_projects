HANGMAN TODO LIST

HANGMAN SCREENS
	- FRAME 1 -> Start Screen
		> Buttons that randomly selects a word
		  from selected category
		> Buttons that exits out of game
		> Hangman Image (Displays board?)
	- FRAME 2 -> Game Screen
		> Board display
			-> changes if person makes
			   incorrect guess
		> Empty letter spaces (_)
			-> Will reveal letters if player
			   guess correct letter(s)
		> Buttons for letters
			-> When selected, it will remove itself
			-> Buttons are disabled when game ends
		> Quit Button -> goes to Start Screen
			      -> Will first asks if user wants to leave

CLASSES
	- HangmanGUI   -> Class that runs game
	- WordButton   -> Class for category buttons
	- LetterButton -> Class for letter buttons

OPTIONAL FEATURES
	- Timer
		-> Display timer that will run automatically
		-> Stop timer when game is paused
		-> Resets timer when entering/quitting new game
	- Scoring
		-> Scoring is based on time and
		   the number of correct/incorrect guesses

Link to different types of fonts:
https://stackoverflow.com/questions/39614027/list-available-font-families-in-tkinter


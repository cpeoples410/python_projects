HANGMAN PROCESS

GUI
	- Display hangman image, letters, and empty lines

BOARD
	- Hangman board (50%)
		> Need to change board when player
		  guesses an incorrect letter / word (TESTING)
	- Number of empty lines ('_') for letters (80%, TESTING)
		> Need to separated line sequence if there are
		  any non-alphabetical characters

FUNCTIONS
	- showLetters 	-> replace spaces with letter if
			   player guesses correct letter
			   (80%, TESTING)
	- run 		-> runs the game using helper functions
			   (40%)
	- guessWord	-> Player will guess what the word is
			   (0%)
	- createLines	-> Hide all letters with underscores
			   (90%, TESTING)

SCORING (TBA)

OPTIONAL TASKS
	- Create Hangman class
	- Timer
	- startGame 	-> allow player to pick a category and
			   randomly select a word from that category
			   (Need to create method)
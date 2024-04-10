#!/usr/bin/env python3


#initialize variables before functions(s)
wrongGuesses = 7
guessed = False
correctLetters = []
wrongLetters = []

#function to process the guesses player enters
def processGuess(turn, guess, wrongGuesses):
	blanks = ''
	validLetter = False
	
	if guess in word:
		validLetter = True
			
	if validLetter == True:
		if turn != 1:
			correctLetters.append(guess)
			print('CORRECT!', 'The letter \'', guess, '\' is in the word.')
	else:
		if turn != 1:
			wrongLetters.append(guess)
			wrongGuesses = wrongGuesses - 1
			print('WRONG! \'', guess, '\' isn\'t in the word.')
		print('Guesses left: ', wrongGuesses)
		
	lettersGuessedCorrect = 0
	for letter in word:
		letterInWord = False
		if letter in correctLetters:
			letterInWord = True
			lettersGuessedCorrect = lettersGuessedCorrect + 1
				
		if letterInWord is True:
			blanks = blanks + letter + ' '
		else:
			blanks = blanks + '_ '
			
	print(blanks)
	return lettersGuessedCorrect, wrongGuesses

#variable and loop to prevent numbers in word
numberInWord = True
while numberInWord is True:
	word = input('Welcome to Hang Person! The gender-inclusive murder game that requires at least 2 players. Please note: this game is intended to be played for fun. DO NOT use this game to commit violent acts. Time to begin! Player 1, please enter a word for your opponent: ').lower()
#           ^
#           translates word value to lowercase

	#variable and loop to test each letter
	validCharacters = 0
	for letter in word:
		if letter.isdigit() is False:
			validCharacters += 1
	if len(word) == validCharacters:
		numberInWord = False
	else:
		print('I\'m sorry! Numbers break the gallows! Please try again using only letters.')



#hang person art
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']



#calls the processGuess function
processGuess(1, '', wrongGuesses)
turn = 2

#if enough guesses left, loop asking player for their guess
while guessed is False and wrongGuesses > 0:
	print(HANGMANPICS[len(wrongLetters)])
	print('Correct Letters: ', correctLetters)
	print('Wrong Letters: ', wrongLetters)
	
	guess = input('What letter would you like to guess? ').lower()
	#                                		      ^
	#						      translates guesses to lowercase
	
	newLetter = True
	if guess in wrongLetters:
		newLetter = False
	if guess in correctLetters:
		newLetter = False
			
	if newLetter is False:
		print('I\'m sorry, you already guessed that letter.')
		continue
	#prevents player form guessing numbers
	elif guess.isdigit() is True:
		print('I\'m sorry! Numbers break the gallows! Please try again entering only letters.')
		continue

	lettersGuessedCorrect, wrongGuesses = processGuess(turn, guess, wrongGuesses)

	if len(word) == lettersGuessedCorrect:
		print('Great Job! You\'ve guessed the word with', wrongGuesses, 'guesses left!')
		guessed = True
		
if wrongGuesses == 0:
	print('Too bad! The word was:', word)
	print('Ha ha, you lose!')
else:
	print('Congrats! You win!')
	
print('Please play again!')

#!/usr/bin/env python3

word = input('Welcome to Hang Person! The gender-inclusive murder game that requires at least 2 players. Please note: this game is intended to be played for fun. DO NOT use this game to commit violent acts. Time to begin! Player 1, please enter a word for your opponent: ')

#initialize variables
wrongGuesses = 7
guessed = False
correctLetters = ''
wrongLetters = ''
blanks = ''



for letter in word:
	blanks = blanks+'_ '
	
print(blanks)

print('Guesses remaining: ', wrongGuesses)

while guessed is False and wrongGuesses > 0:

	print('Correct Letters: ', correctLetters)
	print('Wrong Letters: ', wrongLetters)
	
	guess = input('What letter would you like to guess? ')
	
	newLetter = True
	for letter in wrongLetters:
		if guess == letter:
			newLetter = False
	for letter in correctLetters:
		if guess == letter:
			newLetter = False
			
	if newLetter is False:
		print('I\'m sorry, you already guessed that letter.')
	else:	
	
		blanks = ''
		validLetter = False
		
		for letter in word:
			if letter == guess:
				validLetter = True
				
		if validLetter == True:
			correctLetters = correctLetters + guess
			print('CORRECT!', 'The letter \'', guess, '\' is in the word.')
		else:
			wrongLetters = wrongLetters + guess
			wrongGuesses = wrongGuesses - 1
			print('WRONG! \'', guess, '\' isn\'t in the word.')
			print('Guesses left: ', wrongGuesses)
			
		lettersGuessedCorrect = 0
		for letter in word:
			letterInWord = False
			for ltr in correctLetters:
				if letter == ltr:
					letterInWord = True
					lettersGuessedCorrect = lettersGuessedCorrect + 1
					
			if letterInWord is True:
				blanks = blanks + letter + ' '
			else:
				blanks = blanks + '_ '
				
		print(blanks)
		
		if len(word) == lettersGuessedCorrect:
			print('Congrats! You\'ve guessed the word with', wrongGuesses, 'guesses left!')
			guessed = True
		
if wrongGuesses == 0:
	print('Too bad! The word was:', word)
	print('Ha ha, you lose!')
else:
	print('Congrats! You win!')
	
print('Please play again!')

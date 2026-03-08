#Hangman Game Project
import random

#eventually, create word banks based on different lengths of words and ask user for input on which lenght they want

#create a word bank (start with 6 letters)

word_bank = ['python', 'guitar', 'coffee', 'breeze', 'window', 'galaxy', 'jungle', 'silver', 'orchid', 'poetry']

#select which word from word bank

chosen_index = random.randint(0, len(word_bank) - 1)
chosen_word = word_bank[chosen_index]
print(chosen_word)

#main game
#display current state of word: blanks for unrevaled letters

#limited number of incorrect guesses - typically X amount

#take letter guess from user - make sure hasn't already been guessed, and must be a letter. make it lowercase

#reveal if this letter is part of word or not

#repeat process until either number of gusses used up, or word is guessed  orrectyl


#ask if user wnats to repeat the game. 



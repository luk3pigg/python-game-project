import game_functions as gf

#additional ideas to focus on later:
#eventually, create word banks based on different lengths of words and ask user for input on which lenght they want
#adjust number of lives: difficulty setting
#adjust times/time depending on number ie 1 is time, times is 2+


#Main lessons:
    
#Alternative to while True and return in functions, is while True and break.


#create a word bank (start with 6 letters)

word_bank = ['python', 'guitar', 'coffee', 'breeze', 'window', 'galaxy', 'jungle', 'silver', 'orchid', 'poetry']



#starting the game
total_session_games = 0
game_active = gf.start_game()
while game_active:
    chosen_word = gf.select_word(word_bank = word_bank)
    #would you like to know the rules of the game yes: y n: n
    #Choose your settings: lives, word length, timer?
    lives = 6
    correct_guesses = 0
    guessed_letters = []
    display_word = ['_'] * len(chosen_word)
    total_guesses = 0
    game_won = False
    #main game 
    while lives > 0 and not game_won: 
        print(f"\n\n\nYou currently have {lives} lives.")
        print(f"You currently have {correct_guesses} correct guesses.")
        if total_guesses > 0:
            print("You have guessed the following letters:")
            print(*guessed_letters)
        print("Here's what you know so far:")
        print(*display_word)
        
        letter_guess, total_guesses = gf.letter_validation(total_guesses=total_guesses, guessed_letters=guessed_letters)
        lives, correct_guesses, game_won = gf.guess_result(guessed_letters, chosen_word, display_word, letter_guess=letter_guess, lives=lives, correct_guesses=correct_guesses, game_won=game_won)
    
        
    
    if game_won:
        print(f"You won! The secret word was {chosen_word}!")
    else:
        print(f"Oh no! You have run out of lives! The correct word was {chosen_word}")
    #stats
    total_session_games += 1
    print(f"Total games you have played in this session: {total_session_games}")
    #restart game option
    game_active = gf.restart_game()
    





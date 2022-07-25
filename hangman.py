# author: Wei Feng Tan
# date: 4/11/22 
# file: hangman.py is a program that resembles the hangman game. Guess correctly to win. 
# input: The user can input numbers and strings. 
# output: The output will consist of strings that tell the user if they guessed correcrly or not.


import random


dictionary_file = "dictionary.txt"  # making a dictionary.txt in the same folder where hangman.py is located

# Functions

# importing the dictionary
# the dictionary keys are word sized from 1-12 and the values are lists of words
# for exmaple dictionary = { 2 : ['Ms', 'ad'], 3 : ['cat', 'dog', 'sun']}
# if a word has the size more than 12 letters, put into list with the key equal to 12. 
def import_dictionary (filename) :
    dictionary = {2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: [], 10: [], 11: [], 12: []}
    words = []
    max_size = 12
    try :
        open_dict = open('/Users/alan/Projects/Hangman/dictionary.txt')
        words = open_dict.read().split("\n")
        words = list(map(str.strip, words))
    except Exception :
        print ("there is an error")
        pass

# sorting the words into the dictionary based on how many letters that it has.
    for i in range (2,13):
        for j in words:
            if (len(j) == i):
                dictionary[i].append(j)
            elif (len(j) > 12) :
                dictionary[12].append(j)
    
    
    return dictionary

# print the dictionay (for debugging)
def print_dictionary (dictionary) :
    max_size = 12
    print (dictionary)
    
# get options size and lives from the user, use try-except statements for wrong input
def get_game_options () :
    try :
        print ("Please choose a size of a word to be guessed [3 - 12, default any size]:")
        user_input = int(input())
        if (user_input < 3) or (user_input > 12) :
            word_size = random.randint(3, 12)
        else :
            word_size = user_input
        print (f"The word size is set to {word_size}.")
    except Exception:
        word_size = random.randint(3, 12)
        print ("the length of the word is", word_size)

# This second part is how many lives that the user wants.
    try :
        print ("Please choose a number of lives [1 - 10, default 5]:")
        user_input2 = int(input())
        if (user_input2 < 1) or (user_input2 > 10) :
            lives = 5
        else :
            lives = user_input2
        print (f"You have {lives} lives.")
    except Exception :
        lives = 5
        print (f"You have {lives} lives.")

    return (word_size, lives)

def split (word) :
    return [char for char in word]
    

# MAIN

if __name__ == '__main__' :

    # make a dictionary from a dictionary file
    dictionary = import_dictionary(dictionary_file)

    # print dictionary for debugging 
    #print_dictionary(dictionary)

    game_start = True
    while (game_start) :
        # print out the game introduction and getting size of word and how many lives
        print ("**********************************")
        print ("*                                *")
        print ("*  Welcome to the Hangman Game!  *")
        print ("*                                *")
        print ("**********************************")
        print ("\n")
        size, life = get_game_options()

        # selecting a word from dictionary
        word_list = []
        game_word = " "
        word_list = dictionary[size]
        game_word = random.choice(word_list)
        game_word = game_word.lower()

        # START GAME LOOPS
        game_start = True
        game_continue = True
        index_list = []
        letter_guesses = []
        hidden_letters = split(game_word)
        winner = len(game_word)
        #print (hidden_letters)
        place_holders = []
        for i in range(len(game_word)) :
            place_holders.append("__ ")
        hypen = "-"
        if hypen in hidden_letters :
            hypen_index = hidden_letters.index(hypen)
            place_holders[hypen_index] = "-"
            winner -= 1
        
    
        #print (place_holders)
        wrong_guess = 0
        
        while (game_continue) :
        
            print("Letters chosen:", end = " ")

            # for loop to print out the guesses that the player has made
            for x in range(len(letter_guesses)):
                if (x == 0):
                    print(letter_guesses[x], end = "")
                else :
                    print(", " + letter_guesses[x], end = " ")
                

            # print statements for the lifes
            print ("\n")
            #print ("__ " * size, end = " ")
            for y in range(len(place_holders)):
                       print(place_holders[y], end = " ")
            print (f"lives: {life}", end = " ")
            print ("X" * wrong_guess, end = "")
            print ("O" * life)
            if (life <= 0) :
                    game_word = game_word.upper()
                    print("You lost! The word is " + game_word + "!")
                    game_continue = False
                    break
            if (winner == 0) :
                game_word = game_word.upper()
                print ("Congratulations!!! You won! The word is " + game_word + "!")
                game_continue = False
            else :
                # prompt user input and check if the input meets conditions
                print("Please choose a new letter >")
                guess = input()
                
                not_alpha = False
                while (not_alpha == False) :
                    check = guess.upper()
                    if check in letter_guesses  :
                        print("You have already chosen this letter.")
                        print("Please choose a new letter >")
                        guess = input()
                    else:
                        if (guess.isalpha()) and (len(guess) == 1) :
                            alpha = guess.upper()
                            lower = guess.lower()
                            letter_guesses.append(alpha)
                            not_alpha = True
                        else :
                            print("Please choose a new letter >")
                            guess = input()
                 
                # check if the guessed letter is in the word.
                index_list = []
                lower = guess.lower()
                if lower in hidden_letters :
                    print("You guessed right!") 
                    #index = hidden_letters.index(lower)
                    for i in range(len(hidden_letters)) :
                        if (lower == hidden_letters[i]) :
                            index = i
                            index_list.append(index)
                            
                            
                    for j in range(len(index_list)) :
                        upper = lower.upper()
                        elements = index_list[j]
                        place_holders[elements] = upper
                        winner -= 1 
                    
                    
                else :
                    print("You guessed wrong, you lost one life.")
                    wrong_guess += 1
                    life -= 1
                


        print("Would you like to play again [Y/N]?")
        start = input()
        start = start.upper()
        if (start == "Y") :
            game_start = True
            game_continue = True
        else :
            game_start = False
            print ("Goodbye!")
        
        
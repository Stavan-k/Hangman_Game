import hangman_body
import word_list
import random

aval_guess = 6  # Number of available guesses
random_word = ""  
wrong_guess = 0

def get_word():
    return random.choice(word_list.words)

def start_game():
    global random_word, display_word
    random_word = get_word()
    display_word = ['_' for _ in random_word]
    
    print("Let's start playing Hangman! Available lives:", aval_guess)
    print("Your word has", len(random_word), "letters")
    print(' '.join(display_word))

def check_value(letter):
    global aval_guess, wrong_guess, display_word
    if letter in random_word:
        print("Correct letter chosen!")
        for i in range(len(random_word)):
            if random_word[i] == letter:
                display_word[i] = letter
        print(' '.join(display_word))
        if '_' not in display_word:
            print("Congratulations! You guessed the word:", random_word)
            return True
        return False
    else:
        wrong_guess += 1
        aval_guess -= 1
        print(hangman_body.hangman_body_list[wrong_guess - 1])
        print("Oops, wrong guess! Available guesses:", aval_guess)
        if aval_guess == 0:
            print("Sorry, you lost! The word was:", random_word)
            return True
        return False

def User_input():
    return input("\nEnter a letter: ")

play = False
first = 1
while not play and aval_guess > 0:
    if first == 1:
        start_game()
        first += 1
    user_input = User_input()
    play = check_value(user_input)

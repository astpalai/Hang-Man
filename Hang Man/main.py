
import os
import time
import random

def play_again():
    pass

def play_hangman(word):
    display = '_'*len(word)
    count = 0
    limit = 6

    while limit:
        if limit == 6:
            print('   _____  \n'
                  '  |     | \n'
                  '  |     | \n'
                  '  |       \n'
                  '  |       \n'
                  '  |       \n'
                  '  |       \n'
                  '__|__\n')
            print('The word to guess: ' + display)
            print('Guesses remaining: ' + str(limit))

        time.sleep(3)
        limit-=1
    

    


    #thanos was here

def hangman():
    #print('Welcome to hangman.')
    #time.sleep(1)
    #print('Game is about to start.')
    #time.sleep(1)
    #print('Best of luck!! \n')
    #time.sleep(1)

    words_to_guess = ['january', 'feb', 'march', 'april', 'may']
    word = random.choice(words_to_guess)
    play_hangman(word)



#main
if __name__ == '__main__':
    hangman()
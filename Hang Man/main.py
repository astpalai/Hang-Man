import os
import sys
import time
import random


CURSOR_UP_ONE = '\x1b[1A' 
ERASE_LINE = '\x1b[2K'
def delete_last_lines(n=1): 
    for _ in range(n): 
        sys.stdout.write(CURSOR_UP_ONE) 
        sys.stdout.write(ERASE_LINE)

def play_again():
    answer = ''
    while answer.lower() != 'y' or answer.lower() != 'n':
        answer = input('\nWould you like to play again (y/n)')
        if answer == 'y':
            os.system('cls')
            return True
        elif answer == 'n':
            os.system('cls')
            return False
        else:
            print('Incorrect input. Try again \n')
            time.sleep(2)
            os.system('cls')

def play_hangman(word):
    display = '_'*len(word)
    letters_guessed = []
    count = 0
    limit = 6

    print('   _____  \n'
          '  |     | \n'
          '  |     | \n'
          '  |        \n'
          '  |        \n'
          '  |        \n'
          '  |        \n'
          '__|__      \n')

    while count<limit:
        if limit-count == 1:
            print('The word to guess: ' + display + ', ' + str(limit-count) + ' Guess remaining')
        else:
            print('The word to guess: ' + display + ', ' + str(limit-count) + ' Guesses remaining')
        print('Letters guessed already: '+str(letters_guessed))
        
        letter = ''
        while len(letter)>1:
            letter = input('Guess a letter :')
            print('You need to input one character. Try again')
            time.sleep(1)
            delete_last_lines(1)
            
        
        if letter in letters_guessed:
            print('Letter checked already. Guess again')
            time.sleep(1)
            delete_last_lines(4)
            continue
        letters_guessed.append(letter)


        if letter in word:        
            for index,value in enumerate(word): # fills the display with the letter guessed
                if letter.lower() == value:
                    display = display[:index] + letter + display[index+1:]
            delete_last_lines(3)
        else:
            print('Sorry, the letter doesnt exist.')
            os.system('cls')
            count+=1
            match count:
                case 1:
                    print('   _____   \n'
                          '  |     |  \n'
                          '  |     |  \n'
                          '  |     O  \n'
                          '  |        \n'
                          '  |        \n'
                          '  |        \n'
                          '__|__      \n')
                    
                case 2:
                    print('   _____   \n'
                          '  |     |  \n'
                          '  |     |  \n'
                          '  |     O  \n'
                          '  |     |  \n'
                          '  |        \n'
                          '  |        \n'
                          '__|__      \n')

                case 3:
                    print('   _____   \n'
                          '  |     |  \n'
                          '  |     |  \n'
                          '  |     O  \n'
                          '  |    /|  \n'
                          '  |        \n'
                          '  |        \n'
                          '__|__      \n')

                case 4:
                    print('   _____   \n'
                          '  |     |  \n'
                          '  |     |  \n'
                          '  |     O  \n'
                          '  |    /|\ \n'
                          '  |        \n'
                          '  |        \n'
                          '__|__      \n')

                case 5:
                    print('   _____   \n'
                          '  |     |  \n'
                          '  |     |  \n'
                          '  |     O  \n'
                          '  |    /|\ \n'
                          '  |    /   \n'
                          '  |        \n'
                          '__|__      \n')
                case 6:
                    print('   _____   \n'
                          '  |     |  \n'
                          '  |     |  \n'
                          '  |     O  \n'
                          '  |    /|\ \n'
                          '  |    / \ \n'
                          '  |        \n'
                          '__|__      \n')
                    print('YOU LOST,the word was '+ word)
                    break
        if display == word:
            print('YOU WON,the word was '+ word)
            break
    

def hangman():
    print('Welcome to hangman.')
    time.sleep(1)
    print('The game is about to start.')
    time.sleep(1)
    print('Best of luck!! \n')
    time.sleep(2)
    os.system('cls')

    words_to_guess = ['tenacious', 'repristinate', 'eruct', 'gul', 'alluvion' , 'superannuated',
     'rasorial', 'lambent', 'caravel', 'gridiron', 'aorta', 'quixotic', 'bulwark', 'syzygy', 'modus ponens',
      'pizazz', 'nonpartisan', 'romaji', 'skijoring', 'ejecta', 'vellicate', 'cranreuch', 'oppugn', 'oolong',
       'vigesimal']

    play = True
    while play:
        word = random.choice(words_to_guess)
        play_hangman(word)
        play = play_again()

    print('Thanks For Playing! Hope to see you again!')
    time.sleep(3)
    exit()



#main
if __name__ == '__main__':
    hangman()
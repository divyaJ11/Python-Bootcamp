import random
from words import word_list #contains list of words used in game

#method to pick a random word from given list
def get_word():
    word = random.choice(word_list).upper()
    return word

#logic of game
def play(word):
    print("LET'S PLAY HANGMAN")
    #print(word.upper())
    word_completion = "_"*len(word)
    guess_letters = []  #list to store all guessed letters
    guess_words= []     #list to store all guessed words 
    guessed = False
    tries = 6   #number of tries is 6
    print(display_hangman(tries))   #display the current hangman stage
    print(word_completion)
    while not guessed and tries>0 :
        #taking input
        guess = input("\nPlease enter your guess : ").upper()
        
        if len(guess) == 1 and guess.isalpha() :
            if guess in guess_letters:
                print("You have already entered this letter. Try again.")
            elif guess in word:
                print("Yay,",guess ," is in the word!")
                
                #storing the positions where guess occurs in word
                #enumerate returns the index coressponding to the letters in word
                indices=[ index for index, letter in enumerate(word) if guess == letter]

                #converting string to list for modification as strings are immutable
                listWordCompletion = list(word_completion)

                #replacing blanks with guessed letter
                for index in indices:
                    listWordCompletion[index] = guess
                
                #convert list to a string again
                word_completion="".join(listWordCompletion)

                #if all letters have been guessed, set guessed to True
                if "_" not in word_completion:
                    guessed=True

                #add the guess to the guessed letters
                guess_letters.append(guess)

            elif guess not in word:
                print(guess," is not in the word.")
                tries -= 1  #deduct number of tries
                guess_letters.append(guess)
        elif len(guess)==len(word) and guess.isalpha():
            if guess in guess_words:
                print("You have already guessed ", guess, ". Try again.")
            elif guess != word :
                print(guess," is not the correct word.")
                guess_words.append(guess)
                tries-=1    #deduct number of tries
            else:
                print("Good job, you guessed it !")
                guessed=True
                word_completion=word
        else:
            print(" Invalid entry !")

        print(display_hangman(tries))
        print(word_completion)
        
    if guessed:
        print("Congrats! You won :)")
    else:
        print(word)
        print("You ran out of chances :( \tBetter luck next time !")


#returns current hangman state        
def display_hangman(tries):
    stages=[
         #stage 6
        """
        -------------
        |           |
        |           |
        |           0
        |          \\|/
        |           |
        |          / \\
        |
        |
    ---------
        """
        ,
        #stage 5
        """
        -------------
        |           |
        |           |
        |           0
        |          \\|/
        |           |
        |          / 
        |
        |
    ---------
        """
        ,
        #stage 4
        """
        -------------
        |           |
        |           |
        |           0
        |          \\|/
        |
        |
        |
    ---------
        """
        ,
        #stage 3
        """
        -------------
        |           |
        |           |
        |           0
        |          \\|
        |
        |
        |
    ---------
        """
        ,
        #stage 2
        """
        -------------
        |           |
        |           |
        |           0
        |           |
        |
        |
        |
    ---------
        """
        ,
        #stage 1
        """
        -------------
        |           |
        |           |
        |           0
        |
        |
        |
        |
    ---------
        """
        ,
        #stage 0
        """
        -------------
        |           |
        |           |
        |
        |
        |
        |
        |
        |
        |
    ---------
        """
    ]
    return(stages[tries])



def main():
    word = get_word()
    play(word)
    
    #loop for playing again
    while input("\nDo you want to play again (Y/N): ").upper() =="Y":
        word = get_word()
        play(word)
    print("Thank you for playing !!")


if __name__ == "__main__":
    main()

# Hangman game

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for letter in secretWord:
        if (letter not in lettersGuessed):
            return False;
    return True;

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    word = '';
    for i in range(len(secretWord)):
        if (secretWord[i] in lettersGuessed):
            word = word + secretWord[i];
        else:
            word = word + '_';
    return word;

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    total = 'abcdefghijklmnopqrstuvwxyz';
    left = '';
    for letter in total:
        if (letter not in lettersGuessed):
            left = left + letter;
    return left;

def hangman():
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print('Welcome to the game Hangman!');
    play = True;
    secretWord = '';
    while (play == True):
        secretWord = chooseWord(wordlist).lower();
        print('I am thinking of a word that is ', str(len(secretWord)), ' letters long');
        guesses = 8;
        guessed = False;
        guess = '';
        lettersGuessed = '';
        while (guesses>0):
            print('-----------');
            print('You have ', guesses, ' left');
            print('Available Letters: ', getAvailableLetters(lettersGuessed));
            guess = input('Please guess a letter: ');
            if guess in lettersGuessed:
                print('Oops! You\'ve already guessed that letter: ', getGuessedWord(secretWord, lettersGuessed));
            else:
                lettersGuessed = lettersGuessed + guess;
                if guess not in secretWord:
                    print('Oops! That letter is not in my word: ', getGuessedWord(secretWord, lettersGuessed));
                    guesses = guesses - 1;
                else:
                    print('Good guess: ', getGuessedWord(secretWord, lettersGuessed));
                    if isWordGuessed(secretWord, lettersGuessed):
                        guessed = True;
                        break;
        print('------------');
        if guessed:
            print('Congratulations, you won!');
        else:
            print('Sorry, you ran out of guesses. The word was ', secretWord);
        play = input('Do you want to play again (Y/N): ');
        if (play=='Y')or(play=='y')or(play==1)or(play==True):
            play = True;
        else:
            play = False;

hangman();

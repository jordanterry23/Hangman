#from nltk.corpus import words
import random
import keyboard
import string
import os

#answer = str(random.sample(words.words(), 1))

wordList = open("words.txt").readlines()
answer = random.choice(wordList).strip()

display = []
for char in answer:
    if char == " ":
        display += " "
    else:
        display += "_"
guessedLetters = []
guessedWords = []
gameOver = False
win = False
incorrect = 0

def GetYN(message):
    print(message)
    alphabet = list(string.ascii_letters)
    while (True):
        for letter in alphabet: 
            if(keyboard.is_pressed(letter)):
                if (letter == "y" or letter == "Y"):
                    return True
                elif (letter == "n" or letter == "N"):
                    return False

def BuildBoard():
    global incorrect
    global win
    print("+-----|     ")
    if(win):
        print("|   (^_^)   ")
    elif(incorrect > 6):
        print("|   (x_x)   ")
    elif(incorrect > 0):
        print("|   (o_o)   ")
    else:
        print("|           ")
    if(win):
        print("|    \|/    ")
    elif(incorrect > 3):
        print("|    /|\    ")
    elif(incorrect > 2):
        print("|    /|     ")
    elif(incorrect > 1):
        print("|     |     ")
    else:
        print("|           ")
    if(incorrect > 5 or win):
        print("|    / \    ")
    elif(incorrect > 4):
        print("|    /      ")
    else:
        print("|           ")
    print("|___________")
    print()

def DisplayWord():
    word = ""
    for char in display:
        word += char
    print(word)
    print()

def DisplayGuessed():
    global guessedLetters
    global guessedWords
    if (guessedLetters.count != 0):
        letters = ""
        for char in guessedLetters:
            letters += (char + "")
        print("Guessed Letters: " + letters)
    if(guessedWords.count != 0):
        words = ""
        for word in guessedWords:
            words += (word + ", ")
        print("Guessed Words: " + words)

def DisplayIncorrect():
    print("Incorrect Guesses: " + str(incorrect))

def Check(newGuess):
    global win
    global incorrect
    global guessedWords
    #Is guess letters?
    if(newGuess.isalpha and newGuess != ""):
        #does the input contain more than one letter?
        if(guessedLetters.__contains__(newGuess)):
            print("You already guessed that letter! Try again!")
            return
        if(len(guess) <= 1):
            guessedLetters.append(guess)
            'Does the word contain this letter?'
            found = False
            for i in range(len(answer)):
                if(answer[i] == guess):
                    display[i] = guess
                    found = True
            if(found == False):
                incorrect += 1
                print("None of those! Try again!")
            check = ""
            for char in display:
                check += char
            if (answer == check):
                win = True
                return
        elif(guess == answer):
            guessedWords += guess
            win = True
            return
        else:
            if(guessedWords.__contains__(guess)):
                print("You already guessed that word! Try again!")
                return
            guessedWords.append(guess)
            incorrect += 1
            print("Nope! Try again!")
    else:
        print("Please guess a letter.")

print("Welcome to Hangman!")
while(gameOver != True and win != True):
    if(incorrect >= 7):
        gameOver = True
        break
    else:
        print()
        BuildBoard()
        DisplayWord()
        DisplayGuessed()
        DisplayIncorrect()
        guess = input("What is your guess?\n")
        Check(guess)
        os.system('cls')

BuildBoard()
print(answer)
DisplayGuessed()
DisplayIncorrect()
if(win == True):
    print("You win!")
else:
    print("Game Over!")

again = GetYN("Would you like to play again (y/n)?")

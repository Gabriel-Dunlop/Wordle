import random
from tkinter.constants import WORD

def userInput(randomWord):
    userWord = input("What is Todays Word? ")
    print(userWord)

def readFromFile():
    wordTxt = open('words.txt', 'r')
    wordTxt = wordTxt.readlines()
    wordList = []
    for word in wordTxt:
        if word != "\n":
            wordList.append(word.strip("\n"))
    word = (wordList[random.randint(0, len(wordList)-1)])
    return word

def board():
    board =["#####","#####","#####","#####","#####","#####"]
    board_rows = [list(row) for row in board]
    return(board_rows)

testing = board()
file = open(WORD)
randomWord = "prank"
emptyString = ""
j = 0
z = 0
  
def checkword(userWord, randomWord):
    if userWord == randomWord:
        return "You win!"
    return None

while z < 6:
    userWord = input("Guess the word: ")
    result = checkword(userWord, randomWord)
    if result == "You win!":
        print(result)
        break
    for i in range(0, len(userWord)):
        if userWord[i] == randomWord[i]:
            testing[j][i] = randomWord[i]
            emptyString += userWord[i]
            print(testing[j][i])
            continue      
        if userWord[i] in randomWord:
            print("it contains!")
        if userWord[i] not in randomWord:
            print("does not contain!")
    print(emptyString)
    j += 1
    z += 1
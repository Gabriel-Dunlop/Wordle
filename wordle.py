import random

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
# randomWord = readFromFile()
# userInput(randomWord)

test = "test"
userWord = "spank"
randomWord = "prank"
emptyString = ""
for i in range(0, len(userWord)):
    if userWord[i] == randomWord[i]:
        emptyString += randomWord[i]
        continue      
    if userWord[i] in randomWord:
        print("it contains!")
    if userWord[i] not in randomWord:
        print("does not contain!")
print(emptyString)




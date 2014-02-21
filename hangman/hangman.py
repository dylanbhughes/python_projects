# Preamble
from random import choice
from random import randint
import turtle
lettersguessed = []

def hangman(Computer, Graphic, Length=5):
    """
    This function starts a game where the computer is choosing the word
    if Computer is True and you choose the word if Computer is False.
    The words with be of length length.
    Graphics is either True or False and indicates whether the man is drawn.
    It returns True if the computer wins and False if the computer Looses.
    """
    myword = ""
    guessedletter = ""
    print("Let's play a game....how about hangman?")
    if Computer == True:
        print("I'll guess the word.")
        print("I'm thinking......")
        myword = pickword(Length)
        displayword = ['_']*len(myword)
        print("Okay, got it! I have a", Length, "letter word.")
        result = getguess(myword, displayword, Graphic)
        if result == True:
            print("You lose! HAHAHAHAHAHAHAHAHA")
            print('By the way, the word was ' + myword + '. Just so you know.')
        else:
            print('Congratuations! You win!')        
    else:
        print("Okay, fine. You pick the word.")
        computerguess(Length, Graphic)


def computerguess(Length, Graphic):
    alphabet = 'qwertyuiopasdfghjklzxcvbnm'
    numberofguesses = 0
    displayword = ['_']*Length
    alreadyguessed = []
    print("Just to be clear, you have picked a", Length, "letter word.")
    print(displayword)
    print("I have 10 guesses total to get the word right.")
    print("Please type only 'Y' or 'N' to respond to my questions.")
    while numberofguesses < 10:
        guessedletter = alphabet[randint(0,24)]
        guessedletter = computeralreadyguess(guessedletter, alreadyguessed)
        alreadyguessed.append(guessedletter)
        print('Is there an', guessedletter, 'in the word?')
        response = getYN()
        if response == 'y':
            print('Nice!')
            displayresponse = computerdisplayword(displayword, guessedletter)
            print('Solid. I now have:', displayresponse)
        else:
            numberofguesses+=1
            if Graphic == True:
                drawhangman(numberofguesses)
            print('Dammit.')
    if numberofguesses == 10:
        return('I lose. =[.')

def computerdisplayword(displayword, guessedletter):
    # Function to place correct letter in displayword.
    position = input("What number blank space does the correctly guessed letter occupy? ")
    Length = len(displayword)
    position = verifyposition(position, Length)
    displayword[position] = guessedletter
    return displayword

def verifyposition(position, Length):
    possibilities = '123456789'
    if position not in possibilities:
        print("Please type a valid position, 1-"+str(Length)+".")
        position = verifyposition(input("What number blank space does the correctly guessed letter occupy? "), Length)
    position = int(position)
    if position > Length:
        print("Please type a valid position, 1-"+str(Length)+".")
        position = verifyposition(input("What number blank space does the correctly guessed letter occupy? "), Length)
    return position
        
            
def computeralreadyguess(guessedletter, alreadyguessed):
    alphabet = 'qwertyuiopasdfghjklzxcvbnm'
    if guessedletter in alreadyguessed:
        guessedletter = alphabet[randint(0,24)]
        guessedletter = computeralreadyguess(guessedletter, alreadyguessed)
    else:
        return guessedletter

def getYN():
    options = 'yn'
    response = input("Y/N:")
    response = response.lower()
    if response not in options:
        print("ONLY TYPE 'Y' OR 'N'!!!!")
        print('Try again: ')
        response = getYN()
    elif response == "":
        print("ONLY TYPE 'Y' OR 'N'!!!!")
        print('Try again: ')
        response = getYN()
    elif len(response) > 1:
        print("ONLY TYPE 'Y' OR 'N'!!!!")
        print('Try again: ')
        response = getYN()        
    else:
        return response
    

def readindict(filename):
    # Read the file of words
    # Returns all words in ???
    f = open(filename, 'r', encoding='utf-8')
    # f is a pointer to the file on the disk. This is called a file handle.
    words = {}
    for word in f:
        word = word.strip().lower()
        if word.endswith("'s"):
            word = word[:-2]
        words[word] = len(word)
        l = len(word)
        if l in words:
            li = words[l]
        else:
            li = []
        li.append(word)
        words[l] = li   
    f.close()
    return words

def pickone(dictionary):
    return choice(dictionary)

def pickword(Length):
    """
    This function picks a word for hangman randomly from a list of words. The
     dictionary for hangman consists of words of length 4 or 5.
    """
    allwords = readindict('american-english')
    allwords = allwords[Length]
    myword = pickone(allwords)
    return myword

def getguess(myword, displayword, Graphic):
    # Function that continues to receive a user's guess until they lose or win.
    guessedletter = ""
    numberofguesses = 0
    while numberofguesses < 10:
        guessedletter = input("Okay, guess a letter: ")
        guessedletter = validinput(guessedletter)
        guessedletter = guessedbefore(guessedletter)
        print("You guessed", guessedletter + "...okay, let me see.")
        evaluation = evaluateguess(myword, displayword, guessedletter, numberofguesses, Graphic)
        displayword = evaluation[0]
        numberofguesses = evaluation[1]
        print(displayword, " " + str(numberofguesses) + "/10 Wrong Guesses")
        if '_' not in displayword:
            return False
    if numberofguesses == 10:
        return True

def guessedbefore(guessedletter):
    # Function that determines if the user has guessed that letter previously.
    for letter in lettersguessed:
        if guessedletter == letter:
            print("You already guessed that! Try again.")
            guessedletter = input("Okay, guess a letter: ")
            guessedletter = guessedbefore(guessedletter)
    return guessedletter

def evaluateguess(myword, displayword, guessedletter, numberofguesses, Graphic):
    # Function that evaluates the users guess and returns a result.
    lettersguessed.append(guessedletter)
    for i in range(len(myword)):
        if guessedletter == myword[i]:
            print("Yes, there is an", guessedletter, "in the word.")
            displayword[i] = guessedletter
    if guessedletter not in myword:
        print('Nope. You suck. Try again.')
        numberofguesses += 1
        if Graphic == True:
            drawhangman(numberofguesses)
    return [displayword, numberofguesses]

def validinput(guessedletter):
    # This is a function to make sure that the user is not a moron.
    alphabet = 'qwertyuiopasdfghjklzxcvbnm'
    guessedletter = guessedletter.lower()
    if guessedletter not in alphabet:
        print('You idiot. I said guess a LETTER. As in: a,b,c,d,e,f, ect.')
        guessedletter = input('Try again: ').lower()
        guessedletter = validinput(guessedletter)
    elif len(guessedletter) != 1:
        print('You idiot. ONE LETTER AT A TIME.')
        guessedletter = input('Try again: ').lower()
        guessedletter = validinput(guessedletter)
    return guessedletter

def drawhangman(numberofguesses):
    wn = turtle.Screen()
    turtle.mode('logo')
    peter = turtle.Turtle()
    peter.hideturtle()
    peter.speed(10)
    
    def square(sidelength):
        # Draw square. 
        for i in range(4):
            peter.forward(sidelength)
            peter.right(90)
    
    def drawline(turn, distance):
        # Draw a line.
        if turn < 0:
            peter.left(abs(turn))
        elif turn > 0:
            peter.right(turn)
        peter.forward(distance)
        if turn < 0:
            peter.right(abs(turn))
        elif turn > 0:
            peter.left(turn)        
    
    def move(turn, distance):
        # Moving the pen.
        peter.penup()
        if turn < 0:
            peter.left(abs(turn))
        elif turn > 0:
            peter.right(turn)
        peter.forward(distance)
        if turn < 0:
            peter.right(abs(turn))
        elif turn > 0:
            peter.left(turn)
        peter.pendown()
    
    def drawgallows():
        # Draw the gallows.
        move(-90, 150)
        move(180, 100)
        square(75)
        move(0, 75)
        move(90, 37.5)
        drawline(0,200)
        drawline(90, 150)
        drawline(180, 25)
    
    def drawhead():
        # Draw the head.
        move(-90, 17.5)
        move(180, 35)
        square(35)
    
    def drawbody():
        # Draw the body.
        move(90, 17.5)
        drawline(180, 75)
    
    def drawlleg():
        drawline(225, 50)
        move(45, 50)
    
    def drawrleg():
        drawline(135, 50)
        move(-45, 50)
    
    def drawlfoot():
        move(225, 50)
        drawline(-45, 10)
        move(135, 10)
        move(45, 50)
    
    def drawrfoot():
        move(135, 50)
        drawline(45, 10)
        move(-135, 10)
        move(-45, 50)
        move(0, 50)
    
    def drawlarm():
        drawline(-45, 50)
        move(135, 50)
    
    def drawrarm():
        drawline(45, 50)
        move(-135, 50)
    
    def drawkill():
        move(0,25)
        move(-90, 17.5)
        drawline(45, 49)
        move(-90, 35)
        drawline(135, 49)
    
    if numberofguesses == 1:
        drawgallows()
    elif numberofguesses == 2:
        drawgallows()
        drawhead()
    elif numberofguesses == 3:
        drawgallows()
        drawhead()        
        drawbody()
    elif numberofguesses == 4:
        drawgallows()
        drawhead()        
        drawbody()        
        drawlleg()
    elif numberofguesses == 5:
        drawgallows()
        drawhead()        
        drawbody()        
        drawlleg()        
        drawrleg()
    elif numberofguesses == 6:
        drawgallows()
        drawhead()        
        drawbody()        
        drawlleg()        
        drawrleg()        
        drawlfoot()
    elif numberofguesses == 7:
        drawgallows()
        drawhead()        
        drawbody()        
        drawlleg()        
        drawrleg()        
        drawlfoot()        
        drawrfoot()
    elif numberofguesses == 8:
        drawgallows()
        drawhead()        
        drawbody()        
        drawlleg()        
        drawrleg()        
        drawlfoot()        
        drawrfoot()        
        drawlarm()
    elif numberofguesses == 9:
        drawgallows()
        drawhead()        
        drawbody()        
        drawlleg()        
        drawrleg()        
        drawlfoot()        
        drawrfoot()        
        drawlarm()        
        drawrarm()
    elif numberofguesses == 10: 
        drawgallows()
        drawhead()        
        drawbody()        
        drawlleg()        
        drawrleg()        
        drawlfoot()        
        drawrfoot()        
        drawlarm()        
        drawrarm()        
        drawkill()
    
    wn.exitonclick()
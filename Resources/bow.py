##############################
#         BOW PATH           #
##############################
import random
import time
import math

level = 1       #set player level
items = []

def bow1():
    print("""
    While walking through the dark hallways of the prison, you encounter a fork. 
    The hallway goes to the left, and to the right.
    Which way will you go?

    Type 'LEFT' to go left, or 'RIGHT' to go right.
    
    """)
    # Get input
    c1 = input()
    time.sleep(1)
    ans = 'incorrect'
    while(ans=='incorrect'):
        # Option 1
        if(c1=="right"):
            print("You decide to head right...")
            ans = 'correct'
            right1()
        # Option 2
        elif(c1=="left"):
            print("You decide to head left...")
            ans='correct'
            left1()
        else:
            print("Invalid answer. Try again.")
            c1 = input()


def right1():       #right path
    print("""
    Around the right corner, there is a locked door.
    
    There is a keypad, but you don't know the code.

    'UNLOCK' to try random combinations. 'BACK' to turn around.
    """)
    # Get input
    c1 = input()
    time.sleep(1)
    ans = 'incorrect'
    while(ans=='incorrect'):
        # Option 1
        if(c1=="unlock"):
            print("")
            ans = 'correct'
            unlock()
        # Option 2
        elif(c1=="back"):
            print("you turn around and go to the left path...")
            ans='correct'
            left1()
        else:
            print("Invalid answer. Try again.")
            c1 = input()

def unlock():        #unlock door sequence
    print("""
    The keypad is a standard 10 digit model, with buttons layed out like you'd see on an old phone keypad.
    
    However, this one has a small screen so you can see what you're typing.

    On the screen, cursor awaits your input.

    [Type any combo of 4 numbers]

    """)
    
    code1 = random.randint(0000,9999)
    def codetest():
        time.sleep(1)
        num1 = input()

        if num1 == 'debugtestcode':
            print(code1)

        elif num1 != code1:
            print("""
        
            [INCORRECT! TRY AGAIN]

            It seems you got the code wrong...

            Try again? 'Y' or 'N'
        
            """)
            yn = input()
            if yn == 'y':
                codetest()
            elif yn == 'n':
                right1()
        elif num1 == code1:
            print("""

            [CORRECT]

            It seems that """,code1,""" was right...

            """)


    codetest()

def afterdoor():        #path after door
    ""



def left1():        #left path
    print("""
    Around the left corner, you encounter a guard!
    
    What will you do?

    'SHOOT', 'ITEM', or 'RUN'
    
    """)

def shoot():        #attack enemy sequence
    dmg = random.randint(level, level*3)



def run():      #run from battle sequence
    ""
    
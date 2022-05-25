import time
### Opening Scene ###
def part1():
    # Print opening message
    print(""" PyAdventure v1.0
          Scene 1 start.
          
          You wake up in a cold, abandoned prison cell. The door is unlocked.
          You hear screams from the floor below. A wave of dread falls over
          you.
          
          You lay next to a sword and a bow and quiver.
          Your next decision is an important one.
          
          Which weapon do you choose?
          Type "SWORD" or "BOW" to decide.
          """)
    # Get input
    c1 = input()
    time.sleep(2)
    ans = 'incorrect'
    while(ans=='incorrect'):
        # Option 1
        if(c1.upper()=="SWORD"):
            print("You pick up the sword, exit the prison cell and start your journey through the left side of the prison.")
            ans = 'correct'
            sword1()
        # Option 2
        elif(c1.upper()=="BOW"):
            print("You pick up the bow and quiver, exit the prison cell and start your journey through the right side of the prison. ")
            ans='correct'
            bow1()
        else:
            print("Invalid answer. Try again.")
            c1 = input()

##############################
#         SWORD PATH         #
##############################

def sword1():
    print(""" PyAdventure v1.0
          Sword path start.
          
          You wander through the prison and find the exit gate. There is a guard in front
          of the door. He does not see you.
          
          You can either try to kill the guard, or talk to him.
          Type "KILL" or "TALK" to decide.
          """)
    c1 = input()
    time.sleep(2)
    ans = 'incorrect'
    while(ans=='incorrect'):
        if(c1.upper()=="KILL"):
            print("You sneak up behind the guard and attack. Your sword bounces off his thick armor. The guard turns around and stabs you. You were killed.")
            ans = 'correct'
            sword1()
        elif(c1.upper()=="TALK"):
            print("You talk to the guard. He turned out to be very friendly and offered to help you.")
            ans='correct'
            sword2()
        else:
            print("Invalid answer. Try again.")
            c1 = input()

#unfinished below
def sword2():
    print(""" PyAdventure v1.0
          Sword path start.
          
          You wander through the prison and find the exit gate. There is a guard in front
          of the door. He does not see you.
          
          You can either try to kill the guard, or talk to him.
          Type "KILL" or "TALK" to decide.
          """)
    c1 = input()
    time.sleep(2)
    ans = 'incorrect'
    while(ans=='incorrect'):
        if(c1.upper()=="KILL"):
            print("You sneak up behind the guard and attack. Your sword bounces off his thick armor. The guard turns around and stabs you. You were killed.")
            ans = 'correct'
            sword1()
        elif(c1.upper()=="TALK"):
            print("You talk to the guard. He turned out to be very friendly and offered to help you.")
            ans='correct'
            sword2()
        else:
            print("Invalid answer. Try again.")
            c1 = input()
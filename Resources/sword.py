##############################
#         SWORD PATH         #
##############################

# -1 = null
# 1 = true
# 0 = false
didIgnore = -1

import time


def sword1():
    print("""
          Sword path start.
          
          You wander through the prison and find the exit gate. There is a guard in front
          of the door. He does not see you.
          
          You can either try to kill the guard, or talk to him.
          Type "KILL" or "TALK" to decide.
          """)
    c1 = input()
    time.sleep(2)
    ans = 'incorrect'
    while(ans == 'incorrect'):
        if(c1.upper() == "KILL"):
            print("You sneak up behind the guard and attack. Your sword bounces off his thick armor. The guard turns around and stabs you. You were killed.")
            ans = 'correct'
            sword1()
        elif(c1.upper() == "TALK"):
            print(
                "You talk to the guard. He turned out to be very friendly and offered to help you.")
            ans = 'correct'
            sword2()
        else:
            print("Invalid answer. Try again.")
            c1 = input()


def sword2():
    print("""
          Will you accept the guard's help?
          
          Type "YES" or "NO" to decide.
          """)
    c1 = input()
    time.sleep(2)
    ans = 'incorrect'
    while(ans == 'incorrect'):
        if(c1.upper() == "YES"):
            print(
                "The guard gave you directions to the nearest city. You continue on your way.")
            ans = 'correct'
            sword3()
        elif(c1.upper() == "NO"):
            print(
                "You politely decline the guard's offer, and continue off in your own direction.")
            ans = 'correct'
            sword3()
        else:
            print("Invalid answer. Try again.")
            c1 = input()


def sword3():
    print("""
          After traveling through the woods outside the prison, you come across a city. 
          Do you enter the city?
          
          Type "YES" or "NO" to decide.
          """)
    c1 = input()
    time.sleep(2)
    ans = 'incorrect'
    while(ans == 'incorrect'):
        if(c1.upper() == "YES"):
            print(
                "You walk inside the city. Right inside the gates you find an old man sitting on a bench by a well. You decide to talk to him.")
            ans = 'correct'
            sword4()
        elif(c1.upper() == "NO"):
            print(
                "You skip the town, and head off in a random direction. Surely this wont get you far...")
            ans = 'correct'
            swordSkip()
        else:
            print("Invalid answer. Try again.")
            c1 = input()


def swordSkip():
    print("""
          You are stopped by a group of guards.
          
          Guard: "You can't be here. Leave or we will have to take action."
          
          You tell them you have no idea where you are. They think you are lying.
          The guards chase you into a city.
          
          Type "OK" to continue.
          """)
    c1 = input()
    time.sleep(2)
    ans = 'incorrect'
    while(ans == 'incorrect'):
        if(c1.upper() == "OK"):
            print("You walk inside the city. Right inside the gates you find an old man sitting on a bench by a well. You decide to talk to him.")
            ans = 'correct'
            sword4()
        else:
            print("Invalid answer. Try again.")
            c1 = input()


def sword4():
    print("""
          You ask the old man for directions. You are trying to get home.
          
          Old Man: "Oh, I wish I could help you, but that dragon..."
          
          He starts whispering what sounds to be a prayer. You cant make out
          what he is saying.
          
          
          Do you keep talking with the old man?
          Type "YES" or "NO" to decide.
          """)
    c1 = input()
    time.sleep(2)
    ans = 'incorrect'
    while(ans == 'incorrect'):
        if(c1.upper() == "YES"):
            print(
                "You decide to keep talking to the old man.")
            didIgnore = 0
            ans = 'correct'
            sword5()
        elif(c1.upper() == "NO"):
            print(
                "You leave the old man alone.")
            didIgnore = 1
            ans = 'correct'
            sword6()
        else:
            print("Invalid answer. Try again.")
            c1 = input()

def sword5():
    print("""
          Old Man: "This dragon, he's keeping me his servant, please free me..."
          
          The old man starts whispering again.
          
          Type "OK" to continue.
          """)
    c1 = input()
    time.sleep(2)
    ans = 'incorrect'
    while(ans == 'incorrect'):
        if(c1.upper() == "OK"):
            print(
                "You walk inside the city. Right inside the gates you find an old man sitting on a bench by a well. You decide to talk to him.")
            ans = 'correct'
            sword6()
        else:
            print("Invalid answer. Try again.")
            c1 = input()

def sword6():
    print("""
          
          Type "YES" or "NO" to decide.
          """)
    c1 = input()
    time.sleep(2)
    ans = 'incorrect'
    while(ans == 'incorrect'):
        if(c1.upper() == "YES"):
            print(
                "You decide to keep talking to the old man.")
            didIgnore = 0
            ans = 'correct'
            sword5()
        elif(c1.upper() == "NO"):
            print(
                "You leave the old man alone.")
            didIgnore = 1
            ans = 'correct'
            sword6()
        else:
            print("Invalid answer. Try again.")
            c1 = input()

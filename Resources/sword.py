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
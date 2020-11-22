# for chosing random number b/w (0,2)

import random

# for counting no of wins.

user_wins=0
computer_wins=0

# displying rules of the game:

print("\t\t <<<<<Rules of the Game>>>>> \n"
      +"\nRock vs Paper------> Paper Wins \n"
      +"Rock vs Scissor----> Rock Wins \n"
      +"Paper vs Scisssor--> Scissor Wins")

# Loop will continue till user or computer
# wins more than two times

while user_wins<3 and computer_wins<3:

    # display what user will choose (1,2,3)
    
    print("\nEnter choice \n 0-->Rock \n 1-->Paper \n 2-->Scissor")
    
    # taking input from the user:
    
    user = int(input("Your Turn: "))
    
    #if user enter wrong value:
    
    while user > 2 or user < 0:
        user = int(input("Enter a valid input:"))

        # Assigning value to user's choice
        
    if user == 0:
        user_choice = 'Rock'
    if user == 1:
        user_choice = 'Paper'
    if user == 2:
        user_choice = 'Scissor'

        # display user's choice
        
    print("Your choice is: ",user_choice)
    
    print("Now its computer turn..")

    # let computer to choose random value(0,2)

    comp = random.randint(0,2)

    # Assigning value to computer's choice

    if comp == 0:
        comp_choice = 'Rock'
    elif comp == 1:
        comp_choice = 'Paper'
    else:
        comp_choice = 'Scissor'

        # user must know what's computer's choice.

    print("Computer choice is: ",comp_choice)
    
    print(user_choice, "VS", comp_choice)

    # condition for tie
    
    if ((user == 0 and comp == 0) or (user == 1 and comp == 1) or (user == 2 and comp == 2)):
        print("The match is draw")
        win=0
    elif ((user == 0 and comp == 1) or (user == 1 and comp == 0)):
        win='Paper'
    elif ((user==0 and comp==2)or(user==2 and comp==0)):
        win='Rock'
    elif (user==1 and comp==2)or(user==2 and comp==1):
        win='Scissor'
        
    # Applying condition, who wins?
        
    if win == user_choice:
        print("**You Win**")

        # if user wins increment
        
        user_wins+=1
    elif win == comp_choice:
        print("**Computer Wins**")

        # if computer wins increment
        
        computer_wins+=1

        # if match is tie
        
    elif win == 0:
        print("**No one Wins**")
        
if user_wins==3:
    print("You won more than 2 times. \n Thanks for playing")
else:
    print("Computer wins more than 2 times. \n Thanks for playing")

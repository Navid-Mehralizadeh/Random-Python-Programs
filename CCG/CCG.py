
import random

print("Winning Rules of the Colors choices Game as follows: "+ "\nEnter a number from one two five and match computer choice to Win the computer.") 

computer_score=0
player_score=0

while True: 
    print("red = 1 \nyellow = 2 \norange = 3 \ngreen = 4 \nblue = 5 \ntake a turn: ") 
    
    player_choice=int(input("Pick a number between 1 to 5: "))
    
    while player_choice>5 or player_choice<1:
        player_choice=int(input("Invalid input, try again: "))
        
    if player_choice == 1: 
        choice_col = 'red'
    elif player_choice == 2: 
        choice_col = 'yellow'
    elif player_choice == 3: 
        choice_col= 'orange'
    elif player_choice== 4: 
        choice_col = 'green'    
    else: 
        choice_col = 'blue'
        
    print("user color choice is: " + choice_col) 
    print("\nNow its computer turn to choose a color.......")
    
    computer_choice=random.randint(1, 5)
    
    while computer_choice == player_choice: 
        computer_choice = random.randint(1, 5) 
    
    if computer_choice == 1: 
        compu_choice_col = 'red'
    elif computer_choice == 2: 
        compu_choice_col = 'yellow'
    elif computer_choice == 3: 
        compu_choice_col = 'orange'
    elif computer_choice == 4: 
        compu_choice_col = 'green'    
    else: 
        compu_choice_col = 'blue'
        
        print("Computer color choice is: " + compu_choice_col) 

    if(choice_col == compu_choice_col):
        player_score += 1
        print("player_score: "+str(player_score))
        print("computer_score: "+str(computer_score))
    else:
        computer_score += 1
         
        print("player_score: " + str(player_score))
        print("computer_score: " +str(computer_score))
    print("Do you want to play again? (Y/N)") 
    answer = input() 

    if answer == 'n' or answer == 'N': 
        break 
    
    if computer_score == player_score:
        print("Game is Tied")
        print("\nThanks for playing") 
    elif computer_score < player_score:
        print("Player is Victorious")
        print("<== User wins ==>")
        print("\nThanks for playing")
    elif computer_score > player_score:
        print("\n<== Computer wins ==>")
        print("\nPlayer is Defeated")
        print("\nThanks for playing")    

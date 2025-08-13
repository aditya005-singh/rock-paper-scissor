import random

# Game option
choices = ['rock' , 'paper' , 'scisser']

while True: 
    #Get player choice
    player_choice = input("Enter your choice(rock , paper , scisser):").lower()


    # Get computer choice
    computer_choice = random.choice(choices)

    print(f"\n chose:{player_choice}")
    print(f"\nThe computer chose:{computer_choice}\n")


     # Determine the winner
    if player_choice == computer_choice: 
        print("It's a tie!") 
    elif (player_choice == 'rock' and computer_choice == 'scissors') or (player_choice == 'paper' and computer_choice == 'rock') or  (player_choice == 'scissors' and computer_choice == 'paper'): 
        print("You win!") 
    else: print("The computer wins!") 
    # Ask if the player wants to play again 
    play_again = input("\nDo you want to play again? (yes/no): ").lower() 
    if play_again != 'yes': 
        break 
    print("Thanks for playing!")



    

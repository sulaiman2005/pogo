import random

def stone_paper_scissors():
    user_choice = input("Enter your choice (stone, paper, scissors): ").lower()
    computer_choice = random.choice(['stone', 'paper', 'scissors'])
    
    print(f"Computer chose: {computer_choice}")
    
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 'stone' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'stone') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        print("You win!")
    else:
        print("You lose!")

stone_paper_scissors()

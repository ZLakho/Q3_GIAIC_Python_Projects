import random

def rock_paper_scissors():
    print("\nWelcome to Rock, Paper, Scissors!\n")
    choices = ["rock", "paper", "scissors"]
    
    while True:
        user_choice = input("Choose rock, paper, or scissors (or type 'quit' to exit): ").lower()
        if user_choice == "quit":
            print("Thanks for playing! Goodbye! ")
            break
        
        if user_choice not in choices:
            print("Invalid choice! Please choose rock, paper, or scissors.")
            continue
        
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")
        
        if user_choice == computer_choice:
            print("It's a tie! Try again!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("You win! Congratulations! 🎊")
        else:
            print("You lose! Better luck next time!")
        
        print("\nLet's play again! \n")

# Run the game
rock_paper_scissors()
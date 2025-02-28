import random

def guess_the_number():
    print("\nWelcome to the Ultimate Guess the Number Game! \n")
    print("I have selected a number between 1 and 100. Can you guess what it is? \n")
    
    number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10
    
    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts} - Enter your guess: "))
            attempts += 1
            
            if guess < number:
                print("Too low! Try again. ")
            elif guess > number:
                print("Too high! Try again. ")
            else:
                print(f"🎉 Congratulations! You guessed the number {number} correctly in {attempts} attempts! ")
                break
        except ValueError:
            print("Invalid input! Please enter a valid number. ")
    
    if attempts == max_attempts and guess != number:
        print(f"Game Over! The correct number was {number}. Better luck next time! ")
    
    print("\nThanks for playing! Play again for more fun! ")

guess_the_number()
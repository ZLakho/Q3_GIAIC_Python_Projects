import random

def choose_word():
    words = ["python", "developer", "hangman", "challenge", "programming","linkedin","giaic"]
    return random.choice(words)

def display(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def hangman():
    word = choose_word()
    guessed_letters = set()
    attempts = 6
    
    print("\nWelcome to Hangman!")
    
    while attempts > 0:
        print(f"\nWord: {display(word, guessed_letters)}")
        print(f"Attempts left: {attempts}")
        
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter!")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue
        
        guessed_letters.add(guess)
        
        if guess not in word:
            attempts -= 1
            print("Wrong guess!")
        else:
            print("Correct guess!")
        
        if set(word).issubset(guessed_letters):
            print(f"\nCongratulations! You guessed the word: {word}")
            return
    
    print(f"\nGame Over! The word was: {word}")

hangman()

import random
import string

def generate_password(length, use_digits=True, use_special=True):
    characters = string.ascii_letters  
    
    if use_digits:
        characters += string.digits 
    if use_special:
        characters += string.punctuation  
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# User input
length = int(input("Enter the desired password length: "))
use_digits = input("Include digits? (yes/no): ").lower() == "yes"
use_special = input("Include special characters? (yes/no): ").lower() == "yes"

# Generate and display password
password = generate_password(length, use_digits, use_special)
print(f"\nYour Generated Password: {password}")
import random

def mad_libs():
    print("\n Welcome to the Ultimate Mad Libs Game! \n")
    
    # List of stories with placeholders
    stories = [
        "Once upon a time, a {adjective} {noun} decided to {verb} in the {place}. Everyone was shocked!",
        "Yesterday, I saw a {adjective} {animal} {verb} near the {place}. It was the most hilarious thing ever!",
        "In a distant galaxy, a {adjective} {noun} was on a mission to {verb} the {place}. The adventure was legendary!",
        "The {adjective} scientist invented a {noun} that could {verb} anywhere, even in the {place}!"
    ]
    
    # Randomly selecting a story
    story_template = random.choice(stories)
    
    # User input for placeholders
    noun = input("Enter a noun: ")
    adjective = input("Enter an adjective: ")
    verb = input("Enter a verb: ")
    place = input("Enter a place: ")
    animal = input("Enter an animal (if needed, else press Enter): ")
    
    # Filling in the story
    story = story_template.format(noun=noun, adjective=adjective, verb=verb, place=place, animal=animal)
    
    print("\nHere is your hilarious Mad Libs story! \n")
    print(story)
    print("\nHope you had fun! Play again for a new story! \n")

# Run the game
mad_libs()

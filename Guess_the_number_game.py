import streamlit as st
import random

def initialize_game():
    st.session_state['random_number'] = random.randint(1, 100)
    st.session_state['attempts'] = 0
    st.session_state['game_over'] = False
    st.session_state['message'] = "Start guessing!"

def main():
    st.title("Number Guessing Game")
    
    if 'random_number' not in st.session_state:
        initialize_game()
    
    st.write("Guess a number between 1 and 100")
    guess = st.number_input("Enter your guess", min_value=1, max_value=100, step=1)
    
    if st.button("Check Guess") and not st.session_state['game_over']:
        st.session_state['attempts'] += 1
        if guess < st.session_state['random_number']:
            st.session_state['message'] = "Too low! Try again."
        elif guess > st.session_state['random_number']:
            st.session_state['message'] = "Too high! Try again."
        else:
            st.session_state['message'] = f"Congratulations! You guessed the number in {st.session_state['attempts']} attempts."
            st.session_state['game_over'] = True
    
    st.write(st.session_state['message'])
    st.write(f"Attempts: {st.session_state['attempts']}")

if __name__ == "__main__":
    main()

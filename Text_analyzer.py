import streamlit as st

def analyze_text(text):
    word_count = len(text.split())
    char_count = len(text)
    vowels = "aeiouAEIOU"
    vowel_count = sum(1 for char in text if char in vowels)
    contains_python = "Python" in text
    avg_word_length = char_count / word_count if word_count > 0 else 0
    
    return word_count, char_count, vowel_count, contains_python, avg_word_length

def main():
    st.title("Text Analyzer")
    
    text = st.text_area("Enter a paragraph:")
    
    if st.button("Analyze Text"):
        if text.strip():
            word_count, char_count, vowel_count, contains_python, avg_word_length = analyze_text(text)
            
            st.write(f"Total Words: {str(word_count)}")
            st.write(f"Total Characters (including spaces): {str(char_count)}")
            st.write(f"Total Vowels: {str(vowel_count)}")
            st.write(f"Contains 'Python': {'Yes' if contains_python else 'No'}")
            st.write(f"Average Word Length: {avg_word_length:.2f}")
        else:
            st.warning("Please enter a paragraph for analysis.")
    
    search_word = st.text_input("Enter a word to search:")
    replace_word = st.text_input("Enter a word to replace it with:")
    if st.button("Replace Word") and search_word and replace_word:
        modified_text = text.replace(search_word, replace_word)
        st.write("Modified Paragraph:")
        st.text_area("", modified_text, height=150)
    
    if st.button("Convert to Uppercase"):
        st.write("Uppercase Paragraph:")
        st.text_area("", text.upper(), height=150)
    
    if st.button("Convert to Lowercase"):
        st.write("Lowercase Paragraph:")
        st.text_area("", text.lower(), height=150)
        
if __name__ == "__main__":
    main()
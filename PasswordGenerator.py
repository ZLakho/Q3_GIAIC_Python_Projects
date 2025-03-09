import streamlit as st
import re
import random
import string

def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if any(char.islower() for char in password) and any(char.isupper() for char in password):
        score += 1
    else:
        feedback.append("Include both uppercase and lowercase letters.")

    if any(char.isdigit() for char in password):
        score += 1
    else:
        feedback.append("Include at least one number (0-9).")

    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("Include at least one special character (!@#$%^&*).")

    common_passwords = ["password", "123456", "password123", "qwerty", "admin"]
    if password.lower() in common_passwords:
        feedback.append("Your password is too common. Choose something unique.")
        score = 1  

    if score == 5:
        return "Strong", feedback
    elif score >= 3:
        return "Moderate", feedback
    else:
        return "Weak", feedback

def generate_strong_password(length=12):
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    return "".join(random.choice(characters) for _ in range(length))

def main():
    st.title("Password Strength")

    password = st.text_input("Enter a password:", type="password")

    if password:
        strength, feedback = check_password_strength(password)
        st.write(f"**Password Strength:** {strength}")

        if feedback:
            st.warning("Suggestions to improve your password:")
            for suggestion in feedback:
                st.write(f"- {suggestion}")

        if strength == "Weak":
            if st.button("Generate a Strong Password"):
                strong_password = generate_strong_password()
                st.success(f"Suggested Strong Password: `{strong_password}`")

if __name__ == "__main__":
    main()

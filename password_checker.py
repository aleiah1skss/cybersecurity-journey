import re

def check_password_strength(password):
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    # Count how many checks passed
    score = 5 - sum([length_error, digit_error, uppercase_error, lowercase_error, symbol_error])

    if score == 5:
        return "Strong 🔐"
    elif 3 <= score < 5:
        return "Moderate 🔒"
    else:
        return "Weak ❌"

# Get password input from the user
user_password = input("Enter your password to check its strength: ")
strength = check_password_strength(user_password)
print(f"Password Strength: {strength}")

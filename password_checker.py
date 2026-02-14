import re

def check_password_strength(password):
    score = 0

    # Length Check
    if len(password) >= 8:
        score += 1

    # Uppercase Check
    if re.search(r"[A-Z]", password):
        score += 1

    # Lowercase Check
    if re.search(r"[a-z]", password):
        score += 1

    # Number Check
    if re.search(r"[0-9]", password):
        score += 1

    # Special Character Check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1

    # Strength Result
    if score == 5:
        return "Very Strong Password 🔥"
    elif score >= 3:
        return "Moderate Password ⚠"
    else:
        return "Weak Password ❌"


# User Input
password = input("Enter your password: ")
result = check_password_strength(password)

print("Password Strength:", result)

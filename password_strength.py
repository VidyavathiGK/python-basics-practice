import re

def analyze_password(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add uppercase letters.")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add numbers.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add special characters.")

    ratings = {4: "Strong", 3: "Moderate", 2: "Weak", 1: "Very Weak", 0: "Very Weak"}
    return ratings.get(score, "Weak"), feedback

# Example usage:
if __name__ == "__main__":
    pwd = "SecurePassword123!"
    strength, tips = analyze_password(pwd)
    print(f"Password Strength: {strength}")
    if tips:
        print("Suggestions:", tips)

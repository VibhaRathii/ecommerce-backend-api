import re

def check_password_strength(password):
    
    if len(password) < 8:
        return "Weak Password ❌ (Minimum 8 characters required)"

    if not re.search("[A-Z]", password):
        return "Weak Password ❌ (Add at least one uppercase letter)"

    if not re.search("[a-z]", password):
        return "Weak Password ❌ (Add at least one lowercase letter)"

    if not re.search("[0-9]", password):
        return "Weak Password ❌ (Add at least one digit)"

    if not re.search("[@#$%^&*!]", password):
        return "Weak Password ❌ (Add at least one special character)"

    return "Strong Password ✅"


def main():
    print("===== Password Strength Checker =====")
    
    password = input("Enter your password: ")
    
    result = check_password_strength(password)
    
    print(result)


if __name__ == "__main__":
    main()
#Task 17: Validate Email Using Regular Expressions
import re

def is_valid_email(email):
    # Regular expression for a valid email
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(pattern, email) is not None

def main():
    # Input email
    email = input("Enter an email address: ")
    # Check if valid
    if is_valid_email(email):
        print("Valid email address")
    else:
        print("Invalid email address")

if __name__ == "__main__":
    main()
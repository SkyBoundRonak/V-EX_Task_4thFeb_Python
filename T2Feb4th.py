#Task 2: Write a program that checks if a word is a palindrome.
def is_palindrome(word):
    # Remove any spaces and convert to lowercase for case-insensitive comparison
    word = word.replace(" ", "").lower()
    # Check if the word is the same forwards and backwards
    return word == word[::-1]

def main():
    # Ask the user for input
    user_input = input("Enter a word or phrase: ")
    
    # Check if it's a palindrome
    if is_palindrome(user_input):
        print("Palindrome")
    else:
        print("Not Palindrome")

if __name__ == "__main__":
    main()
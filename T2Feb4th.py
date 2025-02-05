#Task 2: Write a program that checks if a word is a palindrome.
def is_palindrome(word):
    word = word.replace(" ", "").lower()
    # Check if the word is the same forwards and backwards
    return word == word[::-1]

def main():
    user_input = input("Enter a word or phrase: ")
    if is_palindrome(user_input):
        print("Palindrome")
    else:
        print("Not Palindrome")

if __name__ == "__main__":
    main()

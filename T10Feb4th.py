#Task 10: Generate a List of Squares Using List Comprehension
def generate_squares():
    return [i**2 for i in range(1, 11)]  # List comprehension

def main():
    # Generating the list of squares
    squares = generate_squares()
    # Print the result
    print(squares)

if __name__ == "__main__":
    main()

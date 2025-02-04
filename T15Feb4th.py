#Task 15: Calculate Factorial Using the math Library
import math

def calculate_factorial(n):
    return math.factorial(n)

def main():
    # Input number
    n = int(input("Enter a number: "))
    # Calculate factorial
    result = calculate_factorial(n)
    # Print the result
    print(f"{n}! = {result}")

if __name__ == "__main__":
    main()
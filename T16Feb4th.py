#Task 16: Recursive Factorial Function
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def main():
    # Input number
    n = int(input("Enter a number: "))
    # Calculate factorial
    result = factorial(n)
    # Print the result
    print(f"{n}! = {result}")

if __name__ == "__main__":
    main()
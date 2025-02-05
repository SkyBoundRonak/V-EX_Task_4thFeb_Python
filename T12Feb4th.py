#Task 12: Handle Division by Zero Error
def divide_numbers(a, b):
    try:
        result = a / b  # Attempt to divide
        return result
    except ZeroDivisionError:
        return "Cannot divide by zero"

def main():
    # Input numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
result = divide_numbers(num1, num2)
    print(result)

if __name__ == "__main__":
    main()

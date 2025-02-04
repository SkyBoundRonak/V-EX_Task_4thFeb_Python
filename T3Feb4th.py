#Task 3: Find the Largest Number in a List
def find_largest_number(numbers):
    # Using the built-in max() function
    return max(numbers)

def main():
    # Example input
    numbers = [2, 3, 1, 4, 9]
    
    # Find the largest number
    largest = find_largest_number(numbers)
    print(f"The largest number in the list is: {largest}")

if __name__ == "__main__":
    main()
#Task 9: Calculate the Average of a List of Numbers
def calculate_average(numbers):
    return sum(numbers) / len(numbers)  # Sum divided by count

def main():
    # Input list
    numbers = [2, 4, 6, 8, 10]
    # Calculate the average
    average = calculate_average(numbers)
    # Print the result
    print(f"Average of the list: {average}")

if __name__ == "__main__":
    main()
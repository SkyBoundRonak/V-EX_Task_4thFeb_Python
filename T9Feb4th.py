#Task 9: Calculate the Average of a List of Numbers
def calculate_average(numbers):
    return sum(numbers) / len(numbers)  

def main():   
   numbers = [2, 4, 6, 8, 10]
    average = calculate_average(numbers)
    print(f"Average of the list: {average}")

if __name__ == "__main__":
    main()

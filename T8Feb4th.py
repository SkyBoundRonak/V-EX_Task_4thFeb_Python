#Task 8: Sum of Even Numbers from 1 to n
def sum_of_evens(n):
    total = 0
    for i in range(1, n + 1):  # Loop from 1 to n
        if i % 2 == 0:  # Check if the number is even
            total += i  # Adding to the total
    return total

def main():
    n = int(input("Enter a number: "))
    result = sum_of_evens(n)
    print(f"Sum of even numbers from 1 to {n}: {result}")

if __name__ == "__main__":
    main()

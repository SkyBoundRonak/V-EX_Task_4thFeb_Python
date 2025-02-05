#Task 7: Determine if a Number is Positive, Negative, or Zero
def check_number(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

def main():  
    num = float(input("Enter a number: "))
     result = check_number(num)
    print(result)

if __name__ == "__main__":
    main()

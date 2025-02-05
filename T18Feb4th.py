#Task 18: Display Current Date and Time
from datetime import datetime

def get_current_datetime():
    now = datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")

def main():
    current_datetime = get_current_datetime()
    print(f"Current date and time: {current_datetime}")

if __name__ == "__main__":
    main()

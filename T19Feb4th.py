#Task 19: Measure Execution Time Using a Decorator
import time

def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Time taken to execute {func.__name__}: {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@measure_time
def example_function():
    time.sleep(2)  # Simulate a time-consuming task

def main():
    example_function()

if __name__ == "__main__":
    main()
#Task 4: Swap the First and Last Elements of a Tuple
def swap_first_last(t):
    # Convert the tuple to a list for swapping
    lst = list(t)
    # Swap the first and last elements
    lst[0], lst[-1] = lst[-1], lst[0]
    # Convert back to a tuple
    return tuple(lst)

def main():
    # Example input
    t = (1, 2, 3, 4)
    
    # Swap the first and last elements
    swapped_tuple = swap_first_last(t)
    print(f"Swapped tuple: {swapped_tuple}")

if __name__ == "__main__":
    main()
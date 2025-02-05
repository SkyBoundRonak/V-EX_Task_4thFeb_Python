#Task 4: Swap the First and Last Elements of a Tuple
def swap_first_last(t):
    lst = list(t)
    lst[0], lst[-1] = lst[-1], lst[0]
    return tuple(lst)

def main():
    t = (1, 2, 3, 4)
    
    # Swapping the first and last elements
    swapped_tuple = swap_first_last(t)
    print(f"Swapped tuple: {swapped_tuple}")

if __name__ == "__main__":
    main()

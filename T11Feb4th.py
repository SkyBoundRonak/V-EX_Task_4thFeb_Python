#Task 11: Sort a List of Tuples by the Second Element Using a Lambda Function
def sort_tuples_by_second_element(tuples_list):
    # Use the sorted() function with a lambda function as the key
    return sorted(tuples_list, key=lambda x: x[1])

def main():
    # list of tuples
    tuples_list = [(1, 2), (3, 1), (5, 4)]
    # Sorting the list
    sorted_list = sort_tuples_by_second_element(tuples_list)
    # Print the result
    print(sorted_list)

if __name__ == "__main__":
    main()

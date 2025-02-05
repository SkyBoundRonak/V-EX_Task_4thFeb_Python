#Task 6: Find the Intersection of Two Sets
def find_intersection(set1, set2):

    return set1.intersection(set2)

def main():
    # Input sets
    set1 = {1, 2, 3}
    set2 = {2, 3, 4}

    intersection = find_intersection(set1, set2)
 
    print(intersection)

if __name__ == "__main__":
    main()
    

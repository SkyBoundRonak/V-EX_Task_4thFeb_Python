#Task 13: Count Lines and Words in a Text File
def count_lines_and_words(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()  # Read all lines
            line_count = len(lines)  # Count lines
            word_count = sum(len(line.split()) for line in lines)  # Count words
            return line_count, word_count
    except FileNotFoundError:
        return "File not found."

def main():
    # Input file name
    filename = input("Enter the file name: ")
    result = count_lines_and_words(filename)
    if isinstance(result, tuple):
        line_count, word_count = result
        print(f"Number of lines: {line_count}")
        print(f"Number of words: {word_count}")
    else:
        print(result)

if __name__ == "__main__":
    main()

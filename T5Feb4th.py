#Task 5: Count the Frequency of Words in a Sentence
def count_word_frequency(sentence):
    # Split the sentence into words
    words = sentence.split()
    # Create a dictionary to store word frequencies
    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1  # Increment count if word exists
        else:
            frequency[word] = 1  # Add word to dictionary with count 1
    return frequency

def main():
    # Input sentence
    sentence = "apple banana apple grapes apple"
    # Count word frequencies
    word_frequency = count_word_frequency(sentence)
    # Print the result
    print(word_frequency)

if __name__ == "__main__":
    main()

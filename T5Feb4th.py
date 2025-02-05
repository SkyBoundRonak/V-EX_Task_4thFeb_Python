#Task 5: Count the Frequency of Words in a Sentence
def count_word_frequency(sentence):
    words = sentence.split()

    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1  # Increment count if word exists
        else:
            frequency[word] = 1  # Add word to dictionary with count 1
    return frequency

def main():
    
    sentence = "apple banana apple grapes apple"
  
    word_frequency = count_word_frequency(sentence)

    print(word_frequency)

if __name__ == "__main__":
    main()

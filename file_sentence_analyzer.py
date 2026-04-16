def file_sentence_analyzer(filename):
    # Step 1: Read the file
    with open(filename, "r") as file:
        sentence = file.read().strip()

    # Step 2: Split into words
    words = sentence.split()

    # Step 3: Perform analysis
    num_words = len(words)
    average_length = sum(len(word) for word in words) / num_words
    longest = max(words, key=len)
    shortest = min(words, key=len)

    # Step 4: Print results
    print("Sentence:", sentence)
    print("Number of words:", num_words)
    print("Average word length:", average_length)
    print("Longest word:", longest)
    print("Shortest word:", shortest)

# Run the function
file_sentence_analyzer("input.txt")

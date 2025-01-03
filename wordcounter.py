def count_words(text):
    """Counts the frequency of each word in the given text."""
    word_counts = {}
    words = text.lower().split()

    for word in words:

        cleaned_word = ''.join(char for char in word if char.isalnum())
        
        if cleaned_word in word_counts:
            word_counts[cleaned_word] += 1
        else:
            word_counts[cleaned_word] = 1

    return word_counts

def display_word_counts(word_counts):
    """Displays word frequencies in a readable format."""
    print("\n--- Word Frequencies ---")
    for word, count in word_counts.items():
        print(f"{word}: {count}")

def main():
    """Main function to run the word counter program."""
    while True:
        print("\n--- Word Counter ---")
        text = input("Enter ka dyan ng salita bro!!: ")

        if text.lower() == 'exit':
            print("Ok na bro alis kana. Adios!")
            break

        word_counts = count_words(text)
        display_word_counts(word_counts)

if __name__ == "__main__":
    main()

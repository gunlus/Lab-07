from string_package.manipulate import reverse_string, capitalize_words, remove_punctuation
from string_package.stats import count_characters, count_words, average_word_length

def main():
    input1 = input("Enter a sentence: ")

    print("Reversed Sentence:", reverse_string(input1))
    print("Capitalized Words:", capitalize_words(input1))
    print("Removed Punctuation:", remove_punctuation(input1))

    print("Characters:", count_characters(input1))
    print("Words:", count_words(input1))
    print("Average Word Length:", average_word_length(input1))

if __name__ == "__main__":
    main()

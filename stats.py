def count_characters(string):
    count = 0
    for char in string:
        count += 1
    return count

def count_words(string):
    return len(string.split())

def average_word_length(string):
    words = string.split()
    if not words:
        return 0
    return sum(len(word) for word in words) / len(words)

if __name__ == "__main__":
    print("Testing stats module")
    test_sentence = "100 yıl önce doğdu şanlı efsane,100 yaşında mutlu ol Fenerbahçe"
    print("Number of Characters:", count_characters(test_sentence))
    print("Number of Words:", count_words(test_sentence))
    print("Average Word Length:", average_word_length(test_sentence))

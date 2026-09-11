def count_word_frequency(sentence):
    words = sentence.lower().split()
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    return frequency

if __name__ == "__main__":
    text = "Python is great and python is fun for practice"
    result = count_word_frequency(text)
    for word, count in result.items():
        print(f"{word}: {count}")

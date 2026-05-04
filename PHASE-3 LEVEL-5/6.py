def count_words(s):
    words = s.split()
    return len(words)

# Example
sentence = "Hello world this is Python"
print("Number of words:", count_words(sentence))
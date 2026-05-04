def count_characters(s):
    count = 0
    for ch in s:
        if ch != ' ':
            count += 1
    return count

# Example
text = "Hello World"
print("Characters (excluding spaces):", count_characters(text))
def reverse_string(s):
    # Base case
    if len(s) == 0:
        return s
    
    # Recursive case
    return reverse_string(s[1:]) + s[0]

# Example
text = "HELLO"
print(reverse_string(text))
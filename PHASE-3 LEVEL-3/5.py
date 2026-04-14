def number_pattern(n):
    if n == 0:
        return
    number_pattern(n - 1)     # recursive call
    
    for i in range(1, n + 1):
        print(i, end=" ")
    print()

# Example
number_pattern(5)
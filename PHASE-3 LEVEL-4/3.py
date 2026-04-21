def triangle(n):
    # Base case
    if n == 0:
        return
    
    # Print current row (top-down → start from n)
    print('* ' * n)
    
    # Recursive call (reduce size)
    triangle(n - 1)

# Example
triangle(5)
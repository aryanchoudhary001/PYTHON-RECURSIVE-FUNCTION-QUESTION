def triangle(n):
    if n == 0:
        return
    print('* ' * n)
    triangle(n - 1)

# Example
triangle(5)
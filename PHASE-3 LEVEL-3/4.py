def triangle(n):
    if n == 0:
        return
    triangle(n - 1)        # recursive call
    print("* " * n)        # print current row

# Example
triangle(5)
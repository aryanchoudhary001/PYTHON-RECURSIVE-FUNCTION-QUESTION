#Print a triangle of stars recursively (bottom-up). 
def triangle(n):
    if n == 0:
        return
    triangle(n - 1)   # Recursive call
    print("*" * n)    # Print after recursion (bottom-up)

# Example
triangle(5)
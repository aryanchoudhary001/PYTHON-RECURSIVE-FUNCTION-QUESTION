 #Print a square of stars recursively (n×n). 
def print_row(n):
    # Base case for row
    if n == 0:
        return
    print("*", end=" ")
    print_row(n - 1)

def print_square(n):
    # Base case for square
    if n == 0:
        return
    
    # Print one row
    print_row(n)
    print()  # move to next line
    
    # Recursive call for remaining rows
    print_square(n - 1)

# Example
print_square(5)
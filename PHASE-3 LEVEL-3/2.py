#Print a square of stars recursively (n×n). 
def print_line(n):
    if n == 0:
        return
    print("*", end="")
    print_line(n - 1)

def print_square(n):
    if n == 0:
        return
    print_line(n)   # print one row
    print()         # move to next line
    print_square(n - 1)  # print remaining rows

# Example
print_square(4)
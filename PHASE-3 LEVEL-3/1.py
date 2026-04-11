#Print a line of n stars recursively. 
def print_stars(n):
    if n == 0:
        return
    print("*", end="")
    print_stars(n - 1)

# Example
print_stars(5)
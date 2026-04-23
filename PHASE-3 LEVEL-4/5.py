#Print pattern of numbers recursively (1 to n each row).
def print_numbers(row, col):
    if row == 0:
        return
    
    # First print smaller rows
    print_numbers(row - 1, col)
    
    # Then print numbers for current row
    for i in range(1, row + 1):
        print(i, end=" ")
    print()

# Example
print_numbers(5, 5)


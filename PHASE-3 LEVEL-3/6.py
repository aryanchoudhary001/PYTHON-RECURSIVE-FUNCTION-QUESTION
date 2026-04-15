def reverse_triangle(n):
    # Base case
    if n == 0:
        return
    
    # Print current row
    print("*" * n)
    
    # Recursive call
    reverse_triangle(n - 1)

# Input
n = int(input("Enter number of rows: "))
reverse_triangle(n)
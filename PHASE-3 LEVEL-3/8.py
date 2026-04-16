def inc_dec(n):
    if n == 0:
        return
    
    # Increasing part (before recursive call)
    print(n, end=" ")
    
    inc_dec(n - 1)
    
    # Decreasing part (after recursive call)
    print(n, end=" ")

# input
n = int(input("Enter a number: "))
inc_dec(n)
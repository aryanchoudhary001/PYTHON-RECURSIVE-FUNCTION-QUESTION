def sum_series(n):
    if n == 1:
        print("sum(1) = 1")
        return 1
    
    print(f"sum({n}) = {n} + sum({n-1})")
    result = n + sum_series(n - 1)
    print(f"Returning: sum({n}) = {result}")
    
    return result

# Input
n = int(input("Enter n: "))

# Function call
total = sum_series(n)

print("\nFinal Sum =", total)
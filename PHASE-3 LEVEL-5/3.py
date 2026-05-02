def second_largest(arr):
    first = second = float('-inf')
    
    for num in arr:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
            
    return second if second != float('-inf') else None

# Example
arr = [10, 5, 20, 8, 20]
print("Second Largest:", second_largest(arr))
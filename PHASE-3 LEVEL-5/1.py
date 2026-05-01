#Check if the array is sorted in ascending order. 
def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

# Example
arr = [1, 2, 3, 4, 5]
print("Sorted" if is_sorted(arr) else "Not Sorted")
def is_descending(arr):
    for i in range(len(arr) - 1):
        if arr[i] < arr[i + 1]:
            return False
    return True

# Example
arr = [9, 7, 5, 5, 2]

if is_descending(arr):
    print("Array is sorted in descending order")
else:
    print("Array is NOT sorted in descending order")
arr = list(map(int, input("Enter elements: ").split()))

if arr == sorted(arr):
    print("Array is sorted in ascending order")
else:
    print("Array is not sorted in ascending order")
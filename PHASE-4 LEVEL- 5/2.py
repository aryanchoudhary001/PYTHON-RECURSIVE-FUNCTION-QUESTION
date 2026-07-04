arr = list(map(int, input("Enter elements: ").split()))

if arr == sorted(arr, reverse=True):
    print("Array is sorted in descending order")
else:
    print("Array is not sorted in descending order")
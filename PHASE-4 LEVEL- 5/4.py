arr = list(map(int, input("Enter elements: ").split()))

arr = list(set(arr))
arr.sort()

if len(arr) >= 2:
    print("Second Smallest:", arr[1])
else:
    print("No second smallest element")
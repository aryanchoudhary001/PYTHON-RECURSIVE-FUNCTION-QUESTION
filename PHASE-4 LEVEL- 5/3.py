arr = list(map(int, input("Enter elements: ").split()))

arr = list(set(arr))
arr.sort()

if len(arr) >= 2:
    print("Second Largest:", arr[-2])
else:
    print("No second largest element")
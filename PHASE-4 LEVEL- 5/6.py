arr = list(map(int, input("Enter elements: ").split()))

total = sum(arr)
result = total - max(arr) - min(arr)

print("Sum:", result)
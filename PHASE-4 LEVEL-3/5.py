arr = [5, -2, 8, -1, 3]

for i in range(len(arr)):
    if arr[i] < 0:
        arr[i] = 0

print(arr)
arr = [3, 7, -2, 9, 5]

minimum = arr[0]

for num in arr:
    if num < minimum:
        minimum = num

print("Minimum element =", minimum)
arr1 = [1, 2, 3, 4]
arr2 = [3, 4, 5, 6]

count = 0

for i in arr1:
    if i in arr2:
        count += 1

print("Common elements count:", count)
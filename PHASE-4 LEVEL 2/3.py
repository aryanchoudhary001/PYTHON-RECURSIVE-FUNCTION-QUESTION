arr = [2, 4, 6, 4, 8, 4]
x = 4

for i in range(len(arr)):
    if arr[i] == x:
        print("First occurrence at index =", i)
        break
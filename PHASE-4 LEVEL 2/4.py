arr = [2, 4, 6, 4, 8, 4]
x = 4

for i in range(len(arr) - 1, -1, -1):
    if arr[i] == x:
        print("Last occurrence at index =", i)
        break
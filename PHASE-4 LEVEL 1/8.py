# Find the index of the maximum element

n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

max_index = 0

for i in range(1, n):
    if arr[i] > arr[max_index]:
        max_index = i

print("Index of maximum element is:", max_index)
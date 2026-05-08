# Find the sum of all elements in an array

n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    num = int(input())
    arr.append(num)

total = sum(arr)

print("Sum of all elements:", total)
# Input n and take n integers into an array; print them

n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    num = int(input())
    arr.append(num)

print("Array elements are:")

for i in arr:
    print(i, end=" ")
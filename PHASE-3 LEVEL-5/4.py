arr = list(set(arr))  # remove duplicates

arr.sort()

second_smallest = arr[1]
second_largest = arr[-2]

print("Second Smallest:", second_smallest)
print("Second Largest:", second_largest)
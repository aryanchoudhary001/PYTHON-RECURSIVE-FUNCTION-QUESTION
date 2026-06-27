# Input array
arr = [1, 2, 2, 3, 4, 4, 4, 5]

freq = {}

# Count frequency
for i in arr:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

# Print frequency
print("Frequency of each element:")
for key, value in freq.items():
    print(key, ":", value)
# Input array
arr = [1, 2, 2, 3, 4, 4, 4, 5]

freq = {}

# Count frequency
for i in arr:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

# Print duplicate elements
print("Elements appearing more than once:")
for key, value in freq.items():
    if value > 1:
        print(key)
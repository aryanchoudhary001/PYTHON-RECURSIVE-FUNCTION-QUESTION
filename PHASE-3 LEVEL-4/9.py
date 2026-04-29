arr = [1, 2, 3, 2, 4, 1, 5, 2]

freq = {}

for num in arr:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

print("Frequency Array:", freq)
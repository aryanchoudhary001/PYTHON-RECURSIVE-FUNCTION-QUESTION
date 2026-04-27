# Input arrays
A = [1, 2, 3, 4]
B = [5, 6, 7, 8]

# Empty result array
C = []

# Element-wise sum
for i in range(len(A)):
    C.append(A[i] + B[i])

# Output
print("Resultant Array:", C)
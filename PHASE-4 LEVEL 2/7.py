arr = [1, 2, 3, 4, 5, 6]

odd_sum = 0

for i in arr:
    if i % 2 != 0:
        odd_sum += i

print("Sum of odd elements =", odd_sum)
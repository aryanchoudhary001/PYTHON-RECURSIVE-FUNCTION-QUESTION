arr = [1, 2, 3, 4, 5, 6]

even_sum = 0

for i in arr:
    if i % 2 == 0:
        even_sum += i

print("Sum of even elements =", even_sum)
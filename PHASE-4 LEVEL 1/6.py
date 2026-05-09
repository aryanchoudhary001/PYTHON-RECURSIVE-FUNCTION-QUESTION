arr = [3, -1, 0, 5, -7, 0, 9]

positive = 0
negative = 0
zero = 0

for num in arr:
    if num > 0:
        positive += 1
    elif num < 0:
        negative += 1
    else:
        zero += 1

print("Positive numbers =", positive)
print("Negative numbers =", negative)
print("Zeroes =", zero)
arr = list(map(int, input("Enter elements: ").split()))

avg = sum(arr) / len(arr)
count = 0

for i in arr:
    if i > avg:
        count += 1

print("Average =", avg)
print("Elements greater than average:", count)
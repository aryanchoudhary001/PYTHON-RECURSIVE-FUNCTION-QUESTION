a = [1, 2, 3, 4, 5]
b = [3, 4, 5, 6, 7]

count = 0

for i in a:
    if i in b:
        count += 1

print("Common Elements Count:", count)
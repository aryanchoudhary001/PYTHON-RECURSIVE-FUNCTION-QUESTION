a = [1, 2, 3, 4]
b = [3, 4, 5, 6]

diff = []

for i in a:
    if i not in b:
        diff.append(i)

for i in b:
    if i not in a:
        diff.append(i)

print("Different Elements:", diff)
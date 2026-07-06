arr = list(map(int, input("Enter elements: ").split()))

visited = []

for i in arr:
    if i not in visited:
        count = 0
        for j in arr:
            if i == j:
                count += 1
        print(i, "->", count)
        visited.append(i)
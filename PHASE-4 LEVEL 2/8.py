arr = [2, 3, 4, 5, 6, 7, 8, 11]

count = 0

for num in arr:
    if num > 1:
        prime = True

        for i in range(2, num):
            if num % i == 0:
                prime = False
                break

        if prime:
            count += 1

print("Count of prime numbers =", count)
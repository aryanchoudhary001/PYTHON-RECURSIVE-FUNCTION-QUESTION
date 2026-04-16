def table(n, i=1):
    if i > 10:
        return
    print(n, "x", i, "=", n * i)
    table(n, i + 1)

# input
n = int(input("Enter a number: "))
table(n)
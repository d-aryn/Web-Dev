a, b  = int(input()), int(input())

if a < b:
    root = a ** 0.5

    start = int(root)

    if start * start < a:
        start += 1
    roo = b ** 0.5
    end = int(roo)

    for i in range(start, end + 1):
        print(i*i)
a = int(input())
s = 2
while a > 0:
    if a % s == 0:
        print(s)
        break
    else:
        s += 1
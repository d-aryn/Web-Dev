x, d  = int(input()), int(input())
count = 0
while x > 0:
    a = x % 10
    if d == a:
        count +=1
    x = x // 10
print(count)

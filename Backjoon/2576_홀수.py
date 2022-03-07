arr = [int(input()) for _ in range(7)]
result = 0
min_num = 101
for a in arr:
    if a%2:
        if min_num > a:
            min_num = a
        result += a
if result:
    print(result)
    print(min_num)
else:
    print(-1)
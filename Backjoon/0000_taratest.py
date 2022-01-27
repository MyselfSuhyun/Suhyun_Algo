m, n = map(int, input().split())
cnt = 0
while True:
    if m > 1:
        m -= 1
        cnt += 1
    else:
        break
    if n > 1:
        n -= 1
        cnt += 1
    else:
        break
print(cnt)
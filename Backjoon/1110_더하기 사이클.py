N = int(input())
ans = N
tmp = 0
cnt = 0
while True:
    tmp = N // 10 + N % 10
    N = (N % 10) * 10 + tmp%10
    cnt += 1
    if ans==N:
        break
print(cnt)
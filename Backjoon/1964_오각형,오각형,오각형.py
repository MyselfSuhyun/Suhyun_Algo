N = int(input())
ans = 5
tmp = 7
for i in range(1,N):
    ans += tmp
    tmp += 3
    ans %= 45678
print(ans)
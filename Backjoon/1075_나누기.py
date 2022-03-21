N = input()
F = int(input())
ans = int(N[:len(N)-2]+'00')
while ans%F:
    ans += 1
print(str(ans)[len(str(ans))-2:len(str(ans))])

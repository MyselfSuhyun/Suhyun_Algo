T = int(input())
for tc in range(1,T+1):
    d, n, s, p = map(int,input().split())
    if d + n*p > n*s:
        print('do not parallelize')
    elif d + n*p == n*s:
        print('does not matter')
    else:
        print('parallelize')
T = int(input())
for _ in range(T):
    N, S = input().split()
    for s in S:
        print(s*int(N),end='')
    print()
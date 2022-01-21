T = int(input())

for _ in range(T):
    if input() == '':
        N = int(input())
        c = 0
        for _ in range(N):
            c += int(input())
        if c%N:
            print('NO')
        else:
            print('YES')
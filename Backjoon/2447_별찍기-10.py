N = int(input())
arr = [[' ']*N for _ in range(N)]


def star(n):
    T = 3
    L = n//T
    if n == T:
        for i in range(T):
            if i%2:
                arr[i][:T] = ['*',' ','*']
            else:
                arr[i][:T] = ['*']*T
        return
    star(n//T)

    for i in range(0, n, L):
        for j in range(0, n, L):
            if i != L or j != L:
                for k in range(L):
                    arr[i+k][j:j+L] = arr[k][:L]


star(N)

for i in range(N):
    for j in range(N):
        print(arr[i][j], end='')
    print()

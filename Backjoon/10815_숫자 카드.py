N = int(input())
N_arr = list(map(int,input().split()))
N_arr.sort()
M = int(input())
M_arr = list(map(int,input().split()))
result = [0]*M

def binary(n,s,e):
    while s<=e:
        m = (s+e)//2
        if N_arr[m] == n:
            return 1
        elif N_arr[m] > n:
            e = m-1
        else:
            s = m+1
    return 0

for i in range(M):
    if binary(M_arr[i],0,N-1):
        result[i] = 1

print(*result)
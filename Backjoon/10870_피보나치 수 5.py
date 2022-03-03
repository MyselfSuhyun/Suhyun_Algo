# fibo = [0,1]
#
N = int(input())
#
# for n in range(2,N+1):
#     fibo.append(fibo[n-1]+fibo[n-2])
# print(fibo[N])

def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibo(n-1)+fibo(n-2)

print(fibo(N))

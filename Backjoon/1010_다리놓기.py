def factorial(n):
    rst = 1
    for i in range(1,n+1):
        rst *= i
    return rst

T = int(input())

for tc in range(1,T+1):
    n, m = map(int,input().split())
    result = factorial(m) // (factorial(n) * factorial(m - n))
    print(result)
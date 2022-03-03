T = int(input())
A = 100
B = 100
for tc in range(1,T+1):
    n, m = map(int,input().split())
    if n<m:
        A -= m
    elif n==m:
        continue
    elif n>m:
        B -= n
print(A)
print(B)
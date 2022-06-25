A, B = map(int,input().split())
C = int(input())
rst = A+B
if rst >= 2*C:
    print(rst-2*C)
else:
    print(rst)
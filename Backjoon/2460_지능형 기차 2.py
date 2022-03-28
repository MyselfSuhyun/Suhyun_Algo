rst = -1
current = 0
for _ in range(9):
    a, b= map(int,input().split())
    if current > a:
        current -= a
    else:
        current = 0
    if current > rst:
        rst = current
    current += b
    if current > rst:
        rst = current
print(rst)
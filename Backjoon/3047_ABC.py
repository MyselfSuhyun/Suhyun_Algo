arr = list(map(int,input().split()))
arr.sort()
S = input()
rst = []
for s in S:
    if s=='A':
        rst.append(arr[0])
    elif s=='B':
        rst.append(arr[1])
    elif s=='C':
        rst.append(arr[2])
print(*rst)
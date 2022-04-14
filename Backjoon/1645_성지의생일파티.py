N = int(input())
arr = [int(input()) for _ in range(N)]
rst = max(arr)
if max(arr)==1:
    print(2)
else:
    print(rst)
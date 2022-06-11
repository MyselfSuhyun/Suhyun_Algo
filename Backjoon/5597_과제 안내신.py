arr = [int(input()) for _ in range(28)]
arr.sort()
rst = [i for i in range(1,31)]
for r in rst:
    if r in arr:
        continue
    print(r)

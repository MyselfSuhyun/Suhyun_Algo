arr = [int(input()) for _ in range(5)]
arr.sort()
rst1 = 0
rst2 = arr[2]
for a in arr:
    rst1 += a
print(rst1//5)
print(rst2)
A, B = map(int,input().split())
arr = [0]*(B+1)

count = 0
for i in range(1,B+1):
    is_valid = False
    for j in range(i):
        arr[count] = i
        count += 1
        if count==B:
            is_valid = True
            break
    if is_valid:
        break
print(sum(arr[A-1:B]))
while True:
    arr = list(map(int,input().split()))
    if arr[0]==0:
        break
    rst = [arr[1]]
    for a in arr[2:]:
        if a == rst[-1]:
            continue
        else:
            rst.append(a)
    print(*rst,'$')

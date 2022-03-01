while True:
    arr = list(map(int, input().split()))
    if arr[0] == 0:
        break
    result = 1
    for i in range(arr[0]):
        sp = arr[2*i + 1]
        p = arr[2*i + 2]
        result = result*sp - p
    print(result)
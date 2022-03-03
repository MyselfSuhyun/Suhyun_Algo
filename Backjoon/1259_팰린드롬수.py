while True:
    arr = list(map(int,input()))
    if len(arr)==1 and not arr[0]:
        break
    for i in range(len(arr)//2):
        if arr[i]!=arr[len(arr)-1-i]:
            print('no')
            break
    else:
        print('yes')

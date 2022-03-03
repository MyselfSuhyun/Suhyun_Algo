arr = list(map(int,input().split()))
if not arr[0]%2 or not arr[1]%2:
    print(0)
else:
    print(min(arr[0],arr[1]))
arr = list(map(int,input().split()))
if arr.count(1)==0:
    print('*')
elif arr.count(1)==1:
    if arr[0]==1:
        print('A')
    elif arr[1]==1:
        print('B')
    elif arr[2]==1:
        print('C')
elif arr.count(1)==2:
    if arr[0]==0:
        print('A')
    elif arr[1]==0:
        print('B')
    elif arr[2]==0:
        print('C')
else:
    print('*')
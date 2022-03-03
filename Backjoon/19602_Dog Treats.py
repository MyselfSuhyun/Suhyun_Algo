arr = [int(input()) for _ in range(3)]
result = arr[0]*1 + arr[1]*2 + arr[2]*3
if result>=10:
    print('happy')
else:
    print('sad')
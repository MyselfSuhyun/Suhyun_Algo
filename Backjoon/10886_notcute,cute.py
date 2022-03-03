N = int(input())
arr = [int(input()) for _ in range(N)]
if arr.count(0)>arr.count(1):
    print('Junhee is not cute!')
else:
    print('Junhee is cute!')

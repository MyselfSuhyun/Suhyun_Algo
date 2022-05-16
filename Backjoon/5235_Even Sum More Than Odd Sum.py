N = int(input())
for _ in range(N):
    arr = list(map(int,input().split()))
    even = 0
    odd = 0
    for a in arr[1:]:
        if a%2:
            odd += a
        else:
            even += a
    if even > odd:
        print('EVEN')
    elif even == odd:
        print('TIE')
    else:
        print('ODD')
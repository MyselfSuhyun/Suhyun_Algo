T = int(input())

for tc in range(1,T+1):
    arr = list(input().split())
    tmp = float(arr[0])

    for a in arr[1:]:
        if a == '@':
            tmp *= 3
        elif a == '%':
            tmp += 5
        elif a == '#':
            tmp -= 7

    print(f'{tmp:.2f}')
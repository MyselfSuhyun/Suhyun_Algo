# 5052. 전화번호 목록
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = list(input() for _ in range(N))
    arr.sort()
    is_valid = True
    for i in range(N-1):
        L = len(arr[i])
        if arr[i] == arr[i+1][:L]:
            is_valid = False
            break

    if is_valid:
        print('YES')
    else:
        print('NO')
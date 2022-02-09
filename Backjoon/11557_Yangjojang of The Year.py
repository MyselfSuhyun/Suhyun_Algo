T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = []
    for _ in range(N):
        name, drinking = input().split()
        drinking = int(drinking)
        arr.append([name,drinking])
    arr.sort(key=lambda x : -x[1])
    print(arr[0][0])
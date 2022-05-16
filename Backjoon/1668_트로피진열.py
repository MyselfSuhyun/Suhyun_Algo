N = int(input())
arr = [int(input()) for _ in range(N)]
rsl = 1
rsr = 1

if N > 1:
    for i in range(N - 1):
        if arr[i] < arr[i + 1]:
            rsl += 1
        else:
            break
    for j in range(N - 1, -1, -1):
        if arr[j] < arr[j - 1]:
            rsr += 1
        else:
            break
print(rsl)
print(rsr)
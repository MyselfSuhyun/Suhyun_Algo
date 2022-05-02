T = int(input())
for _ in range(T):
    N = input()
    arr = [0]*10
    for n in N:
        arr[int(n)] = 1
    print(arr.count(1))
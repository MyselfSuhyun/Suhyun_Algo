import sys
input = sys.stdin.readline

N = int(input())

arr = [0]*10001

for _ in range(N):
    n = int(input())
    arr[n] += 1

for i in range(1,10001):
    if arr[i]:
        for _ in range(arr[i]):
            print(i)



# arr = [int(input()) for _ in range(N)]
# arr.sort()
# for a in arr:
#     print(a)
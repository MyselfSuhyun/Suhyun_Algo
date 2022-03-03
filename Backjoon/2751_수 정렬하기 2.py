# 첫째 줄에 수의 개수 N
N = int(input())
arr = []

for _ in range(N):
    arr.append(int(input()))

for a in sorted(arr):
    print(a)
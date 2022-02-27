import sys
input = sys.stdin.readline

for _ in range(3):
    N = int(input())
    arr = [int(input()) for _ in range(N)]
    if sum(arr)>0:
        print('+')
    elif sum(arr) == 0:
        print(0)
    elif sum(arr)<0:
        print('-')
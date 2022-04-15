import sys
input = sys.stdin.readline
N = int(input())
arr = [0,0]
for _ in range(N):
    A,B = map(int,input().split())
    if A>B:
        arr[0]+=1
    elif A<B:
        arr[1]+=1
print(*arr)
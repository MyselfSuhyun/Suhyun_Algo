import sys
input = sys.stdin.readline

A, B = map(int,input().split())
set_A = set(list(map(int,input().split())))
set_B = set(list(map(int,input().split())))

set_A-=set_B
print(len(set_A))
print(*sorted(set_A))
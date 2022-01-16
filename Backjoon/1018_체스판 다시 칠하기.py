import sys

def solve(y,x):
    s = arr[y][x]
    min_value = 0
    for i in range(8):
        if s == 'B':
            s = 'W'
        else:
            s = 'B'
        for j in range(8):
            if arr[y+i][x+j] != s:
                if s == 'B':
                    s ='W'
                else:
                    s = 'B'
            else:
                if s == 'B':
                    s ='W'
                else:
                    s = 'B'
                min_value +=1
    if arr[y][x] =='B':
        s = 'W'
    else:
        s = 'B'
    min_value2 = 0
    for i in range(8):
        if s == 'B':
            s = 'W'
        else:
            s = 'B'
        for j in range(8):
            if arr[y+i][x+j] != s:
                if s == 'B':
                    s ='W'
                else:
                    s = 'B'
            else:
                if s == 'B':
                    s ='W'
                else:
                    s = 'B'
                min_value2 +=1
    if min_value<min_value2:
        return min_value
    else:
        return min_value2

input = sys.stdin.readline
N, M = map(int,input().split())
arr = [list(input())[:M] for _ in range(N)]

result = 0xffffff

for i in range(N+1-8):
    for j in range(M+1-8):
        tmp = solve(i,j)
        if tmp < result:
            result = tmp

print(result)
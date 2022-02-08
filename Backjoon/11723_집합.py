import sys
input = sys.stdin.readline

N = int(input())

s = set()

for _ in range(N):
    tmp = input().split()

    if len(tmp) == 1:
        if tmp[0] == 'all':
            s = set([i for i in range(1,21)])
        elif tmp[0] == 'empty':
            s = set()
    elif len(tmp) == 2:
        if tmp[0] == 'add':
            s.add(int(tmp[1]))
        elif tmp[0] == 'remove':
            s.discard(int(tmp[1]))
        elif tmp[0] == 'check':
            if int(tmp[1]) in s:
                print(1)
            else:
                print(0)
        elif tmp[0] == 'toggle':
            if int(tmp[1]) in s:
                s.discard(int(tmp[1]))
            else:
                s.add(int(tmp[1]))

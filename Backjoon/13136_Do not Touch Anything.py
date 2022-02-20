R, C, N = map(int,input().split())

if R%N:
    rx = R//N + 1
else:
    rx = R//N

if C%N:
    ry = C//N +1
else:
    ry = C//N

print(rx*ry)
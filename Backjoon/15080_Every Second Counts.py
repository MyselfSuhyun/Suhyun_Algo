before = list(map(int,input().split(':')))
after = list(map(int,input().split(':')))

tb = before[0]*3600 + before[1]*60 + before[2]
ta = after[0]*3600 + after[1]*60 + after[2]

if tb>ta:
    print(ta-tb+3600*24)
else:
    print(ta-tb)
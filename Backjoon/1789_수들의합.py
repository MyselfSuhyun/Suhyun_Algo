N = int(input())
t = 1
while True:
    if t * (t+1) /2 > N:
        break
    t+=1
if N == 1:
    print(1)
else:
    print(t-1)
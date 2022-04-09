A = int(input())
B = int(input())
arr = []
for i in range(A,B+1):
    if i**(1/2)%1==0:
        arr.append(i)

if arr:
    print(sum(arr))
    print(min(arr))
else:
    print(-1)
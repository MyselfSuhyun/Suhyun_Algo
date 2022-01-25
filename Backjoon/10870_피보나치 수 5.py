fibo = [0,1]

N = int(input())

for n in range(2,N+1):
    fibo.append(fibo[n-1]+fibo[n-2])
print(fibo[N])
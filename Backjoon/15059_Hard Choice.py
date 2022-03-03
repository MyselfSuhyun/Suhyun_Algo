Ca = list(map(int,input().split()))
Cr = list(map(int,input().split()))

result = 0

for i in range(3):
    if Ca[i]<Cr[i]:
        result += Cr[i]-Ca[i]

print(result)
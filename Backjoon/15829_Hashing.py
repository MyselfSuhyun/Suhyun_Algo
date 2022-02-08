N = int(input())
S = input()
result = 0
K = 31
for i in range(N):
    result += (ord(S[i])-ord('a')+1)*(K**i)

print(result%1234567891)
S = input()
L = len(S)//2
for i in range(0,L+1):
    if S[i] != S[-1-i]:
        print(0)
        break
else:
    print(1)
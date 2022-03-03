alpha = ['c=','c-','dz=','d-','lj','nj','s=','z=']
a = ['c','d','n','l','s','z']
S = input()

cnt = 0
k = 0
while k < len(S):
    if S[k] in a:
        if k+1 < len(S) and S[k]+S[k+1] in alpha:
            k +=1
        elif k+2< len(S) and S[k]+S[k+1]+S[k+2] == 'dz=':
            k += 2
        k +=1
    else:
        k += 1
    # print(S[k],S[k] in a,)
    cnt +=1
    # print(k, cnt)
print(cnt)

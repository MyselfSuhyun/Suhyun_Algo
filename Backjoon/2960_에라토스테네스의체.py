N, K = map(int,input().split())

is_valid = [True]*(N+1)
count = 0
is_valid[0] = is_valid[1] = False
for i in range(2,N+1):
    valid = False
    if not is_valid[i]:
        continue
    for j in range(i,N+1,i):
        if is_valid[j]:
            is_valid[j] = False
            count +=1
            if count == K:
                print(j)
                valid = True
                break
    if valid:
        break

A,B = input().split()
Al = len(A)
Bl = len(B)
rst = [0,0]
for i in range(Al):
    tmp = False
    for j in range(Bl):
        if A[i]==B[j]:
            rst = [i,j]
            tmp = True
            break
    if tmp:
        break
for i in range(Bl):
    for j in range(Al):
        if i == rst[1]:
            print(A[j],end='')
        elif j == rst[0]:
            print(B[i],end='')
        else:
            print('.',end='')
    print('')
N = int(input())

for i in range(N+2):
    for j in range(N+2):
        if i==0 or i==N+1:
            print('@',end='')
        elif j==0 or j==N+1:
            print('@',end='')
        else:
            print(' ',end='')
    print('')
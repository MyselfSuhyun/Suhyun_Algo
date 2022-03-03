N = input()
L = len(N)
if L ==  2:
    A = int(N[0])
    B = int(N[1])
    print(A+B)
elif L == 4:
    print(20)
else:
    if int(N[L-2:])==10:
        print(int(N[0])+int(N[L-2:]))
    else:
        print(int(N[:L-1])+int(N[-1]))
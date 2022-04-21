while True:
    N = input()
    if N=="0":
        break
    while len(N)>1:
        tmp = 0
        for n in N:
            tmp += int(n)
        N = str(tmp)
    print(N)
t = 0
while True:
    t +=1
    N = int(input())
    if not N:
        break

    n1 = 3*N
    if n1%2:
        n2 = (n1+1)//2
        result = 'odd'
    else:
        n2 = n1//2
        result = 'even'

    n3 = 3*n2

    n4 = n3//9

    print(f'{t}. {result} {n4}')
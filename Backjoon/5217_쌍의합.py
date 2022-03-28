T = int(input())
for tc in range(1,T+1):
    N = int(input())
    rst = ''
    for i in range(1,13):
        for j in range(i+1,13):
            if i+j==N:
                rst += f'{i} {j}, '
            elif i+j>N:
                break
    print(f'Pairs for {N}: {rst[:-2]}')
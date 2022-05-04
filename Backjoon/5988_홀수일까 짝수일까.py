T = int(input())
for tc in range(1,T+1):
    N = int(input())
    N%=10
    if N%2:
        print('odd')
    else:
        print('even')
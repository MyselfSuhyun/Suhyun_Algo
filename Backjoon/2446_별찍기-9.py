N = int(input())

# for i in range(2*N-1,0,-2):
#     print(('*'*i).center(2*N-1,' '))
# for i in range(3,2*N,2):
#     print(('*' * i).center(2 * N - 1, ' '))
for i in range(N):
    print(f"{' ' * i}{'*' * (2 * (N - i) - 1)}")
for i in range(N - 2, -1, -1):
    print(f"{' ' * i}{'*' * (2 * (N - i) - 1)}")
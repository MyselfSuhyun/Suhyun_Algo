def solve(n):
    if n > N:
        return 0
    if n == N:
        return 1

    count =0
    for i in range(1,4):
        count += solve(n+i)
    return count


T = int(input())

for tc in range(1,T+1):
    N = int(input())

    print(solve(0))

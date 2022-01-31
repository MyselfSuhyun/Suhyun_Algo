# 2839. 설탕 배달

N = int(input())

answer = 0xffffff
n = 0
while 5 * n <= N:
    tmp = N - 5 * n
    k = -1
    for i in range(0, N+1, 3):
        if i == tmp:
            k = i // 3
            break

    if k != -1 and n + k < answer:
        answer = n + k
    n += 1
if answer == 0xffffff:
    print(-1)
else:
    print(answer)

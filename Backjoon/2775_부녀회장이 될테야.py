# 2775. 부녀회장이 될테야

# 첫 줄에 Test Case 의 수 T
T = int(input())
for _ in range(T):
    K = int(input())
    N = int(input())
    arr = [[i for i in range(1,N+1)]]
    for k in range(K):
        tmp = []
        t = 0
        for n in range(N):
            t += arr[-1][n]
            tmp.append(t)
        arr.append(tmp)
    print(arr[K][N-1])

# 한번 그려보자

# 1 4 10 20
# 1 3 6 10 15 ....
# 1 2 3 4 5 6 7 8 9 10 11 12 13 14
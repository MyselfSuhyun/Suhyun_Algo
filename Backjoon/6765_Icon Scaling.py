# 우선 배열에 담아주자
arr = ['*x*',' xx','* *']

# 몇배로 늘릴지 값을 받아주자
K = int(input())
# 우선 모든 길이가 3이니까 3을 변수에 담아주자
n = 3

# 우선 원본 높이을 가져오고
for i in range(n):
    # 높이를 K 배 늘려주자.
    for k in range(K):
        # 원본 길이를 가져오고
        for j in range(n):
            # 길이도 K배 늘려주자.
            for l in range(K):
                # 띄움 없이 print 해주고
                print(arr[i][j],end='')
        # 길이를 출력 끝냈으면 개행 해주자.
        print()

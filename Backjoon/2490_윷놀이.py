# A : 도 [ 1(배) : 1개, 0(등): 3개 ]
# B : 개 [ 1(배) : 2개, 0(등): 2개 ]
# C : 걸 [ 1(배) : 3개, 0(등): 1개 ]
# D : 윷 [ 1(배) : 4개, 0(등): 0개 ]
# E : 모 [ 1(배) : 0개, 0(등): 4개 ]

# 0 의 갯수에 따른 배열로 접근하자
arr = ['E','A','B','C','D']

# 윷은 총 3번 던진다 3번 출력하자.
N = 3
for _ in range(N):
    # 윷짝들의 상태를 list 로 받자.
    yut = list(map(int,input().split()))
    # 0 의 갯수를 센 뒤, arr 의 index 로 접근하자.
    print(arr[yut.count(0)])

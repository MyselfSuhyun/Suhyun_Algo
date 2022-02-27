# 1009. 분산처리

result = {
    0 : [10],
    1 : [1],
    2 : [2,4,8,6],
    3 : [3,9,7,1],
    4 : [4,6],
    5 : [5],
    6 : [6],
    7 : [7,9,3,1],
    8 : [8,4,2,6],
    9 : [9,1]
}

T = int(input())
for tc in range(1,T+1):
    a, b = map(int,input().split())
    # print(a**b%10)
    ans = result[a%10]
    print(ans[(b-1)%len(ans)])

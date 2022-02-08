# 높이 H 를 지정
N, M = map(int,input().split())
arr = list(map(int,input().split()))[:N]

# 자르는 K 가 존재한다면
# 내가 가지는건 얼마?
# K 이상일 경우 (a+b+c)-3K
start = 0
end = max(arr)
while start<=end:
    K = (start+end)//2
    tmp = 0
    for a in arr:
        if a-K>=0:
            tmp += a-K
    if tmp >=M:
        start = K +1
    else:
        end = K-1
print(end)
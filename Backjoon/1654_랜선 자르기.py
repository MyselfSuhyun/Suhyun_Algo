K, N = map(int,input().split())
arr = [int(input()) for _ in range(K)]
start, end = 1, max(arr) # 이분탐색 첫시작 1cm, 끝점 최대 길이

while start<=end:
    mid = (start+end) //2 # 중간위치
    lan = 0 # 랜선의 개수
    for i in arr:
        lan += i // mid # 분할 된 랜선의 수

    if lan >=N: # 랜선의 개수가 분기점
        start = mid + 1
    else:
        end = mid - 1
print(end)
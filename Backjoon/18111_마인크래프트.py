import sys
input = sys.stdin.readline

N, M, B = map(int,input().split())
arr= []
for _ in range(N):
    arr.append(list(map(int,input().split())))


#중간값을 구성
min_value = min(map(min,arr))
max_value = max(map(max,arr))
height = 0
# 최소시간을 구하자.
ans = 1e9
print(ans)
print(0xffffff)
for i in range(min_value, max_value+1):
    up_cnt = 0 #  1초걸림
    down_cnt = 0 # 2초걸림
    for j in range(N):
        for k in range(M):
            tmp = arr[j][k]-i
            if tmp > 0:
                down_cnt += tmp
            elif tmp < 0:
                up_cnt -= tmp
    if down_cnt+B >= up_cnt:
        time = 2*down_cnt + up_cnt
        if ans >= time:
            ans = time
            height = i

print(ans,height)
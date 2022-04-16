N, m, M, T, R = map(int,input().split())
# N : 운동하고자하는 시간
# m : 초기맥박
# M : 최대맥박
# T : 증가맥박
# R : 감소맥박
t = 0 # 걸린 시간
cnt = 0 # 운동시간
tmp = m # 현재 맥박
while cnt < N:
    if m+T> M:
        print(-1)
        break
    if tmp+T<=M:
        tmp += T
        cnt +=1
    else:
        tmp = max(tmp-R,m)
    t +=1
else:
    print(t)
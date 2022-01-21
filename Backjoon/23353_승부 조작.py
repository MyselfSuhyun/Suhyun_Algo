import sys
input = sys.stdin.readline

N = int(input())

arr = [list(map(int,input().split()))[:N] for _ in range(N)]

dy = [0,1,1,1]
dx = [1,0,1,-1]

result = 0

for i in range(N):
    v = [0]
    tmp = 0
    h = [0]
    tmp_h = 0
    for j in range(N):
        if arr[i][j]==1:
            tmp +=1
        elif arr[i][j]==2:
            if tmp and v[-1]:
                result = max(result,tmp+v[-1]+1)
            elif tmp and not v[-1]:
                result = max(result,tmp+1)
            else:
                result = max(result,1)
            v.append(tmp)
            tmp = 0
        else:
            result = max(result,tmp)
            v = [0]
            tmp = 0
        if arr[j][i]==1:
            tmp_h +=1
        elif arr[j][i]==2:
            if tmp_h and h[-1]:
                result = max(result,tmp_h+h[-1]+1)
            elif tmp_h and not h[-1]:
                result = max(result,tmp_h+1)
            else:
                result = max(result,1)
            h.append(tmp_h)
            tmp_h = 0
        else:
            result = max(result,tmp_h)
            h = [0]
            tmp_h = 0
    if tmp and v[-1]:
        result = max(result,tmp+v[-1]+1)
    elif tmp and not v[-1]:
        result = max(result,tmp)
    if tmp_h and h[-1]:
        result = max(result,tmp_h+h[-1]+1)
    elif tmp_h and not h[-1]:
        result = max(result,tmp_h)

# for i in range(N):
#     v = [0]
#     tmp = 0
#     h = [0]
#     tmp_h = 0
#     for j in range(0, N - i):
#         if arr[N-1-j-i][j]==1:
#             tmp +=1
#         elif arr[N-1-j-i][j]==2:
#             if tmp and v[-1]:
#                 result = max(result,tmp+v[-1]+1)
#             elif tmp and not v[-1]:
#                 result = max(result,tmp+1)
#             else:
#                 result = max(result,1)
#             v.append(tmp)
#             tmp = 0
#         else:
#             result = max(result,tmp)
#             v = [0]
#             tmp = 0
#         if arr[N-1-j][j+i]==1:
#             tmp_h +=1
#         elif arr[N-1-j][j+i]==2:
#             if tmp_h and h[-1]:
#                 result = max(result,tmp_h+h[-1]+1)
#             elif tmp_h and not h[-1]:
#                 result = max(result,tmp_h+1)
#             else:
#                 result = max(result,1)
#             h.append(tmp_h)
#             tmp_h = 0
#         else:
#             result = max(result,tmp_h)
#             h = [0]
#             tmp_h = 0
#     if tmp and v[-1]:
#         result = max(result,tmp+v[-1]+1)
#     elif tmp and not v[-1]:
#         result = max(result,tmp)
#     if tmp_h and h[-1]:
#         result = max(result,tmp_h+h[-1]+1)
#     elif tmp_h and not h[-1]:
#         result = max(result,tmp_h)
#
# for i in range(N):
#     v = [0]
#     tmp = 0
#     h = [0]
#     tmp_h = 0
#     for j in range(0, N - i):
#         if arr[i+j][j]==1:
#             tmp +=1
#         elif arr[i+j][j]==2:
#             if tmp and v[-1]:
#                 result = max(result,tmp+v[-1]+1)
#             elif tmp and not v[-1]:
#                 result = max(result,tmp+1)
#             else:
#                 result = max(result,1)
#             v.append(tmp)
#             tmp = 0
#         else:
#             result = max(result,tmp)
#             v = [0]
#             tmp = 0
#         if arr[j][i+j]==1:
#             tmp_h +=1
#         elif arr[j][i+j]==2:
#             if tmp_h and h[-1]:
#                 result = max(result,tmp_h+h[-1]+1)
#             elif tmp_h and not h[-1]:
#                 result = max(result,tmp_h+1)
#             else:
#                 result = max(result,1)
#             h.append(tmp_h)
#             tmp_h = 0
#         else:
#             result = max(result,tmp_h)
#             h = [0]
#             tmp_h = 0
#     if tmp and v[-1]:
#         result = max(result,tmp+v[-1]+1)
#     elif tmp and not v[-1]:
#         result = max(result,tmp)
#     if tmp_h and h[-1]:
#         result = max(result,tmp_h+h[-1]+1)
#     elif tmp_h and not h[-1]:
#         result = max(result,tmp_h)


print(result)

# for i in range(N):
#     tmp_v = 0
#     v_exchange = False
#     tmp_h = 0
#     h_exchange = False
#     for j in range(N):
#         if arr[i][j]==1:
#             tmp_v +=1
#         elif arr[i][j]==2 and v_exchange:
#             if result<tmp_v:
#                 result = tmp_v
#             tmp_v = 0
#             v_exchange = False
#         elif arr[i][j]==2 and not v_exchange:
#             tmp_v +=1
#             v_exchange = True
#         else:
#             if result<tmp_v:
#                 result = tmp_v
#             tmp_v = 0
#             v_exchange = False
#
#         if arr[j][i]==1:
#             tmp_h +=1
#         elif arr[j][i]==2 and h_exchange:
#             if result<tmp_h:
#                 result = tmp_h
#             tmp_h = 0
#             h_exchange = False
#         elif arr[j][i]==2 and not h_exchange:
#             tmp_h +=1
#             h_exchange = True
#         else:
#             if result<tmp_h:
#                 result = tmp_h
#             tmp_h = 0
#             h_exchange = False
#     result = max(result,tmp_h,tmp_v)
#
# for i in range(0,N):
#     tmp_v = 0
#     tmp_va = 0
#     v_exchange = False
#     v_arr = []
#     tmp_h = 0
#     h_exchange = False
#     for j in range(0,N-i):
#         if arr[i+j][j]==1:
#             print(1)
#             tmp_v +=1
#         elif arr[i+j][j]==2 and v_exchange:
#             print(2)
#             if result<tmp_v:
#                 result = tmp_v
#             tmp_v = 0
#             v_exchange = False
#         elif arr[i+j][j]==2 and not v_exchange:
#             print(3)
#             tmp_va = tmp_v
#             tmp_v +=1
#             v_exchange = True
#         else:
#             if result<tmp_v:
#                 result = tmp_v
#             tmp_v = 0
#             v_exchange = False
#
#         if arr[j][i+j]==1:
#             tmp_h +=1
#         elif arr[j][i+j]==2 and h_exchange:
#             if result<tmp_h:
#                 result = tmp_h
#             tmp_h = 0
#             h_exchange = False
#         elif arr[j][i+j]==2 and not h_exchange:
#             tmp_h +=1
#             h_exchange = True
#         else:
#             if result<tmp_h:
#                 result = tmp_h
#             tmp_h = 0
#             h_exchange = False
#     result = max(result,tmp_h,tmp_v)
#
# for i in range(N):
#     tmp_v = 0
#     v_exchange = False
#     tmp_h = 0
#     h_exchange = False
#     for j in range(0,N-i):
#         if arr[N-1-j-i][j] == 1:
#             tmp_v += 1
#         elif arr[N-1-j-i][j] == 2 and v_exchange:
#             if result < tmp_v:
#                 result = tmp_v
#             tmp_v = 0
#             v_exchange = False
#         elif arr[N-1-j-i][j] == 2 and not v_exchange:
#             tmp_v += 1
#             v_exchange = True
#         else:
#             if result < tmp_v:
#                 result = tmp_v
#             tmp_v = 0
#             v_exchange = False
#
#         if arr[N-1-j][j+i] == 1:
#             tmp_h += 1
#         elif arr[N-1-j][j+i] == 2 and h_exchange:
#             if result < tmp_h:
#                 result = tmp_h
#             tmp_h = 0
#             h_exchange = False
#         elif arr[N-1-j][j+i] == 2 and not h_exchange:
#             tmp_h += 1
#             h_exchange = True
#         else:
#             if result < tmp_h:
#                 result = tmp_h
#             tmp_h = 0
#             h_exchange = False
#     result = max(result, tmp_h, tmp_v)
#
# print(result)

# import sys
# input = sys.stdin.readline
# # 가로, 세로, 대각선 점수만 보니까, 해당 방향으로만 이동하자.
# dy = [0,1,1,1]
# dx = [1,0,1,-1]
#
# def solve(y,x,ex):
#     global result
#     # 이미 본 배멸
#     # visited= [0,0,0,0]
#     # # 가로, 세로, 대각성 가장 긴거를 찾는다..
#     # for i in range(4):
#     #     ny = y-dy[i]
#     #     nx = x-dx[i]
#     #     if 0<=ny<N and 0<=nx<N and arr[ny][nx]:
#     #         visited[i]=1
#     for i in range(4):
#         # tmp 후에 최대 점수인지 확인하기 위한 임시 변수
#         tmp = 1
#         # ny 와 nx 를 찾기 위해 계속 +1 한다.
#         n = 1
#         # 교환을 했는지 여부
#         exchange = ex
#         while True:
#             # 1 다음 지점의 방향을 확인한다.
#             ny = y + n*dy[i]
#             nx = x + n*dx[i]
#             # 그 범위가 바둑판 내에 있고, 값이 존재할 경우
#             if 0<=ny<N and 0<=nx<N and arr[ny][nx]:
#                 # 1이면 흑돌이다 +=1 해주자.
#                 if arr[ny][nx]==1:
#                     tmp +=1
#                 # 2이면 백돌이다. 교환 여부 확인후, +1 해주면서 1회 교환 사용했음을 표시하자.
#                 elif arr[ny][nx]==2 and not exchange:
#                     tmp +=1
#                     exchange = 1
#                 # 백돌이 한번 더나오고, 교환이 이루어 진상태면, break 걸자.
#                 else:
#                     break
#             # 범위를 벗어나거나 0이면 break 해주자
#             else:
#                 break
#             # 해당과정이 break 가 안걸리면 n += 1 을 통해 다음 좌표를 확인하자.
#             n += 1
#         print(tmp,end = ' ')
#         # 가로, 세로, 대각선 방향 점수를 계산하고, 교환이 이루어 졌고 최대 점수면 대입해주자.
#         if result < tmp:
#             result = tmp
#
#
# N = int(input())
# arr = [list(map(int,input().split()))[:N] for _ in range(N)]
#
# # 최대점수 출력을 위한 변수
# result = 0
#
# for i in range(N):
#     for j in range(N):
#         ## 흑돌의 지점을 찾는다.
#         if arr[i][j] == 1:
#             solve(i,j,0)
#         if arr[i][j] == 2:
#             solve(i,j,1)
# # 출력하자.
# print(result)

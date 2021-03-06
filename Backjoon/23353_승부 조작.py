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
# # ??????, ??????, ????????? ????????? ?????????, ?????? ??????????????? ????????????.
# dy = [0,1,1,1]
# dx = [1,0,1,-1]
#
# def solve(y,x,ex):
#     global result
#     # ?????? ??? ??????
#     # visited= [0,0,0,0]
#     # # ??????, ??????, ????????? ?????? ????????? ?????????..
#     # for i in range(4):
#     #     ny = y-dy[i]
#     #     nx = x-dx[i]
#     #     if 0<=ny<N and 0<=nx<N and arr[ny][nx]:
#     #         visited[i]=1
#     for i in range(4):
#         # tmp ?????? ?????? ???????????? ???????????? ?????? ?????? ??????
#         tmp = 1
#         # ny ??? nx ??? ?????? ?????? ?????? +1 ??????.
#         n = 1
#         # ????????? ????????? ??????
#         exchange = ex
#         while True:
#             # 1 ?????? ????????? ????????? ????????????.
#             ny = y + n*dy[i]
#             nx = x + n*dx[i]
#             # ??? ????????? ????????? ?????? ??????, ?????? ????????? ??????
#             if 0<=ny<N and 0<=nx<N and arr[ny][nx]:
#                 # 1?????? ???????????? +=1 ?????????.
#                 if arr[ny][nx]==1:
#                     tmp +=1
#                 # 2?????? ????????????. ?????? ?????? ?????????, +1 ???????????? 1??? ?????? ??????????????? ????????????.
#                 elif arr[ny][nx]==2 and not exchange:
#                     tmp +=1
#                     exchange = 1
#                 # ????????? ?????? ????????????, ????????? ????????? ????????????, break ??????.
#                 else:
#                     break
#             # ????????? ??????????????? 0?????? break ?????????
#             else:
#                 break
#             # ??????????????? break ??? ???????????? n += 1 ??? ?????? ?????? ????????? ????????????.
#             n += 1
#         print(tmp,end = ' ')
#         # ??????, ??????, ????????? ?????? ????????? ????????????, ????????? ????????? ?????? ?????? ????????? ???????????????.
#         if result < tmp:
#             result = tmp
#
#
# N = int(input())
# arr = [list(map(int,input().split()))[:N] for _ in range(N)]
#
# # ???????????? ????????? ?????? ??????
# result = 0
#
# for i in range(N):
#     for j in range(N):
#         ## ????????? ????????? ?????????.
#         if arr[i][j] == 1:
#             solve(i,j,0)
#         if arr[i][j] == 2:
#             solve(i,j,1)
# # ????????????.
# print(result)

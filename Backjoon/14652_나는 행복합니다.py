N, M ,K = map(int,input().split())

print(K//M)
print(K%M)


# x, y = 0,0
# cnt = 0
# for i in range(N):
#     is_valid = False
#     for j in range(M):
#         if cnt == K:
#             is_valid = True
#             y = i
#             x = j
#             break
#         cnt +=1
#     if is_valid:
#         break
# print(y,x)
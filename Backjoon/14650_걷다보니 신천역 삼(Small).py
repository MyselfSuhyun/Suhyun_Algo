N = int(input())
# arr = [0 for i in range(N)]
# rst = []
# def recur(cur):
#     if cur == N:
#         if arr[0]!=0:
#             tmp =''
#             for a in arr:
#                 tmp += str(a)
#             rst.append(int(tmp))
#         return
#     for i in range(3):
#         arr[cur] = i
#         recur(cur+1)
# recur(0)
# cnt = 0
# for r in rst:
#     if not r%3:
#         cnt +=1
# print(cnt)

arr = [0,2,6,18,54,162,486,1458,4374]
print(arr[N-1])
N = int(input())
arr = list(map(int,input().split()))[:N]
M = int(input())
ans = list(map(int,input().split()))[:M]

dic = dict()
for i in arr:
    dic[i]=1

for j in ans:
    if dic.get(j):
        print(1)
    else:
        print(0)



# for a in ans:
#     if a in arr:
#         print(1)
#     else:
#         print(0)


# tmp = [0] * (max(ans) + 1)
#
# for i in arr:
#     tmp[i] = 1
#
# for j in ans:
#     if tmp[j]:
#         print(1)
#     else:
#         print(0)
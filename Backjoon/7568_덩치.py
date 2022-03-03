N = int(input())
arr =[list(map(int,input().split())) for i in range(N)]

for i in arr:
    count = 1
    for j in arr:
        if i[0] < j[0] and i[1] < j[1]:
            count +=1
    print(count, end =' ')
# arr.sort(key=lambda x:-x[1] and -x[2])
# result = [0]*N
# weight = arr[0][1]
# tall = arr[0][2]
# cnt = 1
# for i in range(len(arr)):
#     if weight <= arr[i][1] and tall <= arr[i][2]:
#         result[arr[i][0]] = cnt
#     elif weight <arr[i][1] or tall < arr[i][2]:
#         if weight <arr[i][1]:
#             weight = arr[i][1]
#         if tall <= arr[i][2]:
#             tall = arr[i][2]
#         result[arr[i][0]]= cnt
#     else:
#         cnt = i+1
#         result[arr[i][0]] = cnt
#         weight = arr[i][1]
#         tall = arr[i][2]
# print(*result)
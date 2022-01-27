from itertools import combinations

N = 9
arr = [int(input()) for _ in range(N)]
arr.sort()
solve = list(combinations(arr,7))
for s in solve:
    if sum(s)==100:
        for i in s:
            print(i)
        break
# arr.sort()
# solve = sum(arr)
#
# print(solve)
# for i in range(9):
#     for j in range(i+1,9):
#         if solve-arr[i]-arr[j]==100:
#             for k in range(9):
#                 if k == i or k==j:
#                     continue
#                 else:
#                     print(arr[k])

# N = int(input())
# dict_sort ={}
# for _ in range(N):
#   age, name = input().split()
#   if dict_sort.get(age):
#     dict_sort[age].append(name)
#   else:
#     dict_sort[age] = [name]
# print(dict_sort)

arr = []
for _ in range(N):
    arr.append(input().split())
arr.sort(key = lambda x: int(x[0]))
for a in arr:
    print(*a)
# import sys
# dict_sort = {}
# for _ in range(N) :
#     age, name = sys.stdin.readline().split()
#     print(age, name)

import sys

N = int(sys.stdin.readline())

dict_sort = {}
for _ in range(N):
    age, name = sys.stdin.readline().split()
    if dict_sort.get(int(age)):
        ## 키값이 있으면 append 로 value를 추가한다.
        dict_sort[int(age)].append(name)
    else:
        ## 키값이 없으면 key:value 를 추가해 key값을 넣는다.
        dict_sort[int(age)] = [name]
result = sorted(dict_sort.keys())
# print(dict_sort)
for k in result:
    tmp = dict_sort[k]
    for t in tmp:
        print(k,t)
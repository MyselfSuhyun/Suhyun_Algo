N = int(input())
arr = [int(input()) for _ in range(N)]
arr.sort()

dict_num = dict()
count = -1
min_num = []
for a in arr:
    if dict_num.get(a):
        dict_num[a]+=1
    else:
        dict_num[a]=1
    if dict_num[a] > count:
        count = dict_num[a]
        min_num = [a]
    elif dict_num[a] == count:
        min_num.append(a)
# 1. 산술 평균
print(round(sum(arr)/N))
# 2. 중앙 값
print(arr[N//2])
# 3. 최빈 값
if len(min_num)>=2:
    print(min_num[1])
else:
    print(*min_num)
# 4. 범위
print(max(arr)-min(arr))

# import sys
# input = sys.stdin.readline
#
# # 오목의 총 줄 갯수는 19개이므로
# n = 19
# arr = [list(map(int,input().split()))[:19] for _ in range(n)]
# print(arr)

S = input()

idx = 0
dic_alpha = dict()
for i in range(ord('a'),ord('z')+1):
    dic_alpha[chr(i)]=-1
for j in S:
    if dic_alpha[j]==-1:
        dic_alpha[j]=idx
    idx+=1

for v in dic_alpha.values():
    print(v,end=' ')

print(*dic_alpha.values())
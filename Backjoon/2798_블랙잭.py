from itertools import permutations
import sys

n, m = map(int, sys.stdin.readline().split())
cards = list(map(int, sys.stdin.readline().split()))

# result = 9999999
# for i in range(n-2) : # 맨 첫장부터 n-2까지 도는 거
#     # sum_3cards = 0
#     for j in range(i+1, n-1) : # 그 다음장부터 n-1까지 도는 거
#         for k in range(j+1, n) : # 3번째 장부터 마지막장까지 도는 거
#             sum_3cards = cards[i]+cards[j]+cards[k]
#             if m - sum_3cards <= result and m>=sum_3cards:
#                 result = m - sum_3cards
# print(m-result)
cards.sort()
sum_3cards = set(permutations(cards,3))
result = 9999999
for i in sum_3cards:
    if m - sum(i)<=result and m>=sum(i):
        result = m-sum(i)
print(m-result)


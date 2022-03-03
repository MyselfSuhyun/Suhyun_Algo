# 10610. 30
import sys
input = sys.stdin.readline
from itertools import permutations

# 문자열로 받자
S = sorted(list(input().rstrip()),reverse=True)

if sum(map(int,S))%3 != 0 or S[-1] != '0':
    print(-1)
else:
    print(''.join(S))

# 메모리 초과
# arr = list(permutations(S,len(S)))
# result = -1
#
# for a in arr:
#     if a[0] != '0':
#         tmp = int(''.join(a))
#         if not tmp%30 and result<tmp:
#             result = tmp
# print(result)
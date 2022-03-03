# 11656. 접미사배열
import sys
input = sys.stdin.readline

S = input().rstrip()

arr = ['']*(len(S))

for i in range(len(S)):
    arr[i] = S[i:]
arr.sort()

for a in arr:
    print(a)
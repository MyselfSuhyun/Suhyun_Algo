import sys

n, k, a, b = map(int, sys.stdin.readline().split())
arr = [k] * n

# 리스트 원소 줄여주기 위에 설명 적어 둠
li = [i for i in arr[::a]]

day = 0
while 0 not in li:  # li 리스트 안에 0이 있으면 멈춤

    for i in range(len(li)):
        li[i] -= 1  # 모든 꽃 매일 1씩 먼저 줄어들고
    li[li.index(min(li))] +=b

    day += 1  # 날짜 추가해주고 ㅠㅠ
print(day)
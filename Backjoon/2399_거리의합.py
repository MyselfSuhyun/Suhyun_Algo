n = int(input())
x = sorted(list(map(int, input().split())))
result = 0
for i in range(n):
    result += x[i] * 2 * (2 * i - n + 1)
print(result)
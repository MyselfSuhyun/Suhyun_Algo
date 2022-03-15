N, M = input().split()
result = 0
for n in N:
    for m in M:
        result += int(n)*int(m)

print(result)
arr = [int(input()) for _ in range(5)]
result = 0
for a in arr:
    if a<=40:
        result += 40
    else:
        result += a
print(result//5)
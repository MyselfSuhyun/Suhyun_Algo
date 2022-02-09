S = input()
result = 10
tmp = S[0]
for s in S[1:]:
    if s == tmp:
        result += 5
    else:
        tmp = s
        result += 10
print(result)
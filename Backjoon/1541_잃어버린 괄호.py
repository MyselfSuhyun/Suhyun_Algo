S = input()
arr = []
X = []
tmp = ''
for s in S:
    if '0'<=s<='9':
        tmp += s
    else:
        arr.append(int(tmp))
        tmp = ''
        X.append(s)
arr. append(int(tmp))
answer = arr[0]
i = 1
for x in X:
    if x == '+':
        answer += arr[i]
        i +=1
    else:
        answer -= sum(arr[i:])
        break
print(answer)
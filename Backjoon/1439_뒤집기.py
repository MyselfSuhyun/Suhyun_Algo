# 1439. 뒤집기
S = input()
tmp = S[0]
count = 0
for s in S:
    if tmp == s:
        continue
    else:
        tmp = s
        count +=1
print((count+1)//2)
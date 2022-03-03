not_self = [True]*10001

for i in range(1,10001):
    tmp = i
    s = str(i)
    for j in range(len(s)):
        tmp += int(s[j])
    if tmp<=10000:
        not_self[tmp]=False

for i in range(1,10001):
    if not_self[i]:
        print(i)

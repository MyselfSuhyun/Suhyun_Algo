S = input()
answer = input()
ans = ''
for s in S:
    if not '0'<=s<='9':
        ans+=s
if answer in ans:
    print(1)
else:
    print(0)
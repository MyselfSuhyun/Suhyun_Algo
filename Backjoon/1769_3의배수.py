N = input()
cnt = 0
while len(N)>1:
    tmp =0
    for n in N:
        tmp += int(n)
    N = str(tmp)
    cnt +=1
print(cnt)
if not int(N) % 3:
    print('YES')
else:
    print('NO')
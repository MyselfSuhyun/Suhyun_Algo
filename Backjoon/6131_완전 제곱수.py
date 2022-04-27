N = int(input())
cnt = 0
for i in range(1,501):
    for j in range(i,501):
        if j**2-i**2>N:
            break
        elif j**2-i**2==N:
            cnt +=1

print(cnt)
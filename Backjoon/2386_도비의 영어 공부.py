while True:
    S = input()
    if S=='#':
        break
    a = S[0]
    cnt = 0
    for b in S[2:]:
        if a==b.lower():
            cnt +=1
    print(a,cnt)

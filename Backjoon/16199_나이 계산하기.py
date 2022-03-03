# 16199. 나이 계산하기
yb, mb, db = map(int,input().split())
ya, ma, da = map(int,input().split())

if mb < ma:
    r1 = ya-yb
elif mb == ma:
    if db<=da:
        r1 = ya-yb
    else:
        r1 = ya-yb-1
else:
    r1 = ya-yb-1
r2 = ya-yb +1
print(r1)
print(r2)
print(r2-1)